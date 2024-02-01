from hashnode_py.queries.mutations import update_webhook, remove_webhook


class Webhook:
    def __init__(self, data: dict, client):
        """
        Initialize the Webhook object with the given data and client.
        Args:
            data (dict): The dictionary containing webhook data.
            client: The client object for interacting with the webhook.
        Attributes:
        """
        super(Webhook, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.publication_id = data['publication']['id']
        self.url = data['url']
        self.events = data['events']
        self.secret = data['secret']
        self.created_at = data['createdAt']
        self.updated_at = data['updatedAt']

    def update(self, url: str = None, events: list[str] = None, secret: str = None):
        """
        Updates a webhook for the publication.
        Args:
            url (str): The URL of the webhook.
            events (list): The webhook will be triggered if any of the selected events occur.
                post_published, post_updated, post_deleted, static_page_published,
                static_page_edited, static_page_deleted.
            secret (str): The secret to use for the webhook.
        """
        for i in events:
            events.append(i.upper())

        if not url:
            url = self.url
        if not events:
            events = self.events
        if not secret:
            secret = self.secret
        query = update_webhook
        variables = {'webhookId': self.id, 'url': url, 'events': events, 'secret': secret}
        data = self.client.fetch_data(query=query, variables=variables)
        return Webhook(data, self.client)

    def delete(self):
        """
        Deletes a webhook for the publication.
        """
        query = remove_webhook
        variables = {'webhookId': self.id}
        self.client.fetch_data(query=query, variables=variables)
        return f'Successfully deleted webhook'
