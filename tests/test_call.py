import pytest
from unittest.mock import patch
from services import call_service

# Na ftiakso mock data LIST?
# Mock data for testing
MOCK_CALL_NOT_ARCHIVED = [{"call_id": "2c94669a-0be0-4e4f-8d8e-b13c6c8ed9d4",
                    "direction": "inbound",
                    "caller": "2311614100344",
                    "callee": "4412564131",
                    "call_duration": 120,
                    "created_at": "2024-06-01T12:00:00Z",
                    "is_archived": False,
                    "call_type": "voicemail",}]

MOCK_CALL_ARCHIVED = [{"call_id": "2c94669a-0be0-4e4f-8d8e-13c6c8ed9d4",
                    "direction": "bound",
                    "caller": "3111614100344",
                    "callee": "9312564131",
                    "call_duration": 400,
                    "created_at": "2023-01-03T16:10:53Z",
                    "is_archived": True,
                    "call_type": "answered",}]

# ------------------------------------------------------------------------------
# Tests for get_all_calls
@patch("services.call_service.repo.get_all_calls")
def test_get_all_calls_success(mock_repo):
    mock_repo.return_value = MOCK_CALL_NOT_ARCHIVED

    calls, error = call_service.get_all_calls()
    
    assert calls[0]["is_archived"] == False
    assert error is None


@patch("services.call_service.repo.get_all_calls")
def test_get_all_calls_is_not_empty(mock_repo):
    mock_repo.return_value = MOCK_CALL_NOT_ARCHIVED

    calls, error = call_service.get_all_calls()
    
    assert len(calls) == 1
    assert error is None


@patch("services.call_service.repo.get_all_calls")
def test_get_all_calls_failure(mock_repo):
    mock_repo.side_effect = Exception("Database connection failed")
    
    calls, error = call_service.get_all_calls()
    
    assert len(calls) == 0
    assert error == "An error occurred while fetching calls."


# ------------------------------------------------------------------------------
# Tests for get_all_archived_calls
@patch("services.call_service.repo.get_all_archived_calls")
def test_get_all_archived_calls_success(mock_repo):
    mock_repo.return_value = MOCK_CALL_ARCHIVED

    calls, error = call_service.get_all_archived_calls()
    
    assert calls[0]["is_archived"] == True
    assert error is None


@patch("services.call_service.repo.get_all_archived_calls")
def test_get_all_archived_calls_is_not_empty(mock_repo):
    mock_repo.return_value = MOCK_CALL_ARCHIVED

    calls, error = call_service.get_all_archived_calls()
    
    assert len(calls) == 1
    assert error is None


@patch("services.call_service.repo.get_all_archived_calls")
def test_get_all_archived_calls_failure(mock_repo):
    mock_repo.side_effect = Exception("Database connection failed")
    
    calls, error = call_service.get_all_archived_calls()
    
    assert len(calls) == 0
    assert error == "An error occurred while fetching archived calls."


# ------------------------------------------------------------------------------
# Tests for get_call_by_id
@patch("services.call_service.repo.get_call_by_id")
def test_get_call_by_id_success(mock_repo): 
    mock_repo.return_value = MOCK_CALL_NOT_ARCHIVED[0]

    call, error = call_service.get_call_by_id("2c94669a-0be0-4e4f-8d8e-b13c6c8ed9d4")
    
    assert call["call_id"] == "2c94669a-0be0-4e4f-8d8e-b13c6c8ed9d4"
    assert error is None


@patch("services.call_service.repo.get_call_by_id")
def test_get_call_by_id_not_found(mock_repo):
    mock_repo.return_value = None

    call, error = call_service.get_call_by_id("non-existent-id")
    
    assert call is None
    assert error == "Call not found."
