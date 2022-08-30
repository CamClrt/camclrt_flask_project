# -*- coding: utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    res = {
        "img": "et_puy_c_est_tout.png",
        "title": "Projet personnel",
        "tag": "Blog Personnel",
        "btn1_url": "https://www.et-puy-c-est-tout.fr",
        "btn1_name": "Lien",
        "btn2_url": "https://github.com/CamClrt/et-Puy-c-est-tout",
        "btn2_name": "Sources et hébergement",
    }
    return render_template("index.html", res=res)
