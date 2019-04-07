# Full Stack Developer Nanodegree Project 1

## What is it

This repository contains my source code for the first FSND assessable project.

## How to set it up

PostgreSQL and Python (including **Pip** and **virtualenv**) are required.

* Clone the repository and `cd` into the **src** directory;
* Create a Python 3.6.7 virtual environment: `virtualenv env`;
* In PostgreSQL and using PSQL:
  * Create a database **news**: `create database news;`,
  * Create a user **newsuser** (note down the password): `create user newsuser with encrypted password '<fill>';`,
  * Connect to **news** and grant **newsuser** full access to **news**:
    * `grant all privileges on database news to newsuser;`
    * `grant all privileges on all tables in schema public to newsuser;`
    * `grant all privileges on all functions in schema public to newsuser;`
* Create a single-line file titled **password** and enter the password for **newsuser** in it (ensure there are no new lines in this file, as this can cause authentication failures when connecting to the database);
* Activate the Python virtual environment: `source env/bin/activate`;
* Install dependencies: `pip install -r requirements.txt`;
* Run the main script via the terminal: `python main.py` or `main.py` (ensure that [main.py](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/main.py) is executable if using the latter command: `chmod +x main.py`).
* Follow the prompts.

## How this project is structured

All source code is located in the src directory, and the main script is `main.py`. The SQL queries used by the script are located in the src/sql directory. `newsdb.py` is a supporting data access module. In keeping with Python best practises, project dependencies are isolated into their own environment via **virtualenv**. The requirements file is [requirements.txt](https://github.com/yottaawesome/fsnd-project-1/blob/master/src/requirements.txt).