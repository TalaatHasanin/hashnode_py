class ScheduledPost:
    def __init__(self, data: dict, client):
        """
        Initialize the ScheduledPost object with the given data and client.
        Args:
            data (dict): The dictionary containing scheduled post data.
            client: The client object for interacting with the scheduled post.
        Attributes:
        """
        super(ScheduledPost, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.author = data['author']['username']
        self.draft_id = data['draft']['id']
        self.scheduled_date = data['scheduledDate']
        self.scheduled_by = data['scheduledBy']['username']
        self.publication_id = data['publication']['id']

