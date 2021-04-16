#! /media/pavan/Data/Work/Work_Github/env/bi_server_env/bin/python
import os
import time
import json
from flask import request, g, jsonify
from app import create_app

app = create_app()

@app.errorhandler(404) 
  
# inbuilt function which takes error as parameter 
def not_found(e): 
  
# defining function 
  return jsonify(
      {
        "message": "Not Found",
        "error": {
            "status": 404
        }
    }), 404

@app.before_request
def option_autoreply():
    """ Always reply 200 on OPTIONS request """

    g.request_start_time = time.time()

    if request.method == 'OPTIONS':
        resp = app.make_default_options_response()

        headers = None
        
        h = resp.headers

        h['Content-Type'] = 'application/json'


        return resp


@app.after_request
def set_allow_origin(resp):
    h = resp.headers
    resp.add_etag()


    try:
        body = json.loads(resp.get_data())
    except:
        body = {}
    if body:
        response_data = body
        if not "error" in body:
            status = body.get("status")
            if status is not None:

                del body["status"]
                
                response_data["status"] = status


    else:
        response_data = {
            "status":False,
            "error_obj":{
                "error_code":"unknown",
                "message":"There is some problem. PLease try again after sometime"
            }
        }
    response_data = json.dumps(response_data)
    resp.set_data(response_data)

    elapsed = time.time() - g.request_start_time
    elapsed = '{}ms'.format(round(1000 * elapsed,2))
    h['X-Response-Time'] = elapsed

    return resp
