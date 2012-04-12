import unittest
import envoy

from csvfilter import VERSION


class HelpOutputTests(unittest.TestCase):

    def setUp(self):
        self.r = envoy.run('csvfilter -h')

    def test_help_output(self):
        self.assertEqual(0, self.r.status_code)

    def test_version_is_present(self):
        self.assertTrue(VERSION in self.r.std_out)
