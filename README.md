AnimalApp
-
App which can be used to add and read data concerning animal health information 

by Łukasz Paciorek

-------------
Technologies used:
- 
- Python 3.8
- Django 4.0.1
- Pillow 9.0.0
- Database on sqlite3  

Configuration before first run:
- 
- configure virtual environment in Python:
    - virtualenv environment_name
    - install modules from requirements.txt (pip install -r requirements.txt)
- download master from repo
- django migrations(python3 manage.py makemigrations, python3 manage.py migrate)
- django create super user
- run django server(python3 manage.py runserver)

----------------
----------------
Main Features:  
-
- Adding resources like deworming remedies, remedies for ticks, vaccines, treatments and diseases, vet clinics
- Adding animal medical information like dewormings, remedies for ticks applications, vaccinations, treatments and diseases, weight, general information and animal main profile

Extra Features: 
-
- creating reports
- printing reports
- adding PDFs with medical stuff like blood tests, etc...

----------------  
----------------
Modules
-

Animals
-
- Animal profile
- Dewormings
- Treatments and diseases
- Remedies for ticks
- Vaccinations
- Weight
- General information


Resources
-
- Deworming remedies
- Treatments and diseases
- Remedies for ticks
- Vaccines
- Vet clinics


----------
Form of project:
- 
- Django templates