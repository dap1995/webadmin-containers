from docker import Client
from app.models.container import Container
class Server(object):
    def __init__(self, hostname, docker_url, versao):
        self.__hostname = hostname
        self.__docker_url = docker_url
        self.__versao = versao

    def get_hostname(self):
        return self.__hostname

    def get_docker_url(self):
        return self.__docker_url

    def get_versao(self):
        return self.__versao

    def set_hostname(self):
        self.__hostname = hostname

    def set_docker_url(self):
        self.__docker_url = docker_url

    def set_versao(self):
        self.__versao = versao

    def listContainers(self):
        containers = []
        cli = Client(self.__docker_url,version='auto')
        for container in cli.containers(all=True):
            container = Container(container.get("Names"), container.get("Status"))
            containers.append(container)
        return containers

