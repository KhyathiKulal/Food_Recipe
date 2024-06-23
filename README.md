Django CRUD Operations Project :
This project demonstrates basic CRUD (Create, Read, Update, Delete) operations using Django.

Steps :
------
1. Create a Virtual Environment :
   * Using virtualenv :
     - Install virtualenv if you haven't already : pip install virtualenv
     - Create a virtual environment : virtualenv venv
     - Activate the virtual environment
        -- On Windows
        venv\Scripts\activate
        -- On macOS/Linux
        source venv/bin/activate
  * Using venv :
      - Create a virtual environment : python3 -m venv venv
      - Activate the virtual  :
         --On Windows
         venv\Scripts\activate
         -- On macOS/Linux
         source venv/bin/activate
        
2. copy the folder and move to it : cd Food_Recipe

3. Apply Migrations : python manage.py makemigrations
                      python manage.py migrate

4. Run the Development Server : python manage.py runserver
