from flask import Flask
from flask import render_template

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

