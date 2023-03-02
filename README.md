# Description
- Proferank is a project where students from different universities in Puerto Rico can rate their professors based on the courses they teach. Additionally, it provides a platform for making anonymous confessions about anything!
# Technology
- Django 4.11
- Tailwinds CSS
# How to run the project
- Create a virtual environment ( I use Pipenv )
- Install the dependencies (You can use the requirements.txt or the Pipfile)
- Activate the virtual environment 
- Run the following commands:
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py tailwind install
$ python manage.py tailwind build
$ python manage.py runserver
```
## Suggestions
- To leave suggestions you can use the following link https://www.proferank.com/reviews/suggestions?next=/ 
