from flask import Flask, render_template, send_from_directory
import os

template_dir = os.path.abspath('./AngularApp/dist')
static_dir = os.path.abspath('./AngularApp/dist')
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

@app.route('/dist/<path:path>')
def send_js(path):
    return send_from_directory('dist', path)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
	app.run()
