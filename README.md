# Full Stack Developer Nanodegree Project 1: Logs analyser

## Introduction

This is project one of the Udacity Full Stack Nanodegree: a terminal-based interactive log analyser for a Postgres database that represents a fictional news website. This log analyser queries the database to answer the following three questions:

* What are the top three most accessed articles?
* Who are the most popular authors?
* On what days did error requests amount to more than 1% of requests on that day?

This project is written with Python 3 in mind. It is untested in Python 2.

## Status
_Complete. Successfully graded._

## How this project is structured

This is a small project and all source code of interest is in the src directory. The main Python script is `main.py` with `newsdb.py` being a supporting data access module. The SQL queries used to analyze the database are located in the src/sql directory. In keeping with Python best practises, project dependencies are isolated into their own environment via `virtualenv`.

## Setting up

You can either set this project up using your own UNIX-like environment, by using Udacity's preconfigured Vagrant/VirtualBox VM.

### Using your own environment

If you're using your own UNIX-like environment, you'll need to satisfy the following prerequisites in order to run this project.

* Python 3
* Pip
* virtualenv
* Git
* The `newsdata.sql` script supplied by Udacity. [Download it](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).

How you go about satisfying these requirements depends on what UNIX environment you're using. Some distributions already come with Python 3 and Pip installed, while others come with none of the above tools. Consult your platform's package manager for determining how to best satisfy these requirements.

Once you have satisfied the above requirements, follow the instructions below.

1. Set up the Postgres database using `psql`:
    1. Create a database "news": `create database news;`.
    2. Run the newsdata.sql script to add the tables and populate the database. Depending on your setup, you may need to use the `sudo -u` command alongside your postgres superuser (usually just "postgres") to run the script, e.g. `sudo -u postgres psql -d news -f newsdata.sql`.
    3. _The following are optional steps which may be required if your Postgres security setup requires accounts to connect with passwords:_
        1. Create a user "newsuser" (note down the password): `create user newsuser with encrypted password '<fill>';`.
        2. Connect to "news" and grant "newsuser" full access to "news" (from `psql`, you can do this with `\connect news`):
            * `grant all privileges on database news to newsuser;`
            * `grant all privileges on all tables in schema public to newsuser;`
            * `grant all privileges on all functions in schema public to newsuser;`
2. Clone the repository and `cd` into the `src` directory.
3. Create a Python 3 virtual environment: `virtualenv env`.
4. _Optional -- dependent on your Postgres security setup as described in step 1.3_. Create a single-line file titled "password" and enter the password for "newsuser" in it (ensure there are no new lines in this file, as this can cause authentication failures when connecting to the database). If this file does not exist, the log analyser will attempt to connect to the "news" database with no specific credentials, which will fail if your Postgres environment is set up to require passwords.
5. Activate the Python virtual environment: `source env/bin/activate`.
6. Install dependencies: `pip install -r requirements.txt`.
7. Run the main script via the terminal: `python main.py` or `main.py` (ensure that `main.py` is executable if using the latter command: `chmod +x main.py`).
8. Follow the prompts.

### Using Udacity's Vagrant VM

Setting up on Udacity's Vagrant VM does not require creating the "news" database, the database user "newsuser", or creating a password file. However, the VM does not have `virtualenv`, so this will need to be installed. Follow the instructions below.

**Please note that the Udacity Vagrant VM as at commit `b36afe` does not appear to install `psycopg2` correctly for Python 3. As such, running the Python script outside of the `virtualenv` (e.g. `python3 main.py`) will generate import errors. You can install `psycopg2` for Python 3 using the following command: `pip3 install psycopg2-binary --user`**.

1. [Install VirtualBox](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1) for your platform. You must use VirtualBox 5.1, as newer versions do not work with Vagrant.
2. [Install Vagrant](https://www.vagrantup.com/downloads.html) appropriately for your platform.
3. [Fork and clone locally](https://github.com/udacity/fullstack-nanodegree-vm) the Udacity VM on GitHub.
4. From Bash:
    1. `cd` into the `vagrant` directory in the Udacity repository you cloned in the previous step.
    2. Run `vagrant up`. This will set up the VM, but it may take quite a while to do so. Consider a :coffee: or twelve.
    3. Run `vagrant ssh` to SSH into the VM once it's set up.
    4. Copy the newsdata.sql script into your Vagrant shared directory and run it with `psql -d news -f vagrant/newsdata.sql`.
    5. Install virtualenv: `sudo apt install virtualenv`.
    6. Clone this repository and `cd` into the `src` directory.
    7. Create a Python 3 virtual environment: `virtualenv -p python3 env`.
    8. Activate the Python virtual environment: `source env/bin/activate`.
    9. Install dependencies: `pip install -r requirements.txt`.
    10. Run the main script via the terminal: `python main.py` or `main.py` (ensure that [main.py](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/main.py) is executable if using the latter command: `chmod +x main.py`).
    11. Follow the prompts.
    12. Once you're finished with the log analyser, press 'q' to quit out of the main loop. You can then deactivate the Python 3 `virtualenv` with `deactivate` and exit the SSH shell with `exit`. Running `vagrant halt` shuts down the VM.
