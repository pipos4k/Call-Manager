from database.models import db, Call
from typing import List, Optional, Any, Dict
import logging

logger = logging.getLogger(__name__)


def get_all_calls() -> List[Dict[str, Any]]:

    try: 
        calls = Call.query.filter_by(is_archived=False)
        return [call.to_dict() for call in calls.all()]

    except Exception as e:
        logger.error(f"Error occurred while fetching all calls: {e}")
        return []
    

def get_all_archived_calls() -> List[Dict[str, Any]]:

    try: 
        calls = Call.query.filter_by(is_archived=True)
        return [call.to_dict() for call in calls.all()]

    except Exception as e:
        logger.error(f"Error occurred while fetching archived calls: {e}")
        return []
    

def get_call_by_id(call_id: str) -> Optional[Dict[str, Any]]:

    try:
        call = Call.query.filter_by(call_id=call_id).first()
        return call.to_dict() if call else None

    except Exception as e:
        logger.error(f"Error occurred while fetching call by ID {call_id}: {e}")
        return None

def archive_call(call_id: str) -> bool:

    try:
        call = Call.query.filter_by(call_id=call_id).first()
        if not call:
            logger.warning(f"Call with ID {call_id} not found for archiving.")
            return False
        
        call.is_archived = True

        db.session.commit()
        logger.info(f"Call with ID {call_id} archived successfully.")
        return True

    except Exception as e:
        db.session.rollback()
        logger.error(f"Error occurred while archiving call with ID {call_id}: {e}")
        return False
    
def unarchive_call(call_id: str) -> bool:

    try:
        call = Call.query.filter_by(call_id=call_id).first()
        if not call:
            logger.warning(f"Call with ID {call_id} not found for unarchiving.")
            return False
        
        call.is_archived = False

        db.session.commit()
        logger.info(f"Call with ID {call_id} unarchived successfully.")
        return True

    except Exception as e:
        db.session.rollback()
        logger.error(f"Error occurred while unarchiving call with ID {call_id}: {e}")
        return False
    

def delete_call(call_id: str) -> bool:

    try:
        call = Call.query.filter_by(call_id=call_id).first()
        if not call:
            logger.warning(f"Call with ID {call_id} not found for deletion.")
            return False
        
        db.session.delete(call)
        db.session.commit()
        logger.info(f"Call with ID {call_id} deleted successfully.")
        return True

    except Exception as e:
        db.session.rollback()
        logger.error(f"Error occurred while deleting call with ID {call_id}: {e}")
        return False

