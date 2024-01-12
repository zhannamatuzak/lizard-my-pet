# Lizard Is My Pet

This Django project functions as a specialized blog designed for individuals contemplating the idea of adopting a lizard as a pet. It caters not only to those in search of essential information for decision-making but also to experienced lizard owners eager to share their firsthand experiences. Owners are invited to share insights into various aspects of daily life with their lizard, including preferred food choices, potential size and growth, lifespan, and even unique names for these captivating pets. The administrator provides visitors with posts about various lizard species, offering a comprehensive overview to assist them in making informed decisions. Simultaneously, visitors who have a lizard as a pet can actively contribute by sharing their own experiences in the experience (comments) section below each post. Reading about the experiences of others serves as a valuable resource for decision-making too. Only registered users have access to submit their experiences across all posts.

![responsive mockup]()

[Link to live site]() 


## Deployment

This project was deployed using [Heroku](https://heroku.com/), [Cloudinary](https://cloudinary.com/), [ElephantSQL](https://www.elephantsql.com/) and [Whitenoise](https://whitenoise.evans.io/en/latest/). 


#### Installing libraries

- Install **Gunicorn** (server used to run Django on Heroku): ``pip3 install django gunicorn``
- Install **pyscopg2** (connects to PostgreSQL): ``pip 3 install dj_database_url pyscopg2``
- Install **Cloudinary** (host static files and images): ``pip3 install dj3-cloudinary-storage``
- Install **Whitenoise** (prevent issues with Heroku not rendering custom stylesheet): ``pip3 install whitenoise``

#### Getting set up

- Create **requirements.txt file** (keeps track of the modules and packages used in your projects): ``pip3 freeze --local > requirements.txt``
- Create **new Django project**: ``django-admin startproject lizardmypet .``
- Create **blog app** (name of the repo will be "blog"): ``python3 manage.py startapp blog``
- Create **add blog app to installed apps** (the blog app needs to be added to the list of installed apps in the settings.py)
- Migrate **changes to the database** (when there is a new app, migrations are automatically created): ``python3 manage.py migrate``
- Run **project** (It will show the error states your specific host. Copy and paste it into the settings.py file ALLOWED_HOSTS.): ``python3 manage.py runserver``

If everything works, it will appear this:


I had to rename my Django project. 
Here are the steps to change the name:

- Rename the Project Directory;
- Rename the root directory of your Django project to the new project name;
- Update manage.py and wsgi.py Files;
- Inside the project directory, there are files named manage.py and wsgi.py. Update these files to use the new project name.
- Update the settings.py File;
- Open the settings.py file inside your project folder and change the ROOT_URLCONF to point to the new project name.
- Update database tables to reflect the new project name. You can do this using Django migrations.
``python manage.py makemigrations``
``python manage.py migrate``
- Update the ASGI_APPLICATION (if applicable);
- Update ASGI_APPLICATION setting to use the new project name.



[Django Secret Key Generator](https://miniwebtool.com/django-secret-key-generator/)


## Credits

#### Code

 1. [MinValueValidator](https://stackoverflow.com/questions/44022056/validators-minvaluevalidator-does-not-work-in-django) -  MinValueValidator was used to help validate the max_size, lifespan, proce_from, price_to fields in the `LizardModel` in Models.py file, to ensure that the values of max_size, lifespan, proce_from, price_to are greater than or equal to 1.
 2. []() -  
 3. []() -
 4. []() - 