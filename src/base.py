# -*- coding:utf-8 -*-
"""
# Author:aluka_han
# Email:aluka_han@163.com
# Datetime:2019/8/30
# Reference: None
# Description:
"""

# Standard library
import os
# Third-party libraries
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder='../templates')


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)
        upload_path = os.path.join(basepath, './', secure_filename(f.filename))
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9991, debug=True)
