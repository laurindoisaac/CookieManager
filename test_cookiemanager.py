# test_cookiemanager.py
"""
Tests for CookieManager module.
"""

import unittest
from cookiemanager import CookieManager

class TestCookieManager(unittest.TestCase):
    """Test cases for CookieManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CookieManager()
        self.assertIsInstance(instance, CookieManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CookieManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
