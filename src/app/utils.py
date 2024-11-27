import json
from typing import Dict


def to_json(data: Dict[str, str]) -> bytes:
    return json.dumps(data).encode("utf-8")
