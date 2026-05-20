from database.models import db, Notes
from typing import Optional, Dict, Any

import logging

logger = logging.getLogger(__name__)

def add_note_to_db(content: str,
                     call_id: str,
                    ) -> Optional[Dict[str, Any]]: 

    try:
        note = Notes(content= content,
                    call_id= call_id,
                    )
        db.session.add(note)
        db.session.commit()
        logger.info(f"Note added to call with ID {call_id} successfully.")
        return note.to_dict()
    
    except Exception as e:
        db.session.rollback()
        logger.error(f"Error occurred on repository level while adding note to call with ID {call_id}: {e}")
        return None    

