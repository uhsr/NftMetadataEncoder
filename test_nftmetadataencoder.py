# test_nftmetadataencoder.py
"""
Tests for NftMetadataEncoder module.
"""

import unittest
from nftmetadataencoder import NftMetadataEncoder

class TestNftMetadataEncoder(unittest.TestCase):
    """Test cases for NftMetadataEncoder class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataEncoder()
        self.assertIsInstance(instance, NftMetadataEncoder)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataEncoder()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
