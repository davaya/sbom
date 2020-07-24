import json
import jsonschema
import os
import re
from urllib.request import urlopen, Request

show_descriptions = True        # If False, don't include 'name' as the description of 'licenseId'
repo = 'https://github.com/spdx/license-list-data/tree/master/json'
files = ['licenses.json', 'exceptions.json']
outfile = 'spdx-license-enums'


"""
Fetch current SPDX license list from repo
"""

def github_contents(web_url):
    """
    Convert a GitHub repo web page URL to the corresponding API directory URL
    :param web_url: https://github.com/spdx/license-list-data/tree/master/json
    :return: dir_url: https://api.github.com/repos/spdx/license-list-data/contents/json
    """
    m = re.match(r'^(https://)(github.com/)(.*?)/tree/master/(.*)$', web_url)
    if m:
        return m.group(1) + 'api.' + m.group(2) + 'repos/' + m.group(3) + '/contents/' + m.group(4)


data = {}
auth = {'Authorization': 'token ' + os.environ['GitHubToken']}
with urlopen(Request(github_contents(repo), headers=auth)) as d:
    dir = json.loads(d.read().decode())
    for n, f in enumerate(dir):
        if f['name'] in files:
            with urlopen(Request(f['download_url'], headers=auth)) as file:
                data[os.path.splitext(f['name'])[0]] = json.loads(file.read().decode())


"""
Validate license list files
"""

llversion = data['licenses']['licenseListVersion']
print(f'License List Version {llversion}, {data["licenses"]["releaseDate"]}')
assert llversion == data['exceptions']['licenseListVersion']

with open('license_list_source.json') as f:
    jschema = json.load(f)
    jsonschema.Draft7Validator(jschema).validate({'licenselist': data['licenses']})
    jsonschema.Draft7Validator(jschema).validate({'exceptionlist': data['exceptions']})


"""
Generate license and exception enumerations
"""

def item(license, le, desc=True):
    id = {'l': 'licenseId', 'e': 'licenseExceptionId'}
    return [int(license['referenceNumber']), license[id[le]], license['name'].strip() if desc else '']

license_items = [item(k, 'l', show_descriptions) for k in data['licenses']['licenses']]
exception_items = [item(k, 'e', show_descriptions) for k in data['exceptions']['exceptions']]
le_schema = {
    'meta': {
        'module': 'http://spdx.org/license-list/v3.0',
        'patch': llversion,
        'description': f'SPDX License List Enumerations, Version {llversion}, Released {data["licenses"]["releaseDate"]}',
        'exports': ["LicenseList", "ExceptionList"],
        'config': {'$MaxElements': 1000}        # Default is 100, 2020-07-21 license list has 441
    },
    'types': [
        ['LicenseList', 'Enumerated', [], '', license_items],
        ['ExceptionList', 'Enumerated', [], '', exception_items]
    ]
}

print(f'{len(license_items)} licenses, {len(exception_items)} exceptions')
fname = os.path.join('data', outfile + '-' + llversion + '.jadn')
with open(fname, 'w') as f:
    json.dump(le_schema, f)