from flask import Flask

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000

@application.route('/', methods=['GET'])
def landing():
    return "Linkchecker!"
