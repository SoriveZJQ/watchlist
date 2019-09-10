# -*- coding: utf-8 -*-
from flask import render_template, request
from watchlist.index import InfoForm
#from werkzeug.utils import secure_filename
from watchlist.query import start
from watchlist import app
import os


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        info = start(os.path.dirname(os.path.abspath(form.fileopen.data.filename))+'/'+form.fileopen.data.filename,
                     form.term.data, os.path.dirname(os.path.abspath(form.filestore.data.filename))+'/'+form.filestore.data.filename)
        #print(os.path.dirname(__file__))
        return render_template('query.html', form=form, flag=1, info=info)

    #if request.method == 'POST':
    #    f = request.files['file']
    #    basepath = os.path.dirname(__file__)
    #    upload_path = os.path.join(basepath, 'static/uploads', secure_filename(f.filename))
    #    f.save(upload_path)
    #
    #    return render_template()


    return render_template('query.html', form=form, flag=0)
