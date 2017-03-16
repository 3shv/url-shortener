# url-shortener

This is a sample implementation of URL-shortener service using Django, python 3.x

APIs built:

    1. Creating a shortened URL -- (/api/create/)

    2. Configuring it for different user agents (/api/configure/)

    3. List all urls submitted with their navigation counts and time elapsed (/api/urls/)

    4. Navigation to target-url (/(?P[a-zA-Z0-9])/

Installation instructions:

    You can use a virtual environment to create isolated environments. See http://docs.python-guide.org/en/latest/dev/virtualenvs/

    Dependencies:

        Python 3.5

        Django 1.10 See https://docs.djangoproject.com/en/1.10/topics/install/

    Steps:

        1. pip install -r requirements.txt

        2. cd project/ # outermost project folder

        3. python manage.py migrate # creates tables

        4. python manage.py runserver # Opens a local server on 8000

