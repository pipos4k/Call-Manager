from flask import Flask, jsonify, request
import logging
import sys

from database import setup_database
from services import call_service, note_service

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout) 
]
)

logger = logging.getLogger(__name__)

setup_database.init_db(app)

@app.route("/calls", methods=["GET"])
def get_all_calls():
    
    try:
        calls, error = call_service.get_all_calls()

        if error:
            return _error_response(error, 500)
        return _success_response({"calls": calls})
    
    except Exception as e:
        logger.error(f"Error occurred while fetching all calls: {e}")
        return _error_response("An error occurred while fetching calls.", 500)

@app.route("/calls/archived", methods=["GET"])
def get_all_archived_calls():

    try:
        calls, error = call_service.get_all_archived_calls()

        if error:
            return _error_response(error, 500)
        return _success_response({"calls": calls})
    
    except Exception as e:
        logger.error(f"Error occurred while fetching archived calls: {e}")
        return _error_response("An error occurred while fetching archived calls.", 500)
    

@app.route("/calls/<call_id>", methods=["GET"])
def get_call_by_id(call_id):

    try:
        call = call_service.get_call_by_id(call_id)

        if not call:
            return _error_response("Call not found.", 404)
        return _success_response({"call": call})

    except Exception as e:
        logger.error(f"Error occurred while fetching call by ID {call_id}: {e}")
        return _error_response("An error occurred while fetching the call.", 500)


@app.route("/calls/<call_id>/notes", methods=["POST"])
def add_note_to_call(call_id):

    try:
        call_id = call_id

        data = request.get_json()
        if not data:
            return _error_response("Invalid JSON body.", 400)

        content = data.get("content")

        note = note_service.add_note_service(
            content, 
            call_id)

        if not note:
            return _error_response("Failed to add note to call. Call or Note may not exist.", 404)
        return _success_response({"note": note}, 201)

    except Exception as e:
        logger.error(f"Error occurred while adding note to call with ID {call_id}: {e}")
        return _error_response("An error occurred while adding the note to the call.", 500)
    

@app.route("/calls/<call_id>/archive", methods=["PATCH"])
def archive_call(call_id):

    try:
        success = call_service.archive_call(call_id)

        if not success:
            return _error_response("Failed to archive call.", 404)
        return _success_response({"message": "Call archived successfully."})

    except Exception as e:
        logger.error(f"Error occurred while archiving call with ID {call_id}: {e}")
        return _error_response("An error occurred while archiving the call.", 500)


@app.route("/calls/<call_id>/unarchive", methods=["PATCH"])
def unarchive_call(call_id):

    try:
        success = call_service.unarchive_call(call_id)

        if not success:
            return _error_response("Failed to unarchive call.", 404)
        return _success_response({"message": "Call unarchived successfully."})

    except Exception as e:
        logger.error(f"Error occurred while unarchiving call with ID {call_id}: {e}")
        return _error_response("An error occurred while unarchiving the call.", 500)
    

@app.route("/calls/<call_id>", methods=["DELETE"])
def delete_call(call_id):

    try:
        success = call_service.delete_call(call_id)

        if not success:
            return _error_response("Failed to delete call.", 404)
        return _success_response({"message": "Call deleted successfully."})

    except Exception as e:
        logger.error(f"Error occurred while deleting call with ID {call_id}: {e}")
        return _error_response("An error occurred while deleting the call.", 500)
    

def _success_response(data, status_code: int = 200):

    return jsonify({"success": True, **data}), status_code


def _error_response(message: str, status_code: int = 400):

    return jsonify({"success": False, "error": message}), status_code


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)

