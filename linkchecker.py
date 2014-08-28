from flask import Flask, render_template, request
import storytracker
import requests

application = Flask(__name__)
application.debug = True
application.config['PORT'] = 5000


@application.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@application.route('/result/', methods=['POST', 'GET'])
def result():
	if request.method == 'POST':
	    u = request.form['url']
	    link_type = request.form['link_type']
	    url = storytracker.archive(u)
	    links = [h for h in url.hyperlinks if link_type in h.href]
	else:
		u = request.args.get('url', '')
		link_type = request.args.get('link_type','')
		url = storytracker.archive(u)
		links = [h for h in url.hyperlinks if link_type in h.href]
	return render_template('results.html', links=links, num_links = len(links), url=u, link_type=link_type)


if __name__ == "__main__":
    application.run()
