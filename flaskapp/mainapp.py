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
    article = cfg['articles'][1]
    doiurl = "http://dx.doi.org/" + article['doi']
    title = article['title']
    summary = article['summary']
    return render_template('sample.html',
                           name=name,
                           affiliation=affiliation,
                           summary=summary,
                           doiurl=doiurl,
                           title=title,
                           gravatarhash=gravatarhash)

if __name__ == '__main__':
    app.run(debug=True)
