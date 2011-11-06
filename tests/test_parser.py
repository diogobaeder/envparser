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

        name = parser.get('name')

        self.assertEqual(name, 'John Doe')

    @istest
    def gets_string_from_configuration_default_if_section_and_file_dont_exist(self):
        parser = Parser(self.basefile, 'weirdsection')

        name = parser.get('name')

        self.assertEqual(name, 'John Doe')

    @istest
    def gets_string_from_another_environment_if_section_exists(self):
        parser = Parser(self.basefile, 'dev')

        name = parser.get('name')

        self.assertEqual(name, 'John Doe Dev')

    @istest
    def gets_string_from_another_environment_if_file_exists(self):
        parser = Parser(self.basefile, 'live')

        name = parser.get('name')

        self.assertEqual(name, 'John Doe Live')

    @istest
    def gets_string_from_another_environment_if_file_and_section_exists(self):
        parser = Parser(self.basefile, 'tests')

        name = parser.get('name')

        self.assertEqual(name, 'John Doe Tests')

    @istest
    def gets_integer_from_configuration(self):
        parser = Parser(self.basefile)

        age = parser.getint('age')

        self.assertEqual(age, 30)

    @istest
    def gets_integer_from_configuration_default_if_doesnt_exist_in_section(self):
        parser = Parser(self.basefile, 'dev')

        age = parser.getint('age')

        self.assertEqual(age, 30)

    @istest
    def gets_integer_from_configuration_default_if_section_and_file_dont_exist(self):
        parser = Parser(self.basefile, 'weirdsection')

        name = parser.getint('age')

        self.assertEqual(name, 30)

    @istest
    def gets_float_from_configuration(self):
        parser = Parser(self.basefile)

        salary = parser.getfloat('salary')

        self.assertEqual(salary, 560.00)

    @istest
    def gets_string_from_another_environment_using_same_extension_as_base_file(self):
        parser = Parser(os.path.abspath(os.path.join(os.path.dirname(__file__), 'fixtures', 'base.ini')), 'live')

        name = parser.get('name')

        self.assertEqual(name, 'John Doe Live INI')