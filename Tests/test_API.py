import unittest
from functions import user_account


class Test(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(user_account.hello(), "Hello Simplon !")
    
