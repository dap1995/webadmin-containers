from flask import render_template
from app import app
import platform
from app.models.server import Server

@app.route('/')
def index():
    servers = []
    containers = {}
    servers.append(Server(platform.node(), 'unix://var/run/docker.sock', platform.release()))
    return render_template("index.html", servers=servers)
