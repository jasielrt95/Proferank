import os


def build():
    print("Formating python files..")
    os.system("black .")
    print("Formating python files.. Done")
    print("Formating templates")
    os.system("djlint .")
    print("Formating templates.. Done")


if __name__ == "__main__":
    build()
