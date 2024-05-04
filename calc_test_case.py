import unittest
from unittest.mock import patch
from social import Post

class TestPostMethods(unittest.TestCase):

    def test_get_text(self):
        post = Post("Hello, world!")
        self.assertEqual(post.get_text(), "Hello, world!")

    def test_get_likes(self):
        post = Post("Hello, world!")
        self.assertEqual(post.get_likes(), 0)

    @patch('builtins.input', side_effect=['5'])
    def test_like(self, mock_input):
        post = Post("Hello, world!")
        post.like()
        self.assertEqual(post.get_likes(), 5)

    def test_get_comments(self):
        post = Post("Hello, world!")
        self.assertEqual(post.get_comments(), [])

    def test_add_comment(self):
        post = Post("Hello, world!")
        post.add_comment("Nice post!")
        self.assertEqual(post.get_comments(), ["Nice post!"])

if __name__ == '__main__':
    unittest.main()

