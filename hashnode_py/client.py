from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

from hashnode_py.resources.user import User
from hashnode_py.resources.publication import Publication
from hashnode_py.resources.post import Post
from hashnode_py.resources.tag import Tag
from hashnode_py.resources.follow import Follows, Followers
from hashnode_py.queries.user_queries import user_info
from hashnode_py.queries.post_queries import post_info, feed
from hashnode_py.queries.publication_queries import publication_info
from hashnode_py.queries.follow_queries import follows_info, followers_info
from hashnode_py.queries.tag_queries import tag_info


class HashnodeClient:
    def __init__(self, token: str):
        """
        Initializes the class with a token and sets up the client with the provided token for API requests.
        :param token: Str - the token used for authorization
        :return: None
        """
        if not token:
            raise ValueError("No token provided")
        self.token = token
        headers = {
            'Authorization': self.token
        }
        _transport = RequestsHTTPTransport(
            url='https://gql.hashnode.com/',
            headers=headers,
            use_json=True,
        )
        self.client = Client(
            transport=_transport,
            fetch_schema_from_transport=True
        )

    def get_user(self, username: str) -> User:
        """
        Retrieves user information using the provided username and returns a User object.
        Args:
            username (str): The username of the user to retrieve information for.
        Returns:
            User: An object representing the user's information.
        """
        query = user_info
        variables = {'username': username}
        data = self.fetch_data(query=query, variables=variables)
        data = data['user']
        user = User(data, HashnodeClient(self.token))
        return user

    def get_publication(self, host_url: str = None, host_id: str = None) -> Publication:
        """
        Fetches publication information for a given host or id.
        Args:
            host_url (str): The host for which the publication information is to be fetched.
            host_id (str): The id for which the publication information is to be fetched.
        Returns:
            Publication: The publication information for the given host or id.
        """
        query = publication_info
        if host_id:
            variables = {'id': host_id}
        elif host_url:
            variables = {'host': host_url}
        else:
            raise ValueError("Either host or id must be provided")
        data = self.fetch_data(query=query, variables=variables)
        data = data['publication']
        publication = Publication(data, HashnodeClient(self.token))
        return publication

    def get_post(self, post_id: str) -> Post:
        """
        Fetches post information for a given post id.
        Args:
            post_id (str): The id for which the post information is to be fetched.
        Returns:
            Post: The post information for the given post id.
        """
        query = post_info
        variables = {'id': post_id}
        data = self.fetch_data(query=query, variables=variables)
        data = data['post']
        post = Post(data, HashnodeClient(self.token))
        return post

    def get_tag(self, tag_slug: str) -> Tag:
        """
        Fetches tag information for a given tag slug.
        Args:
            tag_slug (str): The slug for which the tag information is to be fetched.
        Returns:
            Tag: The tag information for the given tag slug.
        """
        query = tag_info
        variables = {'slug': tag_slug}
        data = self.fetch_data(query=query, variables=variables)
        data = data['tag']
        tag = Tag(data, HashnodeClient(self.token))
        return tag

    def get_followers(self, username: str, page_size: int, page_number: int) -> Followers:
        """
        Retrieves followers for a user based on the specified page size and page number.
        Args:
            username (str): The username of the user to retrieve followers for.
            page_size (int): The number of followers to retrieve per page.
            page_number (int): The page number to retrieve.
        Returns:
            Followers: A followers objects representing the followers of the specified user.
        """
        query = followers_info
        variables = {'username': username, 'pageSize': page_size, 'page': page_number}
        data = self.fetch_data(query=query, variables=variables)
        nodes = data['user']['followers']['nodes']
        users = [User(i, HashnodeClient(self.token)) for i in nodes]
        page_info = data['user']['followers']['pageInfo']
        result = Followers(users, page_info, HashnodeClient(self.token))
        return result

    def get_follows(self, username: str, page_size: int, page_number: int) -> Follows:
        """
        Retrieves follows for a user based on the specified page size and page number.
        Args:
            username (str): The username of the user to retrieve follows for.
            page_size (int): The number of follows to retrieve per page.
            page_number (int): The page number to retrieve.
        Returns:
            Follows: A follows objects representing the follows of the specified user.
        """
        query = follows_info
        variables = {'username': username, 'pageSize': page_size, 'page': page_number}
        data = self.fetch_data(query=query, variables=variables)
        nodes = data['user']['follows']['nodes']
        users = [User(i, HashnodeClient(self.token)) for i in nodes]
        page_info = data['user']['follows']['pageInfo']
        result = Follows(users, page_info, HashnodeClient(self.token))
        return result

    def get_feed(self, number_of_posts: int,
                 feed_type: str = None,
                 min_reading_time: int = None,
                 max_reading_time: int = None,
                 tags_id: list = None) -> list[Post]:
        """
        Retrieves posts for a user based on the specified page size and page number.
        Args:
            number_of_posts (int): The number of posts to retrieve.
            feed_type (str, optional): The type of feed to retrieve. Defaults to None.
            min_reading_time (int, optional): The minimum reading time of the posts. Defaults to None.
            max_reading_time (int, optional): The maximum reading time of the posts. Defaults to None.
            tags_id (list, optional): The list of tag ids to retrieve. Defaults to None.
        Returns:
            list: A list of dictionaries containing Post objects.
        """
        query = feed
        variables = None

        if number_of_posts > 50:
            raise ValueError("Number of posts must be less than 50")

        if feed_type:
            feed_type = feed_type.upper()
            variables = {
                "first": number_of_posts,
                "type": feed_type
            }

        if min_reading_time:
            variables = {
                "first": number_of_posts,
                "minReadTime": min_reading_time
            }

        if max_reading_time:
            variables = {
                "first": number_of_posts,
                "maxReadTime": max_reading_time
            }

        if tags_id:
            variables = {
                "first": number_of_posts,
                "tags": tags_id
            }

        if not feed_type and not min_reading_time and not max_reading_time and not tags_id:
            variables = {
                "first": number_of_posts
            }

        data = self.fetch_data(query=query, variables=variables)
        edges = data['feed']['edges']
        nodes = [Post(i['node'], self.client) for i in edges]
        result = [node for node in nodes]
        return result

    def fetch_data(self, query: str, variables: dict = None) -> dict:
        """
        Fetches data from the GraphQL API using the provided variables, headers, and query.
        :param variables: Dict - the variables used in the query
        :param query: Str - the query to be executed
        :return: Dict - the data returned from the query
        """
        if not variables:
            variables = {}

        response = self.client.execute(
            document=gql(query),
            variable_values=variables
        )

        return response
