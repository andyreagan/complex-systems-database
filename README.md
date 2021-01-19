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

## Events model

From various emails, Kelly G tried to add a database model for events but got an error making the migration.
Based on this,
I'm not sure what the current state of the site is.

## More notes

Some documentation is there. In short, the way the site works now is that Django receives all web requests that don't match a set of filters via an apache config file (all requests that are in folders rw_common or index_files are sent through the templatery folder which holds the rapidweaver site, as well as all requests that are for files in folders "templatery" or "static" that match extensions js, css, png, jpg are routed in templatery). Those sets all get served by apache right from rapidweaver.
Everything else, including the html pages produced by rapidweaver, and sent through Django.
Django renders these html templates as-if they are Django templates, so tags like {% include people.html %} work from Django's rendering of the html (that tag will tell Django to go pull in people.html and stick it in). Some of these HTML pages, like people.html, are not HTML files from rapidweaver but rather templates in the Django site that load from the people/paper/press database. These can also filter to an individual person, and it's how the people pages are rendered now, Django pulls the person name from the URL and uses that in rendering the Django-side template (again, this is happening via the "include" inside of the rapidweaver html file).

I wrote this up a bit nicer, perhaps, in the README on github.

Anyway, that's how it works now, to use a database to power everything.
The database has models for people, press, papers, and a lot of other things that can connect. Here are all of the models and fields: https://github.com/andyreagan/complex-systems-database/blob/master/cmplxsys/models.py
There are various connections defined between each, like a paper can link to multiple people (and the paper page can pull in those people's names and affiliations...likewise the people page can pull in all paper's that they're linked from).
A lot of options are there now, I see:
- Person
- Position (linked to person)
- Project (linked to 0 or more person)
- Funding (linked to 0 or more person, linked to 0 or more project)
- Course (linked to 0 or more person as teacher, and linked to 1 or more person as student)
- Paper (linked to 0 or more person as author, linked to one of more classes)
   - Order, defined by the person and paper link (to order a list of papers by person)
- Press (linked to 0 or more paper, projects, and people)
- Event

That web allows the people to list all their papers, courses taught, and even students since it's all linked together.
Django builds those people pages (with their paper lists, etc) and the paper pages (with the author list from the links).
It also exposes and API, which is an easy bonus with Django given that it has the database structure to build the templated people, etc html pages.
I use the API to power my own CV actually, because it pulls the papers with nice images for each...but I'm probably the only one who does so (because I'm the only one who knows how to use it!).

All food for thought at this point.
With the difficulty of managing Django and all of this on the shared server, I think that either we rip out this whole database system and do it manually in rapidweaver OR move it to a proper server that's easier to manage.
It does feel like this 80% of the functionality for a really awesome site with all of the linking, but it's missing that really nice way to edit the pages themselves through Django and also missing that documentation on how to use the backend to manage all of the things (people, etc).

## More

Quotes from Scott at UVM

> Sites in general should not be down for particularly long.  It is possible this particular one might be a special case.
>
> First, it appears you symlinked the document root to www-root/, which broke during the migration process.  (In general, please don’t do that.). For the moment, I swapped out the empty vermontcomplexsystems.org-root/ directory created during migration for a symlink to www-root/ link you had on the old server.
>
> Secondly — and potentially a bigger deal — this appears to be a Python Django based site.  Python on silkv1 was 2.6; the oldest supported on silkv2 is 2.7.  The site also appears to be configured to launch the app as a CGI script with various rewrites in .htaccess related to your static resources.  Python CGI is not supported on silkv2 as it is not particularly common anymore; instead, silkv2 uses an app server for most languages other than PHP.  If you take a look at. https://silk.uvm.edu/manual/python/ and can explain how your static resources are organized in relation to your launch script, I could assist with .silk.ini configuration describing what the app server should do, though it is possible you may still have Python 2.6 -> 2.7 related issues you would need to address.

---

Hey Scott, I'm going to see if I can follow the instructions to get it back online now.

Looking at the documentation, it looks like things have been modernized in a good way! I shouldn't have too many questions.

Yes, working with python2.6 and cgi and embedding a rapidweaver site as django's template all resulted in a somewhat arcane setup (though, it ran reliably). Let alone installing django in virtualenv to be used by the cgi (distant memories by now, fortunately).

---

Scott, looking more now.

Can you configure a vanilla .silk.ini:

[app]
type = python
root = myapp
document-root = public
startup-script = wsgi.py

Just put it in www-root, and do step 2:

Notify SAA that you have made these changes, so that an app server can be configured for you and the web server can be set up to speak with it.

That would allow me to keep plugging away on it.

---

I'll be able to look at it again later tonight, the basic idea here is that we have a Django site that loads some other files at templates.
Nothing crazier than that.

The django site is in www-root/db/complex-systems-database, and we just need that site to run.

If the site runs and gets a python error, I can work on it from there.

---

I've done a bunch of things to clean up:
removed phptemp/
rename cmplxsys-wordpress-copy to cmplxsys-wordpress-copy-2015-05-15
rename www-root/2017-11-10wordpress to cmplxsys-wordpress-copy-2017-11-10
removed get-pip.py
removed node_modules/
rename www-root/.old-wordpress-site-backup to cmplxsys-wordpress-copy-2015-05-20
From the site directory (www-root/db/complex-systems-database), I did the following
rm package-lock.json
rm -rf node_modules/
rm -rf dotenv
None of those were tracked in version control and I don't know what they were doing there.
There were also many changes to the site that weren't committed to git (or pushed to github), I did both with these two commits:
https://github.com/andyreagan/complex-systems-database/commit/e0936e6c396926619ccdef473bf78759eef8f51b
https://github.com/andyreagan/complex-systems-database/commit/325aebd0103e009d7e75431dd766b3ce58dd4f33
Scott, the site runs from /users/c/m/cmplxsys/www-root/db/complex-systems-database by running

python2.7 manage.py runserver

so this means that we won't have a problem with the 2.6 -> 2.7.

I actually documented the setup of the site pretty well in the first two sections here:
https://github.com/andyreagan/complex-systems-database

What remains to be done? Scott, I need you to configure the app with the centralized nginx. I think you'll need to modify the .silk.ini in the db/ directory.
I put one in www-root/silk.ini:

[python]
version = 2.7

I also put a starter in the www-root/db/ directory:

[app:vermontcomplexsystems]
type = python
root = complex-systems-database
document-root = ../static
startup-script = wsgi.py

The biggest other piece is the way .htaccess was working before. I wrote about that in the README in the github repo above, and the .htaccess itself is commented pretty well saying what's going on.
Will .htaccess files still work?
If we need to use nginx, I could write the equivalent nginx rules...
I'm not sure how else we'll manage routing the specific files types through templatery.


> The NGINX Unit app server assumes a more standard app directory layout than you are currently using, and thus I copied your wsgi.py into db/complex-systems-database/, made it executable, and symlinked to the static/ directory from inside that same directory.  I added the following to your .silk.ini:
>
> [app:vermontcomplexsystems]
> uri = /
> type = python
> root = db/complex-systems-database
> document-root = static
> startup-script = wsgi.py
>
> I then rebuilt the web server configuration for the host your account is on.  This results in the entire site except for files that exist in the document root being proxied to the app server, which would handle your application.  At this point, the app can be loaded into NGINX Unit by typing `silk-app app load vermontcomplexsystems.org`, which currently fails with the following error:
>
> django.core.exceptions.ImproperlyConfigured: Requested setting DEBUG, but settings are not configured. You must either define the environment variable DJANGO_SETTINGS_MODULE or call settings.configure() before accessing settings.
>
> I am not particularly familiar with Django, though it looks like your manage.py script loads what it’s talking about here while the wsgi.py doesn’t.  If you configure what it wants, you can run the command listed above again to try loading the app, and checking /usr/lib/unit-user-cmplxsys/unit.log if it fails.
>
> > The biggest other piece is the way .htaccess was working before. I wrote about that in the README in the github repo above, and the .htaccess itself is commented pretty well saying what's going on.
> > Will .htaccess files still work?
> > If we need to use nginx, I could write the equivalent nginx rules...
> > I'm not sure how else we'll manage routing the specific files types through templatery.
>
>
> Is there a particular reason you have things split across multiple directories?  As things stand currently, the .htaccess probably would not work.

I can't see the log file:

-bash-4.2$ tail /usr/lib/unit-user-cmplxsys/unit.log
tail: cannot open ‘/usr/lib/unit-user-cmplxsys/unit.log’ for reading: Permission denied

Here's the .htaccess, and we still need to do this, one way or another.
I was writing up a description but the comments here really say what it needs to do:

# push rw_common, index_files directories into templatery
RewriteRule ^rw_common/(.*)?$ /templatery/rw_common/$1 [QSA,NC,L]
RewriteRule ^index_files/(.*)?$ /templatery/index_files/$1 [QSA,NC,L]
# the next four route all js, css, jpg, png extensions
# that have neither the templatery or static folder
# into templatery
RewriteCond %{REQUEST_URI}  !^/templatery/.*$
RewriteCond %{REQUEST_URI}  !^/static/.*$
RewriteRule ^(.*?.js)$ /templatery/$1 [QSA,NC,L]
RewriteCond %{REQUEST_URI}  !^/templatery/.*$
RewriteCond %{REQUEST_URI}  !^/static/.*$
RewriteRule ^(.*?.css)$ /templatery/$1 [QSA,NC,L]
RewriteCond %{REQUEST_URI}  !^/templatery/.*$
RewriteCond %{REQUEST_URI}  !^/static/.*$
RewriteRule ^(.*?.jpg)$ /templatery/$1 [QSA,NC,L]
RewriteCond %{REQUEST_URI}  !^/templatery/.*$
RewriteCond %{REQUEST_URI}  !^/static/.*$
RewriteRule ^(.*?.png)$ /templatery/$1 [QSA,NC,L]
# and this rule then pushes everything else through the Django site!
RewriteRule "^([a-z_\-/0-9\ ]*)/?$" /db/wsgi.py/$1 [QSA,NC,L]

It's not so different than a "standard" deployment of a site where the dynamic part (django/flask/whatever) has to be exectued, and static files are served by the webserver itself. Here we have two static directories, static and templatery. This is how I typically deploy nginx for a website.

The only thing that's more complicated here are two rewrites of rw_common and index_files, and we also push certain file types to be served from templatery.

This is the error I see:

-bash-4.2$ silk-app app load vermontcomplexsystems.org
Adding new application vermontcomplexsystems.org/
Traceback (most recent call last):
  File "/usr/local/bin/silk-app", line 165, in app_load
    unit.save_application(new_app)
  File "/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/uvmsilk/nginx_unit.py", line 339, in save_application
    self._put_json(app.uri, app.to_json())
  File "/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/uvmsilk/nginx_unit.py", line 234, in _put_json
    r.raise_for_status()
  File "/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/requests/models.py", line 940, in raise_for_status
    raise HTTPError(http_error_msg, response=self)
requests.exceptions.HTTPError: 500 Server Error: Internal Server Error for url: http+unix://%2Frun%2Funit-user-cmplxsys%2Fcontrol.sock/config/applications/vermontcomplexsystems_org
During handling of the above exception, another exception occurred:
Traceback (most recent call last):
  File "/usr/local/bin/silk-app", line 214, in <module>
    app_handlers["{0} {1}".format(arguments['<command>'], subcmd)](arguments)
  File "/usr/local/bin/silk-app", line 168, in app_load
    print("{error} {detail}".format(error=err_json['error'], detail=err_json['detail']))
KeyError: 'detail'

Is there more traceback for the error you posted? Perhaps you could chown the log file so I can see it.

---

I've tried a few things.

I changed the .silk.ini to load mysite/wsgi.py, which is the correct entry point for a django app.
That old wsgi.py was written specifically to work with the old silk server.

I added a commented line in the .silk.ini to show how I typically load django with uWSGI, using the module directive.
Without seeing the errors, not much I can do from here.

Here's an example of a "typical" django uswgi config: https://github.com/andyreagan/hedonometer-vagrant-ansible-deployment/blob/master/site-settings/uwsgi/uwsgi_config

---

I tried adding the environment variable that django needs to the uwsgi script, but that seems to have broken it even worse...

---

> I fixed the file ownership on the log file.

---

Is there a way to pass environment variables to the app?

---

I now see in the log:

    2019/12/18 10:19:04 [alert] 109320#109320 Python failed to import module "mysite/wsgi"
    ImportError: Import by filename is not supported.

---

> I just realized that wasn’t documented (yet).  In your .silk.ini’s app section, anything starting with “env.” gets configured in NGINX Unit as an environment variable for your app.  For example:
>
>     [app:vermontcomplexsystems]
>     env.MYENV = some value
>
> results in the app having an environment variable MYENV with value “some value”.

---


Okay.

This is nginx unit docs for django:

https://unit.nginx.org/howto/django/

It says to specify the app using "module". This is actually what I'd tried... is this not supported on your end?

---

It also uses "module" for flask... https://unit.nginx.org/howto/flask/


---

That's just for python in general: https://unit.nginx.org/configuration/#configuration-python


---

I couldn't get it to escape a complex password appropriately:

-bash-4.2$ silk-app app load vermontcomplexsystems.org
Traceback (most recent call last):
  File "/usr/local/bin/silk-app", line 214, in <module>
    app_handlers["{0} {1}".format(arguments['<command>'], subcmd)](arguments)
  File "/usr/local/bin/silk-app", line 139, in app_load
    site_config = config_for_site(app_url.netloc)
  File "/usr/local/bin/silk-app", line 62, in config_for_site
    config = SiteConfig(username=arguments['--user'], hostname=host, site_root=site_root)
  File "/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/uvmsilk/site_config.py", line 38, in __init__
    self.load_preferences()
  File "/opt/rh/rh-python35/root/usr/lib/python3.5/site-packages/uvmsilk/site_config.py", line 53, in load_preferences
    config[s] = dict(config.items(s))
  File "/opt/rh/rh-python35/root/usr/lib64/python3.5/configparser.py", line 855, in items
    return [(option, value_getter(option)) for option in d.keys()]
  File "/opt/rh/rh-python35/root/usr/lib64/python3.5/configparser.py", line 855, in <listcomp>
    return [(option, value_getter(option)) for option in d.keys()]
  File "/opt/rh/rh-python35/root/usr/lib64/python3.5/configparser.py", line 852, in <lambda>
    section, option, d[option], d)
  File "/opt/rh/rh-python35/root/usr/lib64/python3.5/configparser.py", line 393, in before_get
    self._interpolate_some(parser, option, L, value, section, defaults, 1)
  File "/opt/rh/rh-python35/root/usr/lib64/python3.5/configparser.py", line 443, in _interpolate_some
    "found: %r" % (rest,))
configparser.InterpolationSyntaxError: '%' must be followed by '%' or '(', found: "%3v27\\!\\)_cfml*uffm3n9glfdy\\%16\\!\\#4wm5@8t\\)rc@do_z^'"

I tried single, double quotes, backslash escape...
I just made the password simpler.

---

Okay, I've just been trying things and got the django app to launch:

https://vermontcomplexsystems.org/

Now it's an error that maybe I can deal with?

I reinstalled all of the dependencies, that didn't seem to work.


---


Okay, I figured out the error. Google was no help!

Turns out I hadn't pinned the version of one of the dependencies, backing down versions until it worked did the trick.
Updated the requirements.txt.

Now we just have to figure out what to do about templatery serving.
If the webserver is no longer capable of these rules (and we can't define our nginx setting), I can handle it from within python (though this is ugly).


---

Scott, is it possible to have multiple document-root's?


---

Well it's not serving even the single static correctly:

https://vermontcomplexsystems.org/static/images/squirrel-standing-tp-10_400x400.png

This is getting passed through django...
Nginx should just be serving this directory.

---

Scott,

Can you serve the static/ directory without routing it through the app?

---

Scott?


---

I was able to get the site working by having Django serve the static assets.

This is less than ideal, in fact the documentation states (https://django-chinese-docs-16.readthedocs.io/en/latest/ref/contrib/staticfiles.html#django.contrib.staticfiles.views.serve):

    Warning
    This view will only work if DEBUG is True.
    That’s because this view is grossly inefficient and probably insecure. This is only intended for local development, and should never be used in production.

I'm still hoping that the static assets (files) can be served by the webserver.