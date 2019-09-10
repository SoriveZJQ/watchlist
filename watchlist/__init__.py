# -*- coding: utf-8 -*-
import os
from datetime import timedelta
from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = timedelta(seconds=0.1)


from watchlist import views



