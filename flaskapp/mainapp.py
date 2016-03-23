from flask import Flask, render_template
import yaml

import orcid

app = Flask(__name__)


@app.route('/')
def index():
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    name = cfg['user']['0000-0002-2907-3313']['name']
    affiliation = cfg['user']['0000-0002-2907-3313']['affiliation']
    gravatarhash = cfg['user']['0000-0002-2907-3313']['gravatarhash']
    articles = cfg['articles']
    for article in articles:
        if 'doi' in articles[article].keys():
            articles[article]['doiurl'] = "http://dx.doi.org/" + \
                articles[article]['doi']
        else:
            articles[article]['doiurl'] = None
    return render_template('sample.html',
                           profile_data={
                           "user": cfg['user'],
                           "name": name,
                           "affiliation": affiliation,
                           "gravatarhash": gravatarhash},
                           articles=articles)

@app.route('/<orcid_id>')
def storify(orcid_id):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    orcid_json = orcid.get_json(orcid_id)
    try:
        localuserinformation = cfg['user'][orcid_id]
    except KeyError:
        localuserinformation = {}
    profile_data = orcid_json
    if localuserinformation:
        profile_data['affiliation'] = localuserinformation['affiliation']
        profile_data['gravatarhash'] = localuserinformation['gravatarhash']
    return render_template('sample.html',
                           profile_data=profile_data,
                           articles={})

if __name__ == '__main__':
    app.run(debug=True)
