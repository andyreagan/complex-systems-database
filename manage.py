#!/usr/bin/python
import os
import sys

#print(sys.path)
from dotenv import load_dotenv, find_dotenv
#print(dir(dotenv))
load_dotenv()
#load_dotenv(find_dotenv())
#dotenv.load(dotenv.find())

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
