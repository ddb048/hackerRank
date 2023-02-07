# NOTE - JSON Diff Tool

# NOTE - Implement a simple prototype service to find the differnce between tow json objects.  Keep the protoype simple. A JSON will contain only KVP and no nested objects or arrays in  it.  Given two JSION strings, JSON1 JSON2, find the list of keys for which the values are different.  If a  eky is present in only one of teh JSONS it should not be considered in teh result.  The list of keys should be sorted in lexicographically ascending order.

import json

json1 = "{'hello':'world', 'hi': 'hello', 'you':'me'}"

json2 = "{'hello': 'world', 'hi': 'helloo', 'you': 'me'}"

json1 = json.loads(json1)

json2 = json.loads(json2)

keysList1 = json1.keys()

keysList2 = json2.keys()

valuesList1 = json1.values()

valuesList2 = json2.values()
