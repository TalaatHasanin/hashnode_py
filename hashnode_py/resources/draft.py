from hashnode_py.queries.mutations import (
    cancel_schedule, reschedule_draft, schedule_draft)
from hashnode_py.resources.scheduled_post import ScheduledPost


class Draft:
    def __init__(self, data: dict, client):
        """
        Initialize the Draft object with the given data and client.
        Args:
            data (dict): The dictionary containing draft data.
            client: The client object for interacting with the draft.
        """
        super(Draft, self).__init__()
        self.client = client
        self.data = data
        self.id = data['id']
        self.slug = data['slug']
        self.title = data['title']
        self.subtitle = data['subtitle']
        self.author = data['author']['username']
        self.cover_image = data['coverImage']['url'] if data['coverImage'] else None
        self.read_time = data['readTimeInMinutes']
        self.content = data['content']['text'] if data['content'] else None
        self.updated_at = data['updatedAt']
        self.last_backup_status = data['lastBackup']['status'] if data['lastBackup'] else None
        self.last_backup_at = data['lastBackup']['at'] if data['lastBackup'] else None
        self.last_successful_backup = data['lastSuccessfulBackupAt']
        self.last_failed_backup = data['lastFailedBackupAt']

    def schedule(self, author_id: str, publish_at: str) -> ScheduledPost:
        """
        Schedules the draft for publication.
        Args:
            author_id (str): The author ID of the draft.
            publish_at (str): The date and time in ISO 8601 format at which the draft should be published.
                Example: "2022-01-01T00:00:00Z".
        Returns:
            ScheduledPost: A ScheduledPost object representing the scheduled post.
        """
        query = schedule_draft
        variables = {'authorId': author_id, 'publishAt': publish_at, 'draftId': self.id}
        data = self.client.fetch_data(query=query, variables=variables)
        return ScheduledPost(data, self.client)

    def reschedule(self, publish_at: str) -> ScheduledPost:
        """
        ReSchedules the draft for publication.
        Args:
            publish_at (str): The date and time in ISO 8601 format at which the draft should be published.
                Example: "2022-01-01T00:00:00Z".
        Returns:
            ScheduledPost: A ScheduledPost object representing the scheduled post.
        """
        query = reschedule_draft
        variables = {'publishAt': publish_at, 'draftId': self.id}
        data = self.client.fetch_data(query=query, variables=variables)
        return ScheduledPost(data, self.client)

    def cancel_schedule(self):
        """
        ReSchedules the draft for publication.
        Returns:
            str: A success message if the draft was successfully canceled.
        """
        query = cancel_schedule
        variables = {'draftId': self.id}
        self.client.fetch_data(query=query, variables=variables)
        return f'Successfully cancelled schedule'
