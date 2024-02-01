class Comment(object):
    def __init__(self, data: dict, client):
        """
        Initialize the Comment object with the given data and client.
        Args:
            data (dict): The dictionary containing comment data.
            client: The client object for interacting with the comment.
        """
        super(Comment, self).__init__()
        self.client = client
        self.id = data['id']
        self.content = data['content']['text']
        self.author = data['author']['username']
        self.date_added = data['dateAdded']
        self.stamp = data['stamp']
        self.total_reactions = data['totalReactions']
        self.my_total_reactions = data['myTotalReactions']


class Reply(Comment):
    def __init__(self, data: dict, client):
        """
        Initialize the Reply object with the given data and client.
        Args:
            data (dict): The dictionary containing reply data.
            client: The client object for interacting with the reply.
        """
        super(Reply, self).__init__(data, client)
