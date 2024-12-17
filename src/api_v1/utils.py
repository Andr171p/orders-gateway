import json
from typing import Dict


def to_json(data: Dict[str, str]) -> str:
    return json.dumps(data)