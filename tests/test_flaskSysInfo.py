import unittest

import flaskSysInfo


class FlasksysinfoTestCase(unittest.TestCase):

    def setUp(self):
        self.app = flaskSysInfo.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('Welcome to Flask System Info', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
