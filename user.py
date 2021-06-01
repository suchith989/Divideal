
class User:

    __id = None
    __name = None
    __email = None

    def __init__(self, idx, name, email):
        self.__id = idx
        self.__name = name
        self.__email = email


    def setId(self, idx):
        self.__id = idx

    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

