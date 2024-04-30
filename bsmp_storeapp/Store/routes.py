from flask import Blueprint, render_template
from . import store

@store.route('/')
@store.route('/home')
def home():
    return render_template('home.html')
