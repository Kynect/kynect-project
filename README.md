# Kynect

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

a) Download the Installer from EnterpriseDB (Most likely)  
b) Run the Installer as Administrator  
c) Go to Control Panel -> System and Security -> System -> Advanced System Setting --> Environment Variables  
d) Edit Path and add 2 things:  
	i) C:\Program Files\PostgreSQL\9.6\bin  
	ii) C:\Program Files\PostgreSQL\9.6\lib  
e) Run in Powershell:
```sh
> psql -U postgres
```
f) Insert password

- Once accessed, setup the database with the commands below:
```sh
postgres=# CREATE DATABASE testdb;
postgres=# CREATE USER *username* WITH PASSWORD *password*;
postgres=# GRANT ALL ON DATABASE testdb TO *username*;
postgres=# \c testdb;
testdb=# \q
```
**2) Install Python 3.5 for System**

**3) Create a Virtual Environment (Virtualenv):**

- Install Virtualenv (For Windows, just type: *pip install virtualenv*)
- Create virtual environment with python 3.5 called kynect using below commands:

Ubuntu:
```sh
$ virtualenv -p /usr/bin/python3.5 venv_kynect
```
Windows:
```sh
> virtualenv venv_kynect
```
**4) Install Necessary Packages in Virtual Environment:**

- Enter virtual environment using command:

Ubuntu:
```sh
$ source bin/activate
```
Windows (As Administrator in Powershell):
```sh
> Set-ExecutionPolicy RemoteSigned				// Changes Systems Execution Policy
> .\activate									// Run in /Scripts
```
- Install Django via pip using below commands:

Ubuntu:
```sh
$ pip install django
```
Windows:
```sh
> pip install django
```
- If you get a message "*Error loading psycopg2 module: No module named 'psycopg2'*", Run:  
Ubuntu:
```sh
$ pip install psycopg2
```
Windows:
```sh
> pip install psycopg2
```
**5) Clone the Git Repository** 

- Download Git for Windows
- If you need to set up Git, run these commands to set it up:
Ubuntu:
```sh
$ git config --global user.name "username"
$ git config --global user.email "user@example.com"
```
Windows:
```sh
> git config --global user.name "username"
> git config --global user.email "user@example.com"
```
- Now, within the root directory of your virtual environment run the following:

Ubuntu:
```sh
$ git clone https://github.com/EKOTracking/kynect-project.git
```
Windows:
```sh
> git clone https://github.com/EKOTracking/kynect-project.git
```
**6) Run the server:**

- Now you can run the server by entering the directory containing 'manage.py' and running the following:

Ubuntu:
```sh
$ python manage.py runserver
```
Windows:
```sh
> .\manage.py runserver
```
### Access the Website by navigating to *localhost:8000* in your web Browser!

**Testing**

Coming Soon