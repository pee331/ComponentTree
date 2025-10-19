# test_componenttree.py
"""
Tests for ComponentTree module.
"""

import unittest
from componenttree import ComponentTree

class TestComponentTree(unittest.TestCase):
    """Test cases for ComponentTree class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ComponentTree()
        self.assertIsInstance(instance, ComponentTree)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ComponentTree()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
