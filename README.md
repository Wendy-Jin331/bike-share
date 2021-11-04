<h1>Django Project Documentation</h1>

Once all files are installed, 
use command python manage.py runserver and go to
http://localhost:8000/admin/login/?next=/admin/



<h2>Initial setup</h2>

1. Clone the repository
2. Open the project directory in commandline and setup venv

   ```
   $ cd pythonProject
   $ python -m venv .venv 
   $ source .venv/bin/activate
3. Install Django using command line
   ```
   $ python -m pip install Django
4. Install stdnum using command line
   $ python -m pip install python-stdnum
5. Run the web server
   ```
   $ python manage.py runserver
6. you can visit your Django project in your browser by using either http://127.0.0.1:8000 or http://localhost:8000

<h2>URLs</h2>

1. To open any url make sure web server is running 
       i) use command python manage.py runserver
      ii) go to URL http://localhost:8000/admin/login/?next=/admin/

     | Page Title      | URL  | Description |
     | :----:      |    :----:   |   :----: |
     | Site Admin      | http://localhost:8000/admin/login/?next=/admin/       | This is where we administrate the site.<br />Please login using below credentials <br /><br /><b>username</b>: team5 <b>password</b>: team5|
     | Bike Share App   | http://localhost:8000        | To launch project |
     | Paragraph   |         |  |