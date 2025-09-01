Here is a simple fastapi server that simply shortenes url to make it easier to share and readable

    First step:
        1. Create a virtual environment usning python e.g python3 -m venv venv or you can name it instead of venv myvenv
        2. Using the requirements.txt file one can get to install all the required dependacies for this project

    Second step:
        *Once the virtual environment has been created you can simple run the application in two ways/methods
            1.Using uvicorn
                command in the terminal: uvicorn app.main:app --reload --host 0.0.0.0 --port 8080

            2.Using fastapi dev
                command in the terminal: fastapi dev app/main.py

    3. Testing the enpoints
        *Personally i use postman to test api endpoints, use the following steps to do so 
            1.create a post request: http://localhost:8080/api/v1/shorten-url
            2.provide a json body: {"url" : "url to shorten here"}
            3.you will get back a response body with the shortened url.

    The url is formatted and then using this endpoint: "http://localhost:8080/api/v1/url-redirect/short-url" one will get an automatic redirect. Note the short-url is the url you get once you have shortned the url on "http://localhost:8080/api/v1/shorten-url".

Good luck hope you might find this simple project intuitive and good. Happy coding.