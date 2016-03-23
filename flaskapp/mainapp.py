from flask import Flask, render_template
import yaml

import orcid

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
                           profile_data={
                           "user": cfg['user'],
                           "name": name,
                           "affiliation": affiliation,
                           "gravatarhash": gravatarhash},
                           articles=articles)

@app.route('/<orcid_id>')
def storify(orcid_id):
    orcid_json = orcid.get_json(orcid_id)
    return render_template('sample.html',
                           profile_data=orcid_json,
                           articles={})

if __name__ == '__main__':
    app.run(debug=True)
