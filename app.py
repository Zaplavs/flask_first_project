from flask import Flask, request, render_template, send_from_directory
import logging
from main.main import main_blueprint
from search.search import search_blueprint
from loader.loader import loader_blueprint

# POST_PATH = "posts.json"
# UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

logging.basicConfig(filename="basic.log", encoding="UTF-8")

app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(loader_blueprint)


app.run()

