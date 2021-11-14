# pseudo codeimport sys
from flask import render_template, redirect, url_for, request, abort

from flask_sqlalchemy import SQLAlchemy
from models.alarm import Alarm

db = SQLAlchemy()

def index():
    return 'lolz'

# def store():
#     return ''

def show(alarmId):
    Alarm.query.filter_by(id=alarmId).first()
    return f"id: {alarmId}\n{request}"

# def update(alarmId):
#     return ''

# def delete(alarmId):
#     return ''