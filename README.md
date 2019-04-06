# Full Stack Developer Nanodegree Project 1

## What is it

This repository contains my source code for the first FSND assessable project.

## How to set it up

PostgreSQL and Python are required.

* Clone the repository and `cd` into it;
* Create a Python 3.6.7 virtual environment: `virtualenv env`;
* In PostgreSQL and using PSQL:
  * Create a database **news**: `create database news;`,
  * Create a user **newsuser** (note down the password): `create user newsuser with encrypted password '<fill>';`,
  * Connect to **news** and grant **newsuser** full access to **news**:
    * `grant all privileges on database news to newsuser;`
    * `grant all privileges on all tables in schema public to newsuser;`
    * `grant all privileges on all functions in schema public to newsuser;`
* Create a file **password** and enter **newsuser** password in it (this file is excluded from source control);
* Activate the Python virtual environment: `source env/bin/activate`;
* Install dependencies: `pip install -r requirements.txt`;
* Run the main script via the terminal: `python main.py`.
* Follow the prompts.
