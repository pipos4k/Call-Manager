from database.models import db, Notes
from typing import Optional, Dict, Any

import logging

logger = logging.getLogger(__name__)

def add_note_to_db(note_id: str,
                     content: str,
                     call_id: str,
                     created_at) -> Optional[Dict[str, Any]]: 

    try:
        note = Notes(note_id= note_id,
                    content= content,
                    call_id= call_id,
                    created_at= created_at)

        db.session.add(note)
        db.session.commit()
        logger.info(f"Note with ID {note_id} added to call with ID {call_id} successfully.")
        return note.to_dict()
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error occurred on repository level while adding note to call with ID {call_id}: {e}")
        return None    

