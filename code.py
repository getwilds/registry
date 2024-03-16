import json
import fastcore
import datetime
from ghapi.all import GhApi

ORG = 'getwilds'

api = GhApi()

repos = api.repos.list_for_org(ORG)

target_keys = ['name', 'private', 'fork', 'description', 'html_url', 'topics']

data = {}
data['repos'] = [{key: w[key] for key in target_keys} for w in repos]
data['updated'] = datetime.datetime.now(datetime.UTC).isoformat()

class LEncoder(json.JSONEncoder):
	def default(self, obj):
	   if isinstance(obj, fastcore.foundation.L):
	      return list(obj)
	   return json.JSONEncoder.default(self, obj)

with open('registry.json', 'w') as file:
	json.dump(data, file, cls=LEncoder)
