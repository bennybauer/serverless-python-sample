import unittest
import json
from handler import list_posts, get_post


class TestHandler(unittest.TestCase):
    """ Tests handler methods """

    def test_list_posts(self):
        """ Tests list_posts """
        res = list_posts(None, None)
        self.assertEquals(200, res['statusCode'])
        self.assertTrue(len(res['body']) > 0)

    def test_get_post(self):
        """ Tests get_post """
        event = {}
        event['pathParameters'] = {}
        event['pathParameters']['id'] = "1"
        res = get_post(event, None)

        self.assertEquals(200, res['statusCode'])

        post = json.loads(res['body'])
        self.assertEquals(1, post['id'])
        self.assertEquals("sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
         post['title'])

if __name__ == '__main__':
    unittest.main()
