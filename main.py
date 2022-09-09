# -*- coding: utf-8 -*-
import os

from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

from flask import Flask, render_template

load_dotenv()

app = Flask(__name__)

username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_USER_PWD")
host = os.environ.get("DB_HOST")
port = os.environ.get("DB_PORT")
database_name = os.environ.get("DB_NAME")

app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql://{username}:{password}@{host}:{port}/{database_name}"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now()
    )

    title = db.Column(db.String(100), unique=True, nullable=False)
    img = db.Column(db.LargeBinary(), nullable=True)

    tag = db.Column(db.String(50))

    btn1_url = db.Column(db.String(100))
    btn1_name = db.Column(db.String(100))

    btn2_url = db.Column(db.String(100))
    btn2_name = db.Column(db.String(100))

    def __repr__(self):
        return f"<Article {self.title}>"


@app.route("/")
def index():
    result = [
        {
            "img": "et_puy_c_est_tout.png",
            "title": "Projet personnel",
            "tag": "Blog Personnel",
            "btn1_url": "https://www.et-puy-c-est-tout.fr",
            "btn1_name": "Lien",
            "btn2_url": "https://github.com/CamClrt/et-Puy-c-est-tout",
            "btn2_name": "Sources et hébergement",
        },
        {
            "img": "et_puy_c_est_tout.png",
            "title": "Projet personnel",
            "tag": "Blog Personnel",
            "btn1_url": "https://www.et-puy-c-est-tout.fr",
            "btn1_name": "Lien",
            "btn2_url": "https://github.com/CamClrt/et-Puy-c-est-tout",
            "btn2_name": "Sources et hébergement",
        },
        {
            "img": "et_puy_c_est_tout.png",
            "title": "Projet personnel",
            "tag": "Blog Personnel",
            "btn1_url": "https://www.et-puy-c-est-tout.fr",
            "btn1_name": "Lien",
            "btn2_url": "https://github.com/CamClrt/et-Puy-c-est-tout",
            "btn2_name": "Sources et hébergement",
        },
    ]

    return render_template("index.html", result=result)
