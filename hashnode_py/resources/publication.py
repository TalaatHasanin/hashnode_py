from datetime import datetime
from hashnode_py.queries.mutations import (
    publish_post, update_post, remove_post, create_webhook, publish_draft)
from hashnode_py.resources.draft import Draft
from hashnode_py.queries.publication_queries import drafts
from hashnode_py.resources.webhook import Webhook


class Publication:
    def __init__(self, data: dict, client):
        """
        Initialize the Tag object with the given data and client.
        Args:
            data (dict): The dictionary containing tag data.
            client: The client object for interacting with the tag.
        """
        super(Publication, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.title = data['title']
        self.display_title = data['displayTitle']
        self.description_seo = data['descriptionSEO']
        self.about = data['about']['text'] if data['about'] else None
        self.url = data['url']
        self.author = data['author']['username']
        self.header_color = data['headerColor']
        self.ga_tracking_id = data['integrations']['gaTrackingID']
        self.followers_count = data['followersCount']
        self.pinned_post = data['pinnedPost']['id'] if data['pinnedPost'] else None

    def publish_post(self, title: str, content: str, tags_id: list = None, tags_slug: list[dict] = None,
                     subtitle: str = None, image_url: str = None, slug: str = None, origin_url: str = None,
                     disable_comments: bool = False, publish_as: str = None, series_id: str = None,
                     scheduled: bool = False, enable_table: bool = False, co_authors: list = None):
        """
        Publishes a new post to the specified publication.
        Args:
            title (str): The title of the post.
            content (str): The content of the post.
            tags_id (list): A list of tag IDs to associate with the post.
            tags_slug (list[dict]): a list of dictionaries containing tags slug and name.
                Example: [{'slug': 'tag1', 'name': 'Tag 1'}]
            subtitle (str, optional): The subtitle of the post. Defaults to None.
            image_url (str, optional): The URL of the image to use for the post. Defaults to None.
            slug (str, optional): The slug of the post. Defaults to None.
            origin_url (str, optional): The original URL of the post. Defaults to None.
            disable_comments (bool, optional): Whether to disable comments on the post. Defaults to False.
            publish_as (str, optional): The type of post to publish. Defaults to None.
            series_id (str, optional): The ID of the series to which the post belongs. Defaults to None.
            scheduled (bool, optional): Whether the post is scheduled. Defaults to False.
            enable_table (bool, optional): Whether to enable table of content mode. Defaults to False.
            co_authors (list, optional): A list of coauthor ids. Defaults to None.
        """
        tags = None

        if not tags_id and not tags_slug:
            raise ValueError('Either tags_id or tags_slug must be provided.')

        if tags_id:
            tags = [{'id': tag_id} for tag_id in tags_id]
        elif tags_slug:
            tags = tags_slug
        query = publish_post
        variables = {
            'title': title,
            'content': content,
            'tags': tags,
            'subtitle': subtitle,
            'publicationId': self.id,
            'imageUrl': image_url,
            'slug': slug,
            'originUrl': origin_url,
            'disableComments': disable_comments,
            'publishAs': publish_as,
            'seriesId': series_id,
            'settings': {
                'scheduled': scheduled,
                'enableTableOfContent': enable_table
            },
            'coAuthors': co_authors
        }

        data = self.client.fetch_data(query=query, variables=variables)
        return f'Successfully published with id: "{data["publishPost"]["post"]["id"]}"'

    def update_post(self, post_id: str, title: str = None, subtitle: str = None, content: str = None,
                    published_at: datetime = None, tags_id: list = None, tags_slug: list[dict] = None,
                    image_url: str = None, slug: str = None, origin_url: str = None, publication_id: str = None,
                    disable_comments: bool = False, publish_as: str = None, series_id: str = None,
                    enable_table: bool = False, co_authors: list = None):
        """
        Publishes a new post to the specified publication.
        Args:
            post_id (str): The ID of the post to update.
            title (str): The title of the post.
            content (str): The content of the post.
            published_at (datetime): The date and time when the post was published. Defaults to None.
            tags_id (list): A list of tag IDs to associate with the post.
            tags_slug (list[dict]): a list of dictionaries containing tags slug and name.
                Example: [{'slug': 'tag1', 'name': 'Tag 1'}]
            subtitle (str, optional): The subtitle of the post. Defaults to None.
            image_url (str, optional): The URL of the image to use for the post. Defaults to None.
            slug (str, optional): The slug of the post. Defaults to None.
            origin_url (str, optional): The original URL of the post. Defaults to None.
            disable_comments (bool, optional): Whether to disable comments on the post. Defaults to False.
            publish_as (str, optional): The type of post to publish. Defaults to None.
            series_id (str, optional): The ID of the series to which the post belongs. Defaults to None.
            enable_table (bool, optional): Whether to enable table of content mode. Defaults to False.
            co_authors (list, optional): A list of coauthor ids. Defaults to None.
            publication_id (str, optional): Whether the publication should be changed. Defaults to None.
        """
        tags = None
        if tags_id:
            tags = [{'id': tag_id} for tag_id in tags_id]
        elif tags_slug:
            tags = tags_slug

        if not content:
            post = self.client.get_post(post_id)
            content = post.content

        if not publication_id:
            publication_id = self.id

        query = update_post
        variables = {
            'postId': post_id,
            'title': title,
            'subtitle': subtitle,
            'publishedAt': published_at,
            'content': content,
            'imageUrl': image_url,
            'slug': slug,
            'originUrl': origin_url,
            'tags': tags,
            'publishAs': publish_as,
            'seriesId': series_id,
            'settings': {
                'disableComments': disable_comments,
                'isTableOfContentEnabled': enable_table
            },
            'coAuthors': co_authors,
            'publicationId': publication_id
        }

        data = self.client.fetch_data(query=query, variables=variables)
        return f'Successfully Updated with id: "{data["updatePost"]["post"]["id"]}"'

    def remove_post(self, post_id: str) -> str:
        """
        Removes a post from the specified publication.
        Args:
            post_id (str): The ID of the post to remove.
        """
        query = remove_post
        variables = {
            'postId': post_id
        }
        self.client.fetch_data(query=query, variables=variables)
        return f'Successfully removed"'

    def get_drafts(self, limit: int = 10) -> list:
        """
        Fetches comments for a post.
        Args:
            limit (int): The maximum number of drafts to fetch. Default to 10.
        Returns:
            list: A list of Draft objects.
        """
        query = drafts
        variables = {'id': self.id, 'first': limit}
        data = self.client.fetch_data(query=query, variables=variables)
        edges = data['publication']['drafts']['edges']
        nodes = [Draft(i['node'], self.client) for i in edges]
        result = [node for node in nodes]
        return result

    def publish_draft(self, draft_id: str) -> str:
        """
        Publishes a draft.
        Args:
            draft_id (str): The ID of the draft to publish.
        """
        query = publish_draft
        variables = {'draftId': draft_id}
        data = self.client.fetch_data(query=query, variables=variables)
        return f'Successfully published with id: "{data["publishDraft"]["post"]["id"]}"'

    def create_webhook(self, url: str, events: list[str], secret: str) -> Webhook:
        """
        Creates a webhook for the publication.
        Args:
            url (str): The URL of the webhook.
            events (list): The webhook will be triggered if any of the selected events occur.
                post_published, post_updated, post_deleted, static_page_published,
                static_page_edited, static_page_deleted.
            secret (str): The secret to use for the webhook.
        """
        for i in events:
            events.append(i.upper())
        query = create_webhook
        variables = {'publicationId': self.id, 'url': url, 'events': events, 'secret': secret}
        data = self.client.fetch_data(query=query, variables=variables)
        return Webhook(data, self.client)