from hashnode_py.queries.post_queries import *
from hashnode_py.resources.comment import Comment


class Post:
    def __init__(self, data: dict, client):
        """
        Initializes a Post object with the provided data and client.
        Args:
            data (dict): The data dictionary containing post information.
            client: The client object.
        Returns:
            None
        """
        super(Post, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.slug = data['slug']
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author = data['author']['username']
        self.url = data['url']
        self.publication = data['publication']['title']
        self.cuid = data['cuid']
        self.cover_image = data['coverImage']['url'] if data['coverImage'] else None
        self.brief = data['brief']
        self.read_time = data['readTimeInMinutes']
        self.views = data['views']
        self.reaction_count = data['reactionCount']
        self.response_count = data['responseCount']
        self.featured = data['featured']
        self.bookmarked = data['bookmarked']
        self.featured_at = data['featuredAt']
        self.published_at = data['publishedAt']
        self.updated_at = data['updatedAt']
        self.is_followed = data['isFollowed']
        self.content = data['content']['markdown']

    def get_comments(self, limit: int = 10) -> list:
        """
        Fetches comments for a post.
        Args:
            limit (int): The maximum number of comments to fetch. Default to 10.
        Returns:
            list: A list of Comment objects.
        """
        query = comments
        variables = {'id': self.id, 'first': limit}
        data = self.client.fetch_data(query=query, variables=variables)
        edges = data['post']['comments']['edges']
        nodes = [Comment(i['node'], self.client) for i in edges]
        result = [node for node in nodes]
        return result
