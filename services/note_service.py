from repositories import note_repository as repo
from typing import Optional, Dict, Any

from datetime import timezone, datetime
import uuid
import logging

logger = logging.getLogger(__name__)

def add_note_service(content: str,
                    call_id: str) -> Optional[Dict[str, Any]]:

    try:
        note_id = str(uuid.uuid4())
        content = content.strip()
        call_id = call_id
        created_at = datetime.now(timezone.utc).isoformat()

        note = repo.add_note_to_db(
            note_id= note_id, 
            content= content,
            call_id= call_id,
            created_at= created_at
            )

        logger.info(f"Note with ID {note_id} added to call with ID {call_id} successfully.")
        return note

    except Exception as e:
        logger.error(f"Error occurred on service level while adding note to call with ID {call_id}: {e}")
        return None
    