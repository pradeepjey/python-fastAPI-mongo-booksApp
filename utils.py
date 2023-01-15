def removeNoneKey(object):
    return {k: v for k, v in object.items() if v}