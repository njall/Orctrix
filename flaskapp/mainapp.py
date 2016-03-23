from flask import Flask, render_template, send_from_directory
import yaml
import os
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
                           "user": cfg['user']['0000-0002-2907-3313'],
                           "name": name,
                           "affiliation": affiliation,
                           "gravatarhash": gravatarhash},
                           articles=articles)

@app.route('/<orcid_id>')
def storify(orcid_id):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    orcid_json = orcid.get_profile(orcid_id)
    works = orcid.get_works(orcid_id)
    print(works)
    profile_data = update_userinfo(orcid_id, orcid_json, cfg)

    return render_template('sample.html',
                           profile_data=profile_data,
                           articles=works)


def update_userinfo(orcid_id, orcid_json, cfg):
    try:
        localuserinformation = cfg['user'][orcid_id]
    except KeyError:
        localuserinformation = {}
    profile_data = orcid_json
    if localuserinformation:
        profile_data['affiliation'] = localuserinformation['affiliation']
        profile_data['gravatarhash'] = localuserinformation['gravatarhash']
    return profile_data


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
