#
import ConfigParser
import os


class Parser(object):
    def __init__(self, basefile, environment='DEFAULT'):
        self.__parser = ConfigParser.SafeConfigParser()
        if environment == 'DEFAULT':
            self.__parser.read(basefile)
        else:
            self.__parser.read([basefile, self.__environment_file_from(basefile, environment)])
        self.environment = environment

    def __environment_file_from(self, basefile, environment):
            extension = os.path.splitext(basefile)[1]
            directory = os.path.dirname(basefile)
            return os.path.join(directory, environment + extension)

    def __get_with_method(self, method, option):
        try:
            return method(self.environment, option)
        except ConfigParser.NoSectionError:
            return method('DEFAULT', option)


    def get(self, option):
        return self.__get_with_method(self.__parser.get, option)

    def getint(self, option):
        return self.__get_with_method(self.__parser.getint, option)

    def getfloat(self, option):
        return self.__get_with_method(self.__parser.getfloat, option)
