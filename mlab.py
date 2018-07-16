import mongoengine

# mongodb://<admin>:<admin123>@ds135421.mlab.com:35421/love-assistant

host = "ds135421.mlab.com"
port = 35421
db_name = "love-assistant"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())