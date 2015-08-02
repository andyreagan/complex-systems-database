#! /usr/bin/env python
import os, sys
sys.path.append('/users/c/m/cmplxsys/www-root/db/complex-systems-database')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
os.environ['DJ_SECRET_KEY'] = '3*qr%3v27!)_cfml*uffm3n9glfdy%16!#4wm5@8t)rc@do_z^'
os.environ['DJ_DEBUG'] = 'TRUE'
os.environ['DJ_DB_ENGINE'] = 'django.db.backends.mysql'
os.environ['DJ_DB_NAME'] = 'cmplxsys'
os.environ['DJ_DB_USER'] = 'root'
os.environ['DJ_DB_PASSWORD'] = 'm@candch33s\#'
os.environ['DJ_DB_HOST'] = '127.0.0.1'
os.environ['DJ_DB_PORT'] = '3306'
os.environ['DJ_STATIC_ROOT'] = '/users/c/m/cmplxsys/www-root/db/complex-systems-database/mysite/static'

import django.core.handlers.wsgi

_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
    # environ['PATH_INFO'] = environ['SCRIPT_NAME'] + environ['PATH_INFO']
    result = _application(environ, start_response)
    # yield '%s'  % result
    # f = open("/users/c/m/cmplxsys/www-root/db/result.txt","w")
    # f.write(result)
    # f.close()
    result['Access-Control-Allow-Origin'] = "*"
    return result

request_handler = application

