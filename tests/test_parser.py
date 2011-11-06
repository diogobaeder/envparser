import os
from unittest import TestCase

from nose.tools import istest

from envparser import Parser


class ParserTest(TestCase):
    def setUp(self):
        self.basefile = os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures', 'base.cfg'))

    @istest
    def gets_string_from_configuration(self):
        parser = Parser(self.basefile)

        name = parser.get('section1', 'name')

        self.assertEqual(name, 'John Doe')