import unittest
from hashnode_py.client import HashnodeClient


class HashnodeClientTest(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment by initializing the HashnodeClient with a specific token.
        """
        self.client = HashnodeClient(token="<YOUR_TOKEN_HERE>")

    def test_get_user(self):
        user = self.client.get_user("talaat049")
        self.assertEqual(user.username, "talaat049")

    def test_get_publication(self):
        pub = self.client.get_publication("talaat.hashnode.dev")
        self.assertEqual(pub.url, "https://talaat.hashnode.dev")

    def test_get_feed(self):
        feed = self.client.get_feed(20)
        self.assertIsNotNone(feed)

    def test_fetch_data(self):
        query = """
            query getUser($username: String!) {
                user(username: $username) {
                    username
                }
            }
        """
        variables = {'username': 'talaat049'}
        data = self.client.fetch_data(query=query, variables=variables)
        self.assertEqual(data['user']['username'], 'talaat049')


if __name__ == '__main__':
    unittest.main()
