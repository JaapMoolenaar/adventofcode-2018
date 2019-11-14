import redis
from flask import Flask

from os import path
from werkzeug.utils import secure_filename

# Create cache
cache = redis.Redis(host='redis', port=6379)

# Generic file saver
def save_file(input):
    if input.filename == "":
        return False

    filename = secure_filename(input.filename)
    filepath = path.join(app.config["STORAGE_PATH"], filename)

    input.save(filepath)

    return filepath

app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("app.config.ProductionConfig")
else:
    app.config.from_object("app.config.DevelopmentConfig")


from . import main
from . import test

from app.puzzles import *