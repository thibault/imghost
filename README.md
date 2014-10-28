A simple image hosting thing
============================

For hipsters with static site generators…


Disclaimer
----------

NAME was developped in two lazy afternoons, because I needed it. It was only
released because other people showed interests to him, and is provided "as is".


What is it?
-----------

NAME is a simple software you can install in your server to self host your images.

It is written in Django.


Features
--------

 * Upload images from the Web or your hard drive
 * Automatic thumbnail generation
 * Basic meme creation
 * Media files will be served directly with Nginx


Installation
------------

We recommand creating a dedicated virtual machine to host NAME.

 * create a new user
 * clone the repository
 * create a virtualenv
 * install requirements
 * install and configure nginx and supervisor (see samples in the `docs` directory)
 * syncdb + migrate


TODO
----

 * Rewrite this crap in an honorable way
