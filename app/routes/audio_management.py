from uuid import uuid4
from flask import Blueprint, jsonify, request
from ..services.audio_management import AudioManagementObject

audio_management = Blueprint('audio_management', __name__)



@audio_management.route('/<file_type>', methods=['GET'], defaults={"file_id": None})
@audio_management.route('/<file_type>/<file_id>', methods=['GET'])
def get_file_invoker(file_type, file_id = ""):
    request_data = request.get_json()
    request_id = str(uuid4())

    output = AudioManagementObject.get_file(request_id, file_type, file_id)

    return jsonify( output )

@audio_management.route('/<file_type>/<file_id>', methods=['POST'])
def update_file_invoker(file_type, file_id ):
    request_data = request.get_json().get("data", {})
    request_id = str(uuid4())

    output = AudioManagementObject.update_file(request_id, file_type, file_id, request_data)

    return jsonify( output )

@audio_management.route('/<file_type>/<file_id>', methods=['DELETE'])
def delete_file_invoker(file_type, file_id):
    request_data = request.get_json()
    request_id = str(uuid4())

    output = AudioManagementObject.delete_file(request_id, file_type, file_id)

    return jsonify( output )

@audio_management.route('/create', methods=['POST'])
def publish_event():
    request_data = request.get_json().get("data",{})
    request_id = str(uuid4())
    output = AudioManagementObject.create_file(request_id,request_data)

    return jsonify( output )