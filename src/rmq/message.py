from aio_pika import Message

from typing import Dict


def create_message(body: str, project: str) -> Message:
    headers: Dict[str, str] = {
        "project": project
    }
    message = Message(
        body=body.encode("utf-8"),
        headers=headers
    )
    return message
