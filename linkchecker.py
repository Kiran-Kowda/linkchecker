from flask import Flask, render_template, request
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
    links = [h for h in url.hyperlinks if request.form['link_type'] in h.href]
    return render_template('results.html', links=links, num_links = len(links), url=u, link_type=request.form['link_type'])


if __name__ == "__main__":
    application.run()
