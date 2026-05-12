# test_linkchain.py
"""
Tests for LinkChain module.
"""

import unittest
from linkchain import LinkChain

class TestLinkChain(unittest.TestCase):
    """Test cases for LinkChain class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = LinkChain()
        self.assertIsInstance(instance, LinkChain)
        
    def test_run_method(self):
        """Test the run method."""
        instance = LinkChain()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
