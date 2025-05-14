from flask import Flask
from flask import Blueprint

polaroid = Blueprint('polaroid', __name__)

@polaroid.route('/polaroid/en')
def Polaroid():
    return "<p>Polaroid</p>"

