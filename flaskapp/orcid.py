"""
API wrapper to Orcid.
"""
import requests
import json
import logging
import hashlib

logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://pub.orcid.org/"

def _get_raw_json(orcid_id, action=""):
    """Get raw JSON file for orcid_id."""
    url = orcid_url(orcid_id, action)
    logging.info(url)
    resp = requests.get(url,
                        headers={'Accept':'application/orcid+json'})

    return resp.json()


def orcid_url(orcid_id, action=""):
    return BASE_URL + orcid_id + "/" + action


def get_profile(orcid_id):
    """Get JSON for Orcid and clean it."""
    raw_json = _get_raw_json(orcid_id)

    # TODO Add information
    profile = {}
    profile['given_name'] = raw_json.get("orcid-profile").get("orcid-bio").get("personal-details").get("given-names").get("value")
    profile['family_name'] = raw_json.get("orcid-profile").get("orcid-bio").get("personal-details").get("family-name").get("value")
    profile['email'] = raw_json.get("orcid-profile").get("orcid-bio").get("contact-details").get("email")[0].get("value").lower().strip()
    profile['affiliation'] = get_current_affiliation(orcid_id)
    profile['bio'] = raw_json.get('orcid-profile').get('orcid-bio').get('biography').get('value')
    profile['gravatarhash'] = hashlib.md5(profile['email'].encode('utf-8')).hexdigest()

    return profile


def get_works(orcid_id):
    """ Return dictionary containing work of person with ORCID id. Dict indexed by DOI of works """
    raw_json = _get_raw_json(orcid_id, "/orcid-works")
    works = raw_json['orcid-profile']['orcid-activities']['orcid-works']['orcid-work']
    d = {}
    for item in works:
        doi, tmp_d = work_item(item)
        d[doi] = tmp_d
    return d

def get_current_affiliation(orcid_id):
    #raw_json = _get_raw_json(orcid_id, "orcid-employment")
    string = "I am from the university of life mate"
    return string
    
def work_item(item):
    dobj={}
    if item['work-external-identifiers']:
        doi = item['work-external-identifiers']['work-external-identifier'][0]['work-external-identifier-id']['value']
        dobj['cite'] = item['work-citation']
        dobj['url'] = item['url']
        return doi, dobj,
    else:
        return None, None
