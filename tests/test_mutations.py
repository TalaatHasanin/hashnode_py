import unittest
from hashnode_py.client import HashnodeClient


class MutationsTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by initializing the HashnodeClient with a specific token.
        """
        self.client = HashnodeClient(token="<YOUR_TOKEN_HERE>")

    def test_publish_post(self):
        """
        Test the publish_post mutation
        """
        publication = self.client.get_publication("talaat.hashnode.dev")
        post = publication.publish_post(
            title="this is test title",
            content="this is a test content",
            tags_slug=[{"slug": "test", "name": "Test"}]
        )
        self.assertIsNotNone(post)

    def test_publish_draft(self):
        """
        Test the publish_draft mutation
        """
        publication = self.client.get_publication("talaat.hashnode.dev")
        draft = publication.get_drafts()[0]
        post = publication.publish_draft(draft_id=draft.id)
        self.assertIsNotNone(post)


if __name__ == '__main__':
    unittest.main()
