import sys
import json
import yaml


with open('original/scene_train_annotations.json', 'rb') as f:
    annotations = json.load(f)

print yaml.safe_dump(annotations, default_flow_style=False, allow_unicode=True)

