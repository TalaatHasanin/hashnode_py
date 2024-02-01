class Tag:
    def __init__(self, data: dict, client):
        """
        Initialize the Tag object with the given data and client.
        Args:
            data (dict): The dictionary containing tag data.
            client: The client object for interacting with the tag.
        """
        super(Tag, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.name = data['name']
        self.slug = data['slug']
        self.logo = data['logo']
        self.tagline = data['tagline']
        self.info = data['info']['text'] if data['info'] else None
        self.followers_count = data['followersCount']
        self.posts_count = data['postsCount']

