class Followers:
    def __init__(self, users, page_info, client):
        """
        Initialize the Followers object with the given data and client.
        Args:
            users: The list of User objects.
            page_info: The page information.
            client: The client object for interacting with the followers.
        """
        super(Followers, self).__init__()
        self.client = client
        self.users = users
        self.page_info = page_info
        self.has_next_page = page_info['hasNextPage']
        self.has_previous_page = page_info['hasPreviousPage']
        self.next_page = page_info['nextPage']
        self.previous_page = page_info['previousPage']


class Follows(Followers):
    def __init__(self, users, page_info, client):
        """
        Initialize the Follows object with the given data and client.
        Args:
            users: The list of User objects.
            page_info: The page information.
            client: The client object for interacting with the follows.
        """
        super(Follows, self).__init__(users, page_info, client)
