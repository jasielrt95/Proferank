import os


def populate():

    # if db doesn't exist, create it
    if not os.path.exists("db.sqlite3"):
        os.system("python manage.py migrate")

    os.system("python manage.py createsuperuser")
    os.system("python manage.py populate_professors")
    os.system("python manage.py populate_courses")
    os.system("python manage.py populate_course_comments")
    os.system("python manage.py populate_confessions")
    os.system("python manage.py populate_confession_comments")
    print("The database has been populated successfully!")

if __name__ == "__main__":
    populate()