# Full Stack Developer Nanodegree Project 1: Logs Analyzer

## Introduction

This repository contains my source code for the first FSND assessable project. This project is a terminal-based interactive logs analyzer for a Postgres database that represents a fictional news website. This logs analyzer queries the database to answer the following three questions:

* What are the top three most accessed articles?
* Who are the most popular authors?
* On what days did error requests amount to more than 1% of requests on that day?

## Set up

You can either set this project up using your own UNIX(-like) environment, by using Udacity's preconfigured Vagrant/VirtualBox VM. You will need to satisfy the following prerequisites in order to run this project.

* Python 3;
* Pip;
* virtualenv;
* Git;
* The `newsdata.sql` script supplied by Udacity. A tarball version is available in `src/sql`, or you can [download it](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

How you go about satisfying these requirements depends on what UNIX environment you're using. Some distributions already come with Python 3 and Pip installed, while others come with none of the above tools. Consult your platform's package manager for determining how to best satisfy these requirements.

### Using your own evironment

1. Clone the repository and `cd` into the `src` directory.
2. Create a Python 3 virtual environment: `virtualenv env`.
3. In PostgreSQL and using PSQL:
    1. Create a database "news": `create database news;`.
    2. Create a user "newsuser" (note down the password): `create user newsuser with encrypted password '<fill>';`.
    3. Connect to "news" and grant "newsuser" full access to "news":
        * `grant all privileges on database news to newsuser;`
        * `grant all privileges on all tables in schema public to newsuser;`
        * `grant all privileges on all functions in schema public to newsuser;`
    4. Run the newsdata.sql script to add the tables and populate the database. Depending on your setup, you may need to use the `sudo -u` command alongside your postgres superuser (usually just "postgres") to run the script, e.g. `sudo -u postgres psql -d news -f newsdata.sql`.
4. Create a single-line file titled "password" and enter the password for "newsuser" in it (ensure there are no new lines in this file, as this can cause authentication failures when connecting to the database).
5. Activate the Python virtual environment: `source env/bin/activate`.
6. Install dependencies: `pip install -r requirements.txt`.
7. Run the main script via the terminal: `python main.py` or `main.py` (ensure that [main.py](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/main.py) is executable if using the latter command: `chmod +x main.py`).
8. Follow the prompts.

### Using Udacity's Vagrant VM

Getting set up on Udacity's Vagrant VM does not require creating the "news" database, the user "newsuser", or creating a password file. However, the VM has neither psycopg2 installed for Python 3 nor virtualenv; instructions for fullfilling these requirements are provided as part of the instructions below.

1. Install [VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) for your platform. You must use VirtualBox 5.1, as newer versions do not work with Vagrant.
2. Install [Vagrant](https://www.vagrantup.com/downloads.html) appropriately for your platform.
3. [Fork and clone locally](https://github.com/udacity/fullstack-nanodegree-vm) the Udacity VM on GitHub.
4. From Bash:
    1. `cd` into the `vagrant` directory in the repository you cloned in the previous step.
    2. Run `vagrant up`. This will set up the VM, but it will take quite a while to do so.
    3. Run `vagrant ssh` to SSH into the VM once it's set up.
    4. Install virtualenv: `sudo apt install virtualenv`.
    5. Install libpq-dev (required by psycopg2 for Python 3 for client-side development): `sudo apt install libpq-dev`.
    6. Clone this repository and `cd` into the `src` directory.
    7. Create a Python 3 virtual environment: `virtualenv env`.
    8. Activate the Python virtual environment: `source env/bin/activate`.
    9. Install dependencies: `pip install -r requirements.txt`.
    10. Run the main script via the terminal: `python main.py` or `main.py` (ensure that [main.py](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/main.py) is executable if using the latter command: `chmod +x main.py`).
    11. Follow the prompts.
    12. Press 'q' to quit the logs analyzer, and then exit SSH with `exit`. You can then close the Vagrant VM with `vagrant halt`.

## How this project is structured

All source code is located in the src directory, and the main script is `main.py`. The SQL queries used by the script are located in the src/sql directory. `newsdb.py` is a supporting data access module. In keeping with Python best practises, project dependencies are isolated into their own environment via **virtualenv**. The requirements file is [requirements.txt](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/requirements.txt).