import json

"""
Convert SPDX licenses and exceptions files from JSON format into JADN schema modules
https://github.com/spdx/license-list-data/tree/master/json

The Licenses and Exceptions definitions should go in a single JADN module,
but since SPDX uses separate files, translator follows that convention.
"""

tt = {      # type table: mt = part of JADN module unique name, id = property name defined by SPDX for each type.
    'licenses':   {'mt': 'll', 'id': 'licenseId'},
    'exceptions': {'mt': 'le', 'id': 'licenseExceptionId'}
}

for file in ['license-list-3.8-22', 'license-exceptions-3.8-22']:
    with open(file + '.json') as fp:
        data = json.load(fp)

    ftype = 'licenses' if 'licenses' in data else 'exceptions'
    meta = {'module': 'http:/spdx.org/' + tt[ftype]['mt'] + '/' + data['licenseListVersion']}
    types = [
        [ftype.capitalize(), 'Enumerated', [], '',
        [[int(x['referenceNumber']), x[tt[ftype]['id']], x['name']] for x in data[ftype]]]
    ]

    with open(file + '.jadn', 'w') as fp:
        json.dump({'meta': meta, 'types': types}, fp, indent=1)

    print('Version:', data['licenseListVersion'] + ':', len(types[0][4]), ftype)