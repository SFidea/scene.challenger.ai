import sys
import json
import yaml


if len(sys.argv)!=2:
    print "Usage: python %s <json file>" % sys.argv[0]
    sys.exit(1)

with open(sys.argv[1], 'rb') as f:
    annotations = json.load(f)

print yaml.safe_dump(annotations, default_flow_style=False, allow_unicode=True)

