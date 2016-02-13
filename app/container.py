class Container(object):

        def __init__(self, name, status):
            self.__name = name
            self.__status = status

        def get_name(self):
            return self.__name

        def get_status(self):
            return self.__status

        def set_name(self, name):
            self.__name = name

        def set_status(self, status):
            self.__status = status

        def paused(self):
            status = ""
            paused = False
            for word in self.__status.split():
                if word == "(Paused)":
                    paused = True
                    break
            return paused
