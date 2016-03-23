"""
API wrapper to Orcid.
"""
import hashlib
import logging
import re

import json
import requests

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
    return BASE_URL + orcid_id + action


def get_profile(orcid_id):
    """Get JSON for Orcid and clean it."""
    raw_json = _get_raw_json(orcid_id)

    # TODO Add information
    profile = {}
    for name in ('credit_name', 'given_names', 'family_name'):
        try:
            profile[name] = raw_json.get("orcid-profile").get("orcid-bio").get("personal-details").get(name.replace('_', '-')).get("value")
        except:
            profile[name] = None
    if profile['credit_name']:
        profile['name'] = profile['credit_name']
    else:
        profile['name'] = profile['given_names'] + ' ' + profile['family_name']
    try:
        profile['email'] = raw_json.get("orcid-profile").get("orcid-bio").get("contact-details").get("email")[0].get("value").lower().strip()
    except:
        profile['email'] = None
    profile['affiliation'] = get_current_affiliation(orcid_id)
    try:
        profile['bio'] = raw_json.get('orcid-profile').get('orcid-bio').get('biography').get('value')
    except:
        profile['bio'] = None
    if profile['email']:
        profile['gravatarhash'] = hashlib.md5(profile['email'].encode('utf-8')).hexdigest()
    else:
        profile['gravatarhash'] = None
    return profile


def get_works(orcid_id):
    """ Return dictionary containing work of person with ORCID id. Dict indexed by DOI of works """
    raw_json = _get_raw_json(orcid_id, "/orcid-works")
    try:
        works = raw_json['orcid-profile']['orcid-activities']['orcid-works']['orcid-work']
    except:
        works = None
    d = []
    # TODO Improve the box_type selection
    box_type = "full"
    if works:
        for item in works:
            if box_type == "full":
                box_type = "images"
            elif box_type == "images":
                box_type = "donut"
            else:
                box_type = "full"

            doi, tmp_d = work_item(item)
            if tmp_d:
                tmp_d["doi"] = doi
                tmp_d["image"] = None
                # XXX Need to parse some information
                if tmp_d.get("cite") and tmp_d.get("cite").get("work-citation-type") == "BIBTEX":
                    m = re.search('title\s?=\s?{(.+)}', tmp_d.get("cite").get("citation"))
                    tmp_d["title"] = m.group(1)
                else:
                    continue

                tmp_d["box_type"] = box_type
                print(tmp_d)

                d.append(tmp_d)
    return d

def get_current_affiliation(orcid_id):
    #raw_json = _get_raw_json(orcid_id, "orcid-employment")
    string = "I am from the university of life mate"
    return string
    
def work_item(item):
    dobj={}
    if item['work-external-identifiers'] and item['work-citation']:
        doi = item['work-external-identifiers']['work-external-identifier'][0]['work-external-identifier-id']['value']
        dobj['cite'] = item['work-citation']
        if item['url']:
            dobj['url'] = item['url'].get("value")
        else:
            dobj['url'] = "Not available"
        dobj['title'] = item['work-title']['title']['value']
        dobj['subtitle'] = item.get('work-title').get("subtitle")
        dobj['description'] = item.get('short-description')
        #dobj['type'] = item['type']
        return doi, dobj,
    else:
        return None, None
