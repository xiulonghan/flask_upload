# -*- coding:utf-8 -*-
"""
# Author:aluka_han
# Email:aluka_han@163.com
# Datetime:2019/8/30
# Reference: https://dormousehole.readthedocs.io/en/latest/patterns/fileuploads.html
# Description:
"""

# Standard library
import os
# Third-party libraries
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, flash
from flask import send_from_directory


upload_folder = './'  # 上传文件需要保存的目录
allowed_extensions = ['jpg', 'pdf', 'txt', 'gif']  # 允许上传的文件格式
app = Flask(__name__, template_folder='../templates')
app.secret_key = "super secret key"
app.config['UPLOAD_FOLDER'] = upload_folder
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 上传文件的最大值


def allowed_file(filename):
    """
    上传文件的格式要求
    :param filename:文件名称
    :return:
    """
    return '.' in filename and \
            filename.rsplit('.')[1].lower() in allowed_extensions


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('Please Select File')
            return redirect(url_for('upload'))
        f = request.files['file']
        if not allowed_file(f.filename):
            flash('Please Select Correct File')
            return redirect(url_for('upload'))
        if f and allowed_file(f.filename):
            save_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename))
            f.save(save_path)
            return redirect(url_for('show_upload_file', filename=secure_filename(f.filename)))
    return render_template('upload.html')


@app.route('/<filename>')
def show_upload_file(filename):
    download_path = '../'
    return send_from_directory(download_path, filename)  # as_attachment=True可以实现下载


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9991, debug=True)
