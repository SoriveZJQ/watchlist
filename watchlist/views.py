# -*- coding: utf-8 -*-
from flask import render_template, request
from watchlist.index import InfoForm
from watchlist.query import start
from watchlist import app
import os
import time


UPLOAD_FOLDER='static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
basedir = os.path.abspath(os.path.dirname(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    file_dir = os.path.join(basedir, app.config['UPLOAD_FOLDER'])
    if request.method == 'POST' and form.validate_on_submit():
        f = request.files['fileopen']
        #fname = secure_filename(f.filename)
        fname = f.filename
        print(fname)
        ext = fname.rsplit('.')[1]
        unix_time = int(time.time())
        new_filename = str(unix_time)+'.'+ext
        last_filename = os.path.join(file_dir, new_filename)
        f.save(last_filename)



        info = start(last_filename, form.term.data, file_dir)

        return render_template("query.html", form=form, flag=1, info=info)


    return render_template('query.html', form=form, flag=0)

