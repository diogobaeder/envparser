#
from ConfigParser import RawConfigParser


class Parser(object):
    def __init__(self, basefile):
        self.__parser = RawConfigParser()
        self.__parser.read(basefile)

    def get(self, section, option):
        return self.__parser.get(section, option)