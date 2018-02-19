# Complex Systems Database

Here's the code for the django site behind the UVM Complex Systems website at [http://www.uvm.edu/~cmplxsys/](http://www.uvm.edu/~cmplxsys/), up on github so I don't misplace it!

## Running the site

The site lives in `/users/c/m/cmplxsys/www-root/db/complex-systems-database`.
The `wsgi.py` router lives one level up from the site, at `/users/c/m/cmplxsys/www-root/db/wsgi.py`, and this is code is what is run by the server itself. It goes into the Django site and runs it, returning the completed request.

There is a single `.htaccess` file that pushes URLs through this `wsgi.py` file by putting it into the URL silently, and then the server notices the `.py` in the URL and runs the file.
The file is at  `/users/c/m/cmplxsys/www-root/.htaccess` and I've included a copy of that too.

Given the above two ^ statements, note that the `.htaccess.backup` and `wsgi.py.backup` files in this repo are hard linked to the actual files.

To run commands from the django api, a bit of trickery here.
There is no virtualenv.
Pip is installed locally, and used locally in the `~/.local` directory to install things there.
Python on the server is 2.6.6.

```sh
. ../.env
python manage.py collectstatic
```

## Editing the templates

The HTML templates are in the `templates/` directory of the site.

# User guide

The admin site can be reached here: [http://vermontcomplexsystems.org/admin/](http://vermontcomplexsystems.org/admin/).

## Database model

## API

## Adding/updating people

## Adding/updating press

## Adding/updating papers

