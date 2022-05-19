import os
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
dir_path = 'static'
for filename in os.listdir(dir_path):
    print(filename)
    path = os.path.join(dir_path, filename)
    print(path)
    if filename == 'operatinglow.jpg':
        os.remove(path)
    