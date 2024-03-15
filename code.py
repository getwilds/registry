import json
import datetime
from ghapi.all import GhApi

ORG = 'getwilds'

api = GhApi()

repos = api.repos.list_for_org(ORG)

target_keys = ['name', 'private', 'fork', 'description', 'html_url']

data = {}
data['repos'] = [{key: w[key] for key in target_keys} for w in repos]
data['updated'] = datetime.datetime.now(datetime.UTC).isoformat()

with open('registry.json', 'w') as file:
	json.dump(data, file)
