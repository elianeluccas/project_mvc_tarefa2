# app/controllers/static_controller.py
from flask import render_template

class StaticController:
    @staticmethod
    def index():
        return render_template("index.html")
