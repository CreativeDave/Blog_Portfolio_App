# Blog Portfolio App
> A dynamic blog, portfolio, and resume application enabling a user to customize nearly every detail of content through an intuitively designed backend interface. 

!['image'](./media/content/about.gif)
## About This Project

The intention behind this application was to enable anyone, regardless of coding experience, to choose a template and be able to create an engaing and unique website about their life and work. 

In choosing a programming framework, I wanted to challenge myself to use django in a real world example, and decided to use the Wagtail CMS because of its Page model's functionality. 

I treated this as if I were building a product for a client, taking myself through all the phases of the Project Management Life Cycle. All the way from initiation and planning on trello, to execution and testing, and finally deployment of a production build on Python-Anywhere. 

Overall, this was an incredible learning experience, and I had to challenge myself to learn much more than just django in the end. Depoying a production version of a website, even a medium-small sized one, can be fraught with unexpected challenges so I started a blog about some of my experiences and the pitfalls I had.

To give credit where credit is due, the initial bootstrap template I purchased for this project came from [www.Envato.com](https://envato.com/), by the author [beshleyua](https://themeforest.net/user/beshleyua). I chose to keep his signature in the CSS and JS files, as my modifications there were minimal. I did however, completely dissect the included static index.html and distribute it about the application to recieve django template tags and render content from my page models. The end result is a tree-structured multi-page dynamic web application, able to instantiate new pages as the user wishes, and with some neat class-specific functionality as well. 

*I hope you will continue exploring this repo to see what all went into building it, and I would be honored if you wanted to help me add more front-end themes.*

---

## Project Overview

There are 5 main django apps for this project.
  1. Portfolio - the project's namesake and default app. Only functionally contains:
     - settings files
     - project-wide static folder 
     - base.html & error templates
     - main urls routes
     - wsgi.py
  2. Home - the intial Wagtail migration. Functionally contains templates and models for 3 key pages:
     - Home / landing page
     - About Me page
     - Contact page 
  3. Blog - the blog application of the website. Contains templates and models for:
     - Blog Index page
     - Blog Post page
     - Blog Tag Index page
  4. Project - the projects/portfolio application of the website. Contains templates and models for:
     - Project Index page
     - Project pages
  5. ResumeCV - the resume application of the website. Contains the model and template for:
     - Resume page
    
### Getting Started

Eventually I will have a demo version hosted and provide login credentials. For now, clone the repo as you would ordinarily and use django's built in server to explore the site.

  1. Create a new virtual environment for this project in your directory of choice:  ``` $ python3 -m venv port_venv```
  2. Navigate into this directory and activate the environment ```source bin/activate``` or on Windows ```source Scripts/activate```
  3. Clone this repository ```git clone https://github.com/CreativeDave/Blog_Portfolio_App```
  4. install the requirements: ```pip install -r requirements.txt```
  5. Open the django_polls folder and migrate the database: ```python manage.py makemigrations``` then ```python manage.py migrate```
  6. Finally, start the django development server ```python manage.py runserver``` and open http://127.0.0.1:8000 in your browser.
  7. Use the username: *admin123* and password: *admin123* to login to the admin portal to modify questions and choices. You can reach the admin portal at http://127.0.0.1:8000/admin.

Let me know if you have any comments or questions.     
