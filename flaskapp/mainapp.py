from flask import Flask, render_template, send_from_directory, redirect, url_for
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Required
import yaml
import os
import orcid
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'

class ORCIDForm(Form):
    orcid = StringField('Enter ORCID?', validators=[Required()])
    submit = SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    myorcid = None
    form = ORCIDForm()
    if form.validate_on_submit():
        myorcid = form.orcid.data
        form.orcid.orcid = ''
        return redirect(myorcid)
    return render_template('new.html', form=form, myorcid=myorcid)

@app.route('/<orcid_id>')
def storify(orcid_id):
    if len(orcid_id) is not 19:
      return render_template('feedback.html',
                               feedback={
                               "title": "Sorry page can't be created:",
                               "details": 'ORCID provided is not correct length'}) 

    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.load(ymlfile)
    orcid_json = orcid.get_profile(orcid_id)
    works = orcid.get_works(orcid_id)
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
