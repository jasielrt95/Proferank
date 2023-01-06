import os


def populate():
    # Run the commands to populate the database
    os.system("python manage.py populate_professors")
    os.system("python manage.py populate_courses")
    os.system("python manage.py populate_course_comments")
    os.system("python manage.py populate_confessions")
    os.system("python manage.py populate_confession_comments")
    print("The database has been populated successfully!")

if __name__ == "__main__":
    populate()