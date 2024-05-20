import unittest
import os

class TestFileContextManager(unittest.TestCase):
    def test_file_creation(self):
        with FileContextManager("test.txt", "w") as f:
            f.write("Test file creation")
        self.assertTrue(os.path.exists("test.txt"))

    def test_file_content(self):
        with FileContextManager("test.txt", "r") as f:
            content = f.read()
        self.assertEqual(content, "Test file creation")

    def test_exception_handling(self):
        with self.assertRaises(Exception):
            with FileContextManager("test.txt", "r") as f:
                raise Exception("Test exception")

if __name__ == "__main__":
    unittest.main()
