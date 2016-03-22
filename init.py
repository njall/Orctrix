url = "https://pub.orcid.org/0000-0002-2907-3313"

import requests
import json

resp = requests.get(url,
                    headers={'Accept':'application/orcid+json'})

print json.dumps(resp.json(),
                 sort_keys=True,
                 indent=4, separators=(',', ': '))


