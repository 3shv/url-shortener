# url-shortener

This is a sample implementation of URL-shortener service using Django, python 3.x

APIs built:

    1. Creating a shortened URL -- (/api/create/)
    
        Input: POST {
                        "target_url": "http://google.com/"
                    }

    2. Configuring it for different user agents (/api/configure/)
    
        Input: POST {
                        "slug": "12345678",
                         "config": [
                            "user_agent": "mozilla",
                            "target_url": "http://m.facebook.com"/
                         ]
                    }

    3. List all urls submitted with their navigation counts and time elapsed (/api/urls/)

    4. Navigation to target-url (/(?P[a-zA-Z0-9])/
    
            GET /12345678/
    
You can test using these sample postman API collection provided [here](https://www.getpostman.com/collections/e2558ca1600cde040258) 

Installation instructions:

   You can use a virtual environment to create isolated environments. See <http://docs.python-guide.org/en/latest/dev/virtualenvs/>

   Dependencies:

    Python 3.5

    Django 1.10 
   See <https://docs.djangoproject.com/en/1.10/topics/install/>

    Steps:

        1. pip install -r requirements.txt

        2. cd project/ # outermost project folder

        3. python manage.py migrate # creates tables

        4. python manage.py runserver # Opens a local server on 8000

