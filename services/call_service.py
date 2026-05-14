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
    
def get_call_by_id(call_id: str) -> Optional[Dict[str, Any]]:

    try:
        call = repo.get_call_by_id(call_id)
        return call

    except Exception as e:
        logger.error(f"Error occurred while fetching call by ID {call_id}: {e}")
        return None
    
def archive_call(call_id: str) -> bool:

    try:
        success = repo.archive_call(call_id)
        return True if success else False

    except Exception as e:
        logger.error(f"Error occurred while archiving call with ID {call_id}: {e}")
        return False
    
