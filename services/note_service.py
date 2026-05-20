from repositories import note_repository as repo
from typing import Optional, Dict, Any, Tuple

import logging

logger = logging.getLogger(__name__)

def add_note_service(content: str,
                    call_id: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:

    try:
        content = content.strip()
        call_id = call_id

        note = repo.add_note_to_db(
            content= content,
            call_id= call_id,
            )

        logger.info(f"Note added to call with ID {call_id} successfully.")
        return (note, None) if note else (None, "Failed to add note to the call.")

    except Exception as e:
        logger.error(f"Error occurred on service level while adding note to call with ID {call_id}: {e}")
        return None, "An error occurred while adding the note to the call."
    