from flask import Flask, send_from_directory, render_template
import os
from FileWrapper import FileWrapper

app = Flask(__name__)

targetFolder = '/Users/GongLi/Downloads'


@app.route('/hello')
def hello_world():
    return 'Hello Wolrd'

@app.route('/list')
def list():

    allFiles = os.listdir( targetFolder )
    allFileWrapper = [FileWrapper(address, '/download/' + address) for address in allFiles]

    return render_template('hello.html', files=allFileWrapper)


@app.route('/download/<path:filename>')
def download_file(filename):
    return send_from_directory(targetFolder, filename, as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)
