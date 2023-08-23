# -*- encoding: utf-8 -*-
import os

# import Flask 
from flask import Flask, render_template, request, redirect, g, url_for
from .config import Config
from app.spam import runSpam

# Inject Flask magic
app = Flask(__name__)

# load Configuration
app.config.from_object( Config )

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        phone = request.form.get('phone')
        runSpam(phone)
 
    return render_template('pages/sp.html')

@app.route('/rest', methods=['GET'])
def spamS():
    if request.args.get("phone"):
        phone = request.args["phone"]
        runSpam(phone)
    return f'Spam phone: {phone}'
