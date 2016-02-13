from flask import Flask

app = Flask('webadmin')
from app import views
from app import container
