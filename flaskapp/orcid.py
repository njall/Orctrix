"""
API wrapper to Orcid.
"""
import requests
import json

import logging
logging.basicConfig(level=logging.DEBUG)

BASE_URL = "https://pub.orcid.org/"

def _get_raw_json(orcid_id):
    """Get raw JSON file for orcid_id."""
    url = BASE_URL + orcid_id
    logging.info(url)
    resp = requests.get(url,
                        headers={'Accept':'application/orcid+json'})

    return resp.json()

def get_json(orcid_id):
    """Get JSON for Orcid and clean it."""
    raw_json = _get_raw_json(orcid_id)

    # TODO Add information
    json = {
            "name": raw_json["orcid-profile"]["orcid-bio"]["personal-details"]["credit-name"]["value"],
            "affiliation": None,
            "summary": None,
            "doiurl": None,
            "title": None,
            "gravatarhash": None,
            }

    return json
