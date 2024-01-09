## Deployment

This project was deployed using [Heroku](https://heroku.com/), [Cloudinary](https://cloudinary.com/), [ElephantSQL](https://www.elephantsql.com/) and [Whitenoise](https://whitenoise.evans.io/en/latest/). 


#### Installing libraries

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-cloudinary-storage``
- Install **Whitenoise** (prevent issues with Heroku not rendering custom stylesheet): ``pip3 install whitenoise``

#### Getting set up

- Create **requirements.txt file** (keeps track of the modules and packages used in your projects): ``pip3 freeze --local > requirements.txt``
- Create **new Django project** (a project name, do not call "blog"): ``django-admin startproject zentrumwest .``
- Create **blog app** (name of the repo will be "blog"): ``python3 manage.py startapp blog``
- Create **add blog app to installed apps** (the blog app needs to be added to the list of installed apps in the settings.py)
- Migrate **changes to the database** (when there is a new app, migrations are automatically created): ``python3 manage.py migrate``
- Run **project** (It will show the error states your specific host. Copy and paste it into the settings.py file ALLOWED_HOSTS.): ``python3 manage.py runserver``

If everything works, it will appear this:

## Credits

#### Code

 1. [MinValueValidator](https://stackoverflow.com/questions/44022056/validators-minvaluevalidator-does-not-work-in-django) -  MinValueValidator was used to help validate the max_size, lifespan, proce_from, price_to fields in the `LizardModel` in Models.py file, to ensure that the values of max_size, lifespan, proce_from, price_to are greater than or equal to 1.
 2. []() -  
 3. []() -
 4. []() - 