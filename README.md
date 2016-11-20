# Location Tracker

### Developing
In order to setup your environment to run the development server and test the application, or to contribute to the project, follow the instructions below.

**1) Install and Set Up PostgreSQL Database:**

- Install PostgreSQL:

Ubuntu:
```sh
$ sudo apt-get install postgresql
$ sudo apt-get update
$ sudo apt-get install postgresql postgresql-contrib
$ sudo -u postgres psql
```
Windows:
```sh
- Enter Scripts Here
```
- Once accessed, setup the database with the commands below:
```sh
postgres=# CREATE DATABASE testdb;
postgres=# CREATE USER *username* WITH PASSWORD *password*;
postgres=# GRANT ALL ON DATABASE testdb to *username*;
postgres=# \c testdb;
testdb=# \q
```
**2) Install Python 3.5 for System**

**3) Create a Virtual Environment (Virtualenv):**

- Install Virtualenv
- Create virtual environment with python 3.5 called kynect using below commands:

Ubuntu:
```sh
$ virtualenv -p /usr/bin/python3.5 kynect
```
Windows:
```sh
- Enter Scripts Here
```
**4) Install Necessary Packages in Virtual Environment:**

- Enter virtual environment using command:

Ubuntu:
```sh
$ source bin/activate
```
Windows:
```sh
- Enter scripts here
```
- Install Django via pip using below commands:

Ubuntu:
```sh
$ pip install django
```
Windows:
```sh
- Enter Scripts Here
```
- For Ubuntu, if you get a message like so;

*Error loading psycopg2 module: No module named 'psycopg2'*

Run this command to install psycopg2:
```sh
$ pip install psycopg2
```
**5) Clone the Git Repository 

- Within the root directory of your virtual environment run the following:

Ubuntu:
```sh
$ git clone https://github.com/EKOTracking/PetManager.git
```
Windows:
```sh
- Enter scripts here
```
**6) Run the server:**

- Now you can run the server by entering the folder containing 'manage.py' and running the following:

Ubuntu:
```sh
$ python manage.py runserver
```
Windows:
```sh
- Enter scripts here
```

### Access the Website by navigating to *localhost:8000* in your web Browser!

**Testing**

Coming Soon