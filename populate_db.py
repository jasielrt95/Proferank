import os
import argparse
import time


def populate():
    start_time = time.time()
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--reset", help="reset the database", action="store_true")

    args = parser.parse_args()

    # if reset, delete db
    if args.reset:
        if os.path.exists("db.sqlite3"):
            os.remove("db.sqlite3")

    # if db doesn't exist, create it
    if not os.path.exists("db.sqlite3"):
        os.system("python manage.py makemigrations")
        os.system("python manage.py migrate")

    os.system(
        "python manage.py createsuperuser --username jasiel --email jasielrt95@gmail.com"
    )
    os.system("python manage.py populate_professors")
    os.system("python manage.py populate_courses")
    os.system("python manage.py populate_course_comments")
    os.system("python manage.py populate_confessions")
    os.system("python manage.py populate_confession_comments")
    os.system("python manage.py populate_reviews")
    print("The database has been populated successfully!")
    # minutes elapsed
    print("Elapsed time: %s minutes" % ((time.time() - start_time) / 60))


if __name__ == "__main__":
    populate()
