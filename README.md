Hey githubbers,

Here's the code for the django site behind the UVM Complex Systems website at [http://www.uvm.edu/~cmplxsys/](http://www.uvm.edu/~cmplxsys/), up on github so I don't misplace it!

To run commands from the django api, a bit of trickery here.
There is no virtualenv.
Pip is installed locally, and used locally in the ~/.local directory to install things there.
Python on the server is 2.6.6.

. ../.env
python manage.py collectstatic