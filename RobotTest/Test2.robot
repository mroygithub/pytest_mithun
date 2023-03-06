*** Settings ***

Library           RequestsLibrary

*** Variables ***
${Url_one}  https://www.google.com

${JsonBody}

{
  "id": 2002,
  "category": {
    "id": 0,
    "name": "Samsung"
  },
  "name": "Tiger",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}

*** Test Cases ***

Verify Google Application

    create session  mysession   ${Url_one}
    ${response} =   Get Request  mysession  ${Url_one}
    log to console  ${response.status_code}
    log to console  ${response.content}
    log to console  ${response.headers}
    ${status_code}=  Convert To String   ${response.status_code}
    should be equal     ${status_code}     200


PET Application

    ${resp}=    POST On Session    jsonplaceholder  /posts  json=${JsonBody}
    Status Should Be                 200  ${resp}


