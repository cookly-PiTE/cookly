# **cookly**
## Participants
 * Przemysław Markiewicz
 * Bartłomiej Długosz
 * Dominik Kobyra
 * Tomasz Praszkiewicz
 
 ## Short description of the idea
Web application that helps people to find recipes based on their requirements and needs. 

## Project configuration and running locally
To tun application locally you need to run following commands:
* install virtual environment: `sudo apt install python3-virtualenv`
* Create virtual environment:`virtualenv venv --python=python3.8`
* Activate virtualenv:
    * on linux: `source venv/bin/activate` (deactivate with `deactivate` command)
    * on windows: `.\venv\Scripts\activate`
* Install dependencies `pip install -r requirements.txt`
* get secret values - you have to create `.env` file (it should look like `.env.example`) and ask for secret variables
* To load recipes into database it may be necessary to run script `python manage.py runscript load_data` 
* Run application `python manage.py runserver`
## Technology stack
* Backend: Python, Django
* Frontend: Django templates, Bootstrap
* Database: MongoDB
## Features
* Allowing user to search for recipes using tags and ingredients
* Allowing user to rate and comment on recipes
* Allowing user to filter recipes based on ratings and popularity
* Allowing user to get a random recipe with a lucky roll
* User can add new recipe to database
## Roadmap
#### sprint 1 (16.11-22.11)
* Creating environment and installation script
* Basic structure of project
* Connecting MongoDB to Django
* Travis CI basic configuration (for automatic testing)
### sprint 2 (23.11-29.11)
* Basic UI layout
* Maintain and load dataset to the database
* Write unit tests for functionality.
* Endpoint for randomizing entire food set for the day**
### sprint 3 (30.11-6.12)
* Create site for recipe details
* Make searching webpage
* Most searched recipes (at home site)
* Write unit tests for functionality
### sprint 4 (7.12-13.12)
* Finish styling webpage with CSS and Bootstrap
* Allow user to see highest rated recipes
* Final corrections and test


