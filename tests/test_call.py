import pytest
from unittest.mock import patch
from services import call_service

from mock_data import *

# Mock data for testing
MOCK_DATA = generate_mock_data()
MOCK_CALLS_NOT_ARCHIVED = non_archived_mock_data(MOCK_DATA)
MOCK_CALLS_ARCHIVED = archived_mock_data(MOCK_DATA)
# ------------------------------------------------------------------------------
# Tests for get_all_calls
@patch("services.call_service.repo.get_all_calls")
def test_get_all_calls_success(mock_repo):
    mock_repo.return_value = MOCK_CALLS_NOT_ARCHIVED

    calls, error = call_service.get_all_calls()
    
    assert calls[0]["is_archived"] == False
    assert error is None


@patch("services.call_service.repo.get_all_calls")
def test_get_all_calls_is_not_empty(mock_repo):
    mock_repo.return_value = MOCK_CALLS_NOT_ARCHIVED

    calls, error = call_service.get_all_calls()
    
    assert len(calls) >= 1
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
    mock_repo.return_value = MOCK_CALLS_ARCHIVED

    calls, error = call_service.get_all_archived_calls()
    
    assert calls[0]["is_archived"] == True
    assert error is None


@patch("services.call_service.repo.get_all_archived_calls")
def test_get_all_archived_calls_is_not_empty(mock_repo):
    mock_repo.return_value = MOCK_CALLS_ARCHIVED

    calls, error = call_service.get_all_archived_calls()
    
    assert len(calls) >= 1
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
    mock_repo.return_value = MOCK_DATA[0]

    call, error = call_service.get_call_by_id(mock_repo["call_id"])
    
    assert call["call_id"] == mock_repo.return_value["call_id"]
    assert error is None


@patch("services.call_service.repo.get_call_by_id")
def test_get_call_by_id_not_found(mock_repo):
    mock_repo.return_value = None

    call, error = call_service.get_call_by_id("non-existent-id")
    
    assert call is None
    assert error == "Call not found."
