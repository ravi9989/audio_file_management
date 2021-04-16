import os
import datetime
from app.models.song import Song 
from app.models.podcast import Podcast
from app.models.book import Book
from ..error_codes import error_code

file_types = {
    "song" : Song,
    "podcast" : Podcast,
    "audio_book" : Book

}

CURRENT_WORKING_DIRECTORY = os.getcwd()

class AudioManagement(object):

    def __init__(self):
        pass

    def get_file(self, request_id, file_type, file_name):

        if file_type not in file_types:

            return error_code["ERROR_WITH_FILE_TYPE"]

        if not file_name:

            return {
                "status" : True,
                "data" : file_types[file_type].objects(**{})
            }

        else:

            return {
                "status" : True,
                "data" : file_types[file_type].objects(**{"Id" : file_name})
            }


    def update_file(self, request_id, file_type, file_name, request_data):

        try:

            document = file_types[file_type].objects.filter(Id=file_name).update(**{'set__'+ i : request_data[i] for i in request_data.keys()})
            if not document:

                return error_code["NO_RECORD_FOUND"]
            
            return {
                    "status" : True,
                    "message" : "successfully deleted given record/file"
                }

        except :
            
            return error_code["REQ_FIELDS"]


    def delete_file(self, request_id, file_type, file_name):

        if file_type not in file_types:

            return error_code["ERROR_WITH_FILE_TYPE"]

        existing_record = file_types[file_type].objects(Id = file_name)

        if not existing_record:

            return error_code["NO_RECORD_FOUND"]

        result = file_types[file_type].objects(**{"Id" : file_name}).delete()

        if not result :
            
            return error_code["NO_RECORD_FOUND"]

        if result :

            return {
                "status" : True,
                "message" : "successfully deleted given record/file"
            }


    def create_file(self, request_id, data):

        file_type = data.get("file_type", "")
        if not file_type:
            return error_code["ERROR_WITH_FILE_TYPE"]
        
        check_existing = file_types[file_type].objects(**{"Id" : data.get("Id")})

        if check_existing:

            return error_code["DUPLICATE_RECORD_FOUND"]
        
        response = {} 
        data["uploaded_time"] = datetime.datetime.now()

        try:
            
            response = file_types[file_type](**data).save()
        
        except:
            
            return error_code["REQ_FIELDS"]

        if not response : 

            return error_code["REQ_FIELDS"]
            
        return {
            "status" : True,
            "message" : "successfully created a record"
        }


AudioManagementObject = AudioManagement()