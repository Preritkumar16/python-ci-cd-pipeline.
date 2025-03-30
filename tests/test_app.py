import sys
import os
import unittest

# Add the project directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import some_function

class TestApp(unittest.TestCase):
    def test_some_function(self):
        self.assertEqual(some_function(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
