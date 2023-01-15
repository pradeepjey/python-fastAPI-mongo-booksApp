import json
from bson import json_util

def bson_to_json(o):
    for k, v in o.items():
        if  k == '_id':
            o['_id'] = str(o['_id'])

        if type(k) is dict():
            return bson_to_json(o[k])
        return o

def parse_json(data):
    return json.loads(json_util.dumps(data))