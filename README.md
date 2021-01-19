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
python manage.py collectstatic
```

## Django + Rapidweaver

We've managed to combine a database site with Rapidweaver (or any static HTML generator) as a template engine.
How does this work?

1. All requests that aren't for js, css, png, jpg files are routed through the Django site (see `.htaccess`).
2. Django's `mysite/urls.py` parses URLs and any that don't match a few specific URLs are sent to the "rapidweaver" view.
    - Those that do match URLs from the `cmplxsys` app are sent there. See `cmplxsys/urls.py`
    - The ones matched by `mysite/urls.py` have the data injected, with templates in `templates/` and as follows.
3. The rapidweaver view considers these pages as templates without any data passed into them.
4. Looking for templates in `templates/`, the "folder" `mysite` is a relative, symbolic link back up into the `templatery` directory in `www-root`.


## Editing the templates

The HTML templates are in (1) the `templates/` directory of the site.

# User guide

The admin site can be reached here: [http://vermontcomplexsystems.org/admin/](http://vermontcomplexsystems.org/admin/).

## Database model

## API

## Adding/updating people

## Adding/updating press

## Adding/updating papers

# Notes

Basics:
- The main URL is [vermontcomplexsystems.org](vermontcomplexsystems.org).
- The DNS is UVM's nameservers (see `tools/nameservers.png`).
- The documentation that I have for end users in the `tools/` directory.
- The code for the database is this repo.

The database (and the rest of the site) is all hosted on UVM's silk server, here's my settings from `.ssh/config` for that server:

```
Host cssilk
    User cmplxsys
    Hostname w3.uvm.edu
    IdentityFile ~/.ssh/id_rsa
```

## UVM Servers

I know of two main server systems that UVM supports, the silk service (which is newer and by request, I think) and the zoo server, which is the default web space that everyone gets.
The site was originally a wordpress site on the zoo server, which accessed the database on the silk server (via web API requests) and now everything is on the silk server.
Of course, you'll have log in with the password or copy you own ssh key up there as well (use `ssh-copy-id`).

## Design

On the design of the site --- originally we had this database set up on a different server than silk (external server), moved it to silk to bring things onto UVM servers. On silk, it was set up to be accesses via API requests from the wordpress site (which had JS templates pulling in the data, and building stuff within pages in the wordpress site (using a jinja2-like template in JS called `plate.js`)).
To get away from wordpress, the main site was rebuilt using a web design tool called RapidWeaver, in which Professor Dodds rebuilt the whole site (as you see it now).
RapidWeaver is a website design tool that exports a static website (exports a folder with all the HTML, CSS, JS files that can be hosted for the site).
To use the rapidweaver site in conjunction with this dynamic database backend (built in Python's Django framework), I had the Django site accept all of the web requests, and use the static rapidweaver assets as templates themselves.
So, Django is sitting in front of the whole rapidweaver site, and serves everything.
This is potentially easier than having JS in the rapidweaver site that queries the database, because we can render everything with the full power of Django's templating syntax (and don't have to write the API).
The Django site is served through a WGSI connected on the Silk server, which means Silk's apache (or whichever web server it's running) actually executes the python code. It does this through the wsgi.py file.

I just looked and the Django site is actually using UVM's mysql database (and I've included that password below).
In looking at the code, I now see that the password is this public github repo: https://github.com/andyreagan/complex-systems-database/blob/master/mysite/settings.py#L134
so that's something to fix.

The rapidweaver site that Django uses on silk server is at /users/c/m/cmplxsys/www-root/templatery, and Django sees this in it's templates because there is a symbolic link here: https://github.com/andyreagan/complex-systems-database/tree/master/templates that is called "mysite" and it points to "../../../templatery" (a relative path).
If you look at mysite/urls.py, you'll see where all of the routing happens. It passes off the apis defined in cmplxsys/urls.py (which does some passing to cmplxsys/api.py), to some page views that act like APIs, and then to the rapidweaver view which wraps the templates there.

Because the rapidweaver site is rendered by django, we can use the template inheritance inside of the rapidweaver html pages.
So that means inside of those pages, we can include other templates that are rendered by Django, like the lists of people and press.
Those are templates that are rendered inside of the rapidweaver pages.

## Passwords

Here is what I have written down for passwords (I have some others ones, but I'm 99% sure the others are defunct, the last two here are likely unnecessary).

uvm_webdb_cmplxsys:
  desc: uvm webdb sql
  username: cmplxsys_admin
  password: ****
complex_systems_silk_database_admin:
  desc: complex systems silk database admin
  url: cmplxsys.w3.uvm.edu/db/admin
  username: cmplxsys
  password: ****
uvm_account_cmplxsys:
  desc: uvm account
  username: cmplxsys
  password: ****
wordpress_cmplxsys:
  desc: complex systems wordpress
  url: uvm.edu/~cmplxsys/wp-admin
  username: admin
  password: ****

## Database model

Now about how the database itself is structure.
The whole thing is laid out in the `cmplxsys/models.py`, which defines all of the database models.
Basically, we have objects for "people", for "press", for "papers", etc and all of those link in a variety of ways.
For example, many "people" objects can be linked to a "paper", with an ordering of authorship. And a "paper" can also be linked to "press" (as can individual "people", though we can also get the list of people on a paper that is linked to press by following press -> paper -> authors)
I have a diagram for the structure of the database, or how we designed it anyway, and I'll see if I can find that and attach it (the one you want is `tools/cmplxsys-database.png`).



## API

Here's an example of one of the API calls you'll find in cmplxsys/api.py that is using the "tastypie" API framework to build out these responses:
press_all = fields.ManyToManyField('cmplxsys.api.BasicPressResource',lambda bundle: Press.objects.filter(papers=Paper.objects.filter(authors=bundle.obj)).order_by('-date'),full=True,null=True)
What this does is gets all the papers for a person, and then all the press associated with those papers (if you read this from the innermost call outward).

## More notes

Here are some notes that I passed to Professor Dodds about which templates needed to go in which pages to make it work:

they all just need these two snippets in the template, and it will all work as above when a new version of the rapidweaver site to templatery:

    {% include "people-list-generic.html" %}
    {% include "person-page.html" %}

those snippets will need to go in the index for core team, associated faculty, etc
i.e., in `.../core-team/index.html` and all of the other folders

I had converted a number of inner templates to use CSS layout rather than HTML tables, but the list pages still use tables. The individual person page doesn’t. I need to do the CSS for the list pages.

