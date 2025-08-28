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

        Note: The above commands should start the server, if both dosen't work simple reach out via rensytimsy03@gmail.com, or whatsapp +254790337192

    3. Testing the enpoints
        *Personally i use postman to test api endpoints, use the following steps to do so 
            1.create a post request: http://localhost:8080/api/v1/shorten-url
            2.provide a json body: {"url" : "url to shorten here"}
            3.you will get back a response body with the shortened url.

    DISCLAIMER: Note that url conversion/shortening on this project does not work on local environment, simply this project demonstrates how url are converted and the user get's back the shortend url. In simple terms what i am saying is the returned shortened urls do not work on the browser they are simply used as dummys to explain the formating algorithm

Good luck hope you might find this simple project intuitive and good. Happy coding.