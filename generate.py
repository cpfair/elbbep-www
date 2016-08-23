from jinja2 import Template
import json

NICE_NAMES = {
    "ev2_4": "Original V2R2",
    "v1_5": "Origin V3R&hellip;",
    "v2_0": "Steel",
    "snowy_dvt": "Time",
    "snowy_s3": "Time Steel",
    "spalding": "Time Round"
}
HW_REVS = ["ev2_4", "v1_5", "v2_0", "snowy_dvt", "snowy_s3", "spalding"]

MANIFEST = json.load(open("static/packages/manifest.json", "r"))
for k, item in MANIFEST.items():
    item["name"] = NICE_NAMES[k]
SORTED_MANIFEST = sorted(MANIFEST.items(), key=lambda x: HW_REVS.index(x[0]))

template = Template(open("templates/site.html", "r").read())
rendered = template.render(sorted_manifest=SORTED_MANIFEST)
open("index.html", "w").write(rendered)
