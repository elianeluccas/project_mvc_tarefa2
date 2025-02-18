from flask import Blueprint, render_template

static_bp = Blueprint('static_pages', __name__)

@static_bp.route('/')
def index():
    return render_template('index/index.html')
