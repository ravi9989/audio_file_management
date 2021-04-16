# filed_audio_file_server


1. Setup codebase
 
    1. clone the repository in a directory
            git clone 
    2. go in the directory `cd filed_audio_file_server`
    3. create virtual environment
        `virtualenv venv`
    4. activate environment
        `source venv/bin/activate`
    5. install all project requirements, use command
        `pip3 install -r requirements.txt`
    
2. run the command
    `python3 serve.py`

# apis end point

#### 1. create
    url = /api/v1/create 
    method = Post
    content-type=application/json
    
    -url : /api/v1/create
    - request body:

        {
            "data" : {
                "file_type" : "song"
                "title" : "sorry",
                "duaration_in_secs" : 500
            }
        }
        
                    
####2. Update

    url = /api/v1/<audioFileType>/<audioFileID> 
    method = POST
    content-type=application/json
    
    - url : `/api/v1/audiobook/1`       
    - request body:

        {
            "data" : {
                "title" : "updating_string"
            }
            
        }

##3. delete
  
    url = /api/v1/<audioFileType>/<audioFileID>
    method = DELETE
    content-type = application/json
-example
    - url : `/api/v1/audiobook/1` - delete record present at id 1

##4. get

   1. - url:  `/api/v1/<audioFileType>`
      - description: `get all the data present in <audioFileType> database`
   2.- url:  `/api/v1/<audioFileType>/<audioFileID>`
      - description: `get all data present in <audioFileType> database having id `audioFileID`    
   3. ###### urls
   
           
          url1 = `/api/v1/audiobook` - get all data in audiobook in database
          url2 = `/api/v1/audiobook/1` - get data having id 1
    
    
### Response from REQUEST

    - Action is successful: 200 OK
    - The request is invalid: 406 bad request
    - Any error: 500 internal server error