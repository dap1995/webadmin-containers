from flask import render_template
from app import app
from docker import Client
import platform
from app.container import Container

@app.route('/')
def index():
    osversion = platform.release()
    hostname = platform.node()
    distribution = platform.linux_distribution()
    containers = listContainers()
    return render_template("index.html", osversion=osversion, containers=containers, hostname=hostname, distribution=distribution)

def listContainers():
        containers = []
        cli = Client(base_url='unix://var/run/docker.sock',version='auto')
        for container in cli.containers(all=True):
            container = Container(container.get("Names"), container.get("Status"))
            containers.append(container)
        return containers
