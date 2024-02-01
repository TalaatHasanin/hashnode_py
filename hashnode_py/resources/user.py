from hashnode_py.queries.mutations import *
from hashnode_py.queries.user_queries import *
from hashnode_py.resources.publication import Publication
from hashnode_py.resources.post import Post
from hashnode_py.resources.tag import Tag
from hashnode_py.resources.follow import Follows, Followers
from hashnode_py.resources.comment import Comment, Reply


class User:
    def __init__(self, data: dict, client):
        """
        Initialize the User object with the given data and client.
        Args:
            data (dict): The dictionary containing user data.
            client: The client object for interacting with the user.
        Attributes:
            username: The username of the user.
            id: The unique identifier of the user.
            name: The name of the user.
            bio: The bio text of the user.
            profile_picture: The URL of the user's profile picture.
            followers: The number of followers the user has.
            followings: The number of users the user is following.
            tagline: The tagline of the user.
            date_joined: The date when the user joined.
            location: The location of the user.
            available_for: The availability status of the user.
            ambassador: The ambassador status of the user.
            deactivated: The deactivation status of the user.
            following: The follow status of the user.
            follows_back: The follow back status of the user.
            is_pro: The pro-status of the user.
        """
        super(User, self).__init__()
        self.client = client
        self.data = data
        self.username = data['username']
        self.id = data['id']
        self.name = data['name']
        self.bio = data['bio']['text']
        self.profile_picture = data['profilePicture']
        self.followers_count = data['followersCount']
        self.followings_count = data['followingsCount']
        self.tagline = data['tagline']
        self.date_joined = data['dateJoined']
        self.location = data['location']
        self.available_for = data['availableFor']
        self.deactivated = data['deactivated']
        self.following = data['following']
        self.follows_back = data['followsBack']
        self.is_pro = data['isPro']

    def get_social_media(self, filter: str = 'all'):
        """
        Fetches the social media links of a user.
        Parameters:
            filter (str): Optional. Specify which social media link to return. Defaults to 'all'.
        Returns:
            dict or str: If filter is 'all', returns all social media links in a dictionary. If filter is a valid social media platform, returns the link for that platform as a string.
        """
        query = social_media
        variables = {'username': self.username}
        data = self.client.fetch_data(query=query, variables=variables)
        data = data['user']['socialMediaLinks']
        social_data = {
            'website': data['website'],
            'github': data['github'],
            'twitter': data['twitter'],
            'instagram': data['instagram'],
            'facebook': data['facebook'],
            'stackoverflow': data['stackoverflow'],
            'linkedin': data['linkedin'],
            'youtube': data['youtube']
        }
        if filter == 'all':
            return social_data
        elif filter in data:
            return social_data[filter]

    def get_badges(self, filter: str = 'description') -> list:
        """
        Retrieves badges for a user based on the specified filter.
        Args:
            filter (str): The filter criteria for the badges. Defaults to 'name'.
        Returns:
            list: A list of badges based on the specified filter.
        """
        query = badges
        variables = {'username': self.username}
        data = self.client.fetch_data(query=query, variables=variables)
        data = data['user']['badges']
        if filter == 'all':
            result = [{'badge': badge} for badge in data]
            return result
        else:
            result = [{'badge': badge['name'], filter: badge[filter]} for badge in data]
            return result

    def get_publications(self, role: bool = False) -> list:
        """
        Retrieves publications for a user based on the specified filter.
        Args:
            role (bool): Whether to include the role of each publication.
        Returns:
            list: A list of dictionaries containing Publication objects.
        """
        query = publications
        variables = {'username': self.username}
        data = self.client.fetch_data(query=query, variables=variables)
        data = data['user']['publications']['edges']

        # Extract nodes and roles
        nodes = [Publication(i['node'], self.client) for i in data]
        roles = [i['role'] for i in data]

        if role:
            # Add a role to each publication
            result = [{'publication': node.title, 'role': role} for node, role in zip(nodes, roles)]
            return result
        else:
            result = [node for node in nodes]
            return result

    def get_posts(self, page_size: int, page_number: int):
        """
        Retrieves posts for a user based on the specified page size and page number.
        Args:
            page_size (int): The number of posts to retrieve per page.
            page_number (int): The page number to retrieve.
        Returns:
            list: A list of dictionaries containing Post objects.
        """
        query = posts
        variables = {'username': self.username, 'page_size': page_size, 'page': page_number}
        data = self.client.fetch_data(query=query, variables=variables)
        data = data['user']['posts']['nodes']
        result = [Post(i, self.client) for i in data]
        return result

    def get_tags_following(self):
        """
        Retrieves tags for a user based on the specified page size and page number.
        Returns:
            list: A list of dictionaries containing Tag objects.
        """
        query = tags_following
        variables = {'username': self.username}
        data = self.client.fetch_data(query=query, variables=variables)
        data = data['user']['tagsFollowing']
        result = [Tag(i, self.client) for i in data]
        return result

    def get_followers(self, page_size: int, page_number: int) -> Followers:
        """
        Retrieves followers for a user based on the specified page size and page number.
        Returns:
            Followers: A followers objects representing the followers of the specified user.
        """
        result = self.client.get_followers(self.username, page_size, page_number)
        return result

    def get_follows(self, page_size: int, page_number: int) -> Follows:
        """
        Retrieves follows for a user based on the specified page size and page number.
        Returns:
            Follows: A follows objects representing the follows of the specified user.
        """
        result = self.client.get_follows(self.username, page_size, page_number)
        return result

    def toggle_follow(self, username: str):
        """
        Follows or unfollows a user based on the specified username and id.
        Args:
            username (str): The username of the user to follow or unfollow.
        """
        query = toggle_follow
        variables = {'username': username}
        data = self.client.fetch_data(query=query, variables=variables)
        status = data['toggleFollowUser']['user']['following']
        if status:
            return f'Successfully followed {username}'
        elif not status:
            return f'Successfully unfollowed {username}'

    def like_post(self, post_id: str, likes: int = 1):
        """
        Likes a post based on the specified post id.
        Args:
            post_id (str): The ID of the post to like or unlike.
            likes (int): The number of likes to add or remove. Default to 1.
        """
        query = like_post
        variables = {'postId': post_id, 'likesCount': likes}
        data = self.client.fetch_data(query=query, variables=variables)
        title = data['likePost']['post']['title']
        return f'Successfully liked "{title}"'

    def like_comment(self, comment_id: str, likes: int = 1):
        """
        Likes a comment based on the specified comment id.
        Args:
            comment_id (str): The ID of the comment to like or unlike.
            likes (int): The number of likes to add or remove. Default to 1.
        """
        query = like_comment
        variables = {'commentId': comment_id, 'likesCount': likes}
        data = self.client.fetch_data(query=query, variables=variables)
        author = data['likeComment']['comment']['author']['username']
        return f'Successfully liked "{author}" comment'

    def add_comment(self, post_id: str, content: str) -> Comment:
        """
        Adds a comment to a post based on the specified post id and content.
        Args:
            post_id (str): The ID of the post to add the comment to.
            content (str): The content of the comment to add in markdown.
        Returns:
            Comment: A comment object representing the added comment.
        """
        query = add_comment
        variables = {'postId': post_id, 'content': content}
        data = self.client.fetch_data(query=query, variables=variables)
        comment_data = data['addComment']['comment']
        return Comment(comment_data, self.client)

    def update_comment(self, comment_id: str, content: str) -> Comment:
        """
        Updates a comment based on the specified comment id and content.
        Args:
            comment_id (str): The ID of the comment to update.
            content (str): The content of the comment to update in markdown.
        Returns:
            Comment: A comment object representing the updated comment.
        """
        query = update_comment
        variables = {'commentId': comment_id, 'content': content}
        data = self.client.fetch_data(query=query, variables=variables)
        comment_data = data['updateComment']['comment']
        return Comment(comment_data, self.client)

    def remove_comment(self, comment_id: str) -> str:
        """
        Removes a comment based on the specified comment id.
        Args:
            comment_id (str): The ID of the comment to remove.
        """
        query = remove_comment
        variables = {'commentId': comment_id}
        self.client.fetch_data(query=query, variables=variables)
        return f'Successfully removed comment'

    def add_reply(self, comment_id: str, content: str) -> Comment:
        """
        Adds a comment to a post based on the specified post id and content.
        Args:
            comment_id (str): The ID of the comment to add the reply to.
            content (str): The content of the comment to add in markdown.
        Returns:
            Comment: A comment object representing the added comment.
        """
        query = add_reply
        variables = {'commentId': comment_id, 'content': content}
        data = self.client.fetch_data(query=query, variables=variables)
        comment_data = data['addReply']['reply']
        return Reply(comment_data, self.client)

    def update_reply(self, comment_id: str, reply_id: str, content: str) -> Comment:
        """
        Updates a comment based on the specified comment id and content.
        Args:
            comment_id (str): The ID of the comment to update.
            reply_id (str): The ID of the reply to update.
            content (str): The content of the comment to update in markdown.
        Returns:
            Comment: A comment object representing the updated comment.
        """
        query = update_reply
        variables = {'commentId': comment_id, 'content': content, 'replyId': reply_id}
        data = self.client.fetch_data(query=query, variables=variables)
        comment_data = data['updateReply']['reply']
        return Reply(comment_data, self.client)

    def remove_reply(self, comment_id: str, reply_id: str) -> str:
        """
        Removes a comment based on the specified comment id.
        Args:
            comment_id (str): The ID of the comment to remove.
            reply_id (str): The ID of the reply to remove.
        """
        query = remove_reply
        variables = {'commentId': comment_id, 'replyId': reply_id}
        self.client.fetch_data(query=query, variables=variables)
        return f'Successfully removed reply'


