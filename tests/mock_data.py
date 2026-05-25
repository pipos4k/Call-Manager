import random
from typing import List, Dict, Any

def generate_mock_data() -> List[Dict[str, Any]]:
    mock_data = []

    direction = ["inbound", "outbound"]
    is_archived = [True, False]
    call_type = ["missed", "answered", "voicemail"]

    for mock in range(5):
        mock_data.append({
            "call_id": f"2c94669a-0be0-4e4f-8d8e-b13c6c8ed9d{mock}",
            "direction": random.choice(direction),
            "caller": f"231161410034{mock}",
            "callee": f"441256413{mock}",
            "call_duration": 120 + mock,
            "created_at": f"2024-06-{1+mock}T12:00:00Z",
            "is_archived": random.choice(is_archived),
            "call_type": random.choice(call_type),
        })

    return mock_data

def non_archived_mock_data(mock_data) -> List[Dict[str, Any]]:
    non_archived_data = []

    for call in mock_data:
        if call["is_archived"] == False:
            non_archived_data.append(call)

    return non_archived_data


def archived_mock_data(mock_data) -> List[Dict[str, Any]]:
    archived_data = []

    for call in mock_data:
        if call["is_archived"] == True:
            archived_data.append(call)

    return archived_data
