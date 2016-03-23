from flask import Flask, render_template
import yaml
app = Flask(__name__)


@app.route('/')
def index():
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    name = cfg['user']['name']
    affiliation = cfg['user']['affiliation']
    gravatarhash = cfg['user']['gravatarhash']
    articles = cfg['articles']
    for article in articles:
        articles[article]['doiurl'] = "http://dx.doi.org/" + \
            articles[article]['doi']
    return render_template('sample.html',
                           user=cfg['user'],
                           articles=articles)

if __name__ == '__main__':
    app.run(debug=True)
