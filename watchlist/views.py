# -*- coding: utf-8 -*-
from flask import render_template
from watchlist.index import InfoForm
from watchlist.query import start
from watchlist import app


@app.route('/', methods=['GET', 'POST'])
def index():
    form = InfoForm()
    if form.validate_on_submit():
        info = start(form.fileopen.data.filename, form.term.data, form.filestore.data.filename)
        print(form.term.data)
        return render_template('query.html', form=form, flag=1, info=info)
    return render_template('query.html', form=form, flag=0)
