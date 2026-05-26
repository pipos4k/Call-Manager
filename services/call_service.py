from typing import List, Optional, Dict, Any, Tuple
import logging

from repositories import call_repository as repo

logger = logging.getLogger(__name__)


def get_all_calls() -> Tuple[List[Dict[str, Any]], Optional[str]]:

    try:
        calls = repo.get_all_calls()
        return calls, None

    except Exception as e:
        logger.error(f"Error occurred while fetching all calls: {e}")
        return [], "An error occurred while fetching calls."


def get_all_archived_calls() -> Tuple[List[Dict[str, Any]], Optional[str]]:

    try:
        calls = repo.get_all_archived_calls()
        return calls, None

    except Exception as e:
        logger.error(f"Error occurred while fetching archived calls: {e}")
        return [], "An error occurred while fetching archived calls."
    

def get_call_by_id(call_id: str) -> Tuple[Optional[Dict[str, Any]], Optional[str]]:

    try:
        call = repo.get_call_by_id(call_id)
        return (call, None) if call else (None, "Call not found.")

    except Exception as e:
        logger.error(f"Error occurred while fetching call by ID {call_id}: {e}")
        return None, "An error occurred while fetching the call."

def archive_call(call_id: str) -> Tuple[bool, Optional[str]]:

    try:
        success = repo.archive_call(call_id)
        return (success, None) if success else (False, "Call not found or failed to archive.")
    
    except Exception as e:
        logger.error(f"Error occurred while archiving call with ID {call_id}: {e}")
        return False, "An error occurred while archiving the call."
    

def unarchive_call(call_id: str) -> Tuple[bool, Optional[str]]:

    try:
        success = repo.unarchive_call(call_id)
        return (success, None) if success else (False, "Call not found or failed to unarchive.")

    except Exception as e:
        logger.error(f"Error occurred while unarchiving call with ID {call_id}: {e}")
        return False, "An error occurred while unarchiving the call."
    

def delete_call(call_id: str) -> Tuple[bool, Optional[str]]:

    try:
        success = repo.delete_call(call_id)
        return (success, None) if success else (False, "Call not found or failed to delete.")

    except Exception as e:
        logger.error(f"Error occurred while deleting call with ID {call_id}: {e}")
        return False, "An error occurred while deleting the call."
    
