# Kynect

### Developing
In order to setup your environment to run the development server and test the application, or to contribute to the project, follow the instructions below.

**1) Install and Set Up PostgreSQL Database:**

- Install PostgreSQL and Necessary Libraries for PostGIS(GEOS, PROJ.4, GDAL, PostGIS):

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
&nbsp;&nbsp;&nbsp;&nbsp;i) C:\Program Files\PostgreSQL\9.6\bin  
&nbsp;&nbsp;&nbsp;&nbsp;ii) C:\Program Files\PostgreSQL\9.6\lib  
e) Run in Powershell:
```sh
> psql -U postgres
```
f) Insert password

- Once accessed, setup the database with the commands below:
```sh
postgres=# CREATE DATABASE testdb;
postgres=# CREATE USER *username* WITH PASSWORD '*password*';
postgres=# GRANT ALL ON DATABASE testdb TO *username*;
postgres=# \c testdb;
testdb=# \q
```

- Next, install PostGIS:

Ubuntu:
```sh
$ sudo apt-get install -y postgis postgresql-9.6-postgis-2.3
```
Windows:

a) From within the Application Stack Builder (to run outside of the installer, Start ‣ Programs ‣ PostgreSQL 9.x)
b) Select PostgreSQL Database Server 9.x on port 5432 from the drop down menu
c) Next, expand the Categories ‣ Spatial Extensions menu tree and select PostGIS X.Y for PostgreSQL 9.x.
d) After clicking next, you will be prompted to select your mirror, PostGIS will be downloaded, and the PostGIS installer will begin. Select only the default options during install (e.g., do not uncheck the option to create a default PostGIS database).

- Then install the necessary libraries for PostGIS:

Ubuntu:
```sh
$ sudo apt-get install binutils libproj-dev gdal-bin
```
Windows:

a) First, download the OSGeo4W installer, and run it
b) Select Express Web-GIS Install and click next.
c) In the ‘Select Packages’ list, ensure that GDAL is selected; MapServer and Apache are also enabled by default, but are not required by GeoDjango and may be unchecked safely.
d) Click Next
e) Modify Windows environment

In order to use GeoDjango, you will need to add your Python and OSGeo4W directories to your Windows system Path, as well as create GDAL_DATA and PROJ_LIB environment variables. The following set of commands, executable with cmd.exe, will set this up:

```sh
set OSGEO4W_ROOT=C:\OSGeo4W
set PYTHON_ROOT=C:\Python27
set GDAL_DATA=%OSGEO4W_ROOT%\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%PYTHON_ROOT%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
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

**4) Clone the Git Repository** 

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

**5) Install Necessary Packages in Virtual Environment:**

- Enter virtual environment using command:

Ubuntu:
```sh
$ source bin/activate
```
Windows (As Administrator in Powershell):
```sh
> Set-ExecutionPolicy RemoteSigned				// Changes Systems Execution Policy
> .\Scripts\activate							// Run in Root of Virtual Env.	
```
- Install all dependencies from our requirements.txt (Move into /kynect-project):

```sh
$ pip install -r requirements.txt 
```

**6) Grant Access / Priviliges to Super User to Set Up PostGIS:**

- First run below code to create a superuser login for gaining administraive priviliges in django admin site (Follow Instructions):
```sh
$ python manage.py createsuperuser
```

- Next, change user to 'postgres' and Alter Roles to created user in order to have superuser priviliges.
```sh
$ sudo su - postgres
$ psql
```
```sh
postgres=# ALTER ROLE *username* WITH superuser;
postgres=# ALTER ROLE *username* WITH createrole;
postgres=# ALTER ROLE *username* WITH createdb;
postgres=# ALTER ROLE *username* WITH replication;
postgres=# ALTER ROLE *username* WITH bypassrls;
```

- Within Postgres, type below to view a description of the users and their priviliges and exit when done:
```sh
postgres=# \du
postgres=# \q
```

- Return to being signed in as regular user by logging out of postgres user:
```sh
$ exit
```

- Now migrate all changes in models in order to keep models up to date and create extension for 'PostGIS' on 'testdb' database:
```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

- Login as *username* to 'testdb' database in postgres to confirm extension is implemented:
```sh
$ psql testdb

testdb=# \dx
...
testdb=# \q
```

**7) Run the server:**

- Now you can run the server by entering the directory containing 'manage.py' and running the following:

```sh
$ python manage.py runserver
```

### Access the Website by navigating to *localhost:8000* in your web Browser!

**Testing**

Coming Soon