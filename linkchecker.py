from flask import Flask
from flask import render_template
import storytracker

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000

@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@application.route('/result/', methods=['POST', 'GET'])
def result():
	u = request.form['url']
	url = storytracker.archive(u)
	links = [h for h in url.hyperlinks if 'wikipedia' in h.href]
	return render_template('results.html', links=links, num_links = len(links), url=u)