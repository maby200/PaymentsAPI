# PaymentsAPI


Hi, this is my first API, I worked out a lot :relieved:

## Cloning
If you want to clone this first:

```bash
$ git clone git@github.com:maby200/PaymentsAPI.git
```
## Required packages
For this repo you'll need the packages listed in `requirements.txt`.\
Dont rush into the installation! 
1. First, create a new environment
```bash
$ virtualenv env
```
2. Activate the environment (I'm using Linux)
```bash
$ source env/bin/activate
```
3. (notice the `(env)` which means your environment is active)\
Now we're ready to install the packages in `requirements.txt`
```bash
(env) $ pip install -r requirements.txt
```
4. With that done, you're set up to run the project
```bash
(env) $ python manage.py runserver
```
## Creating an account
Once your project is running, open it in your browser with the url: `http://127.0.0.1:8000/`. \
I recommend you to:
1. Go and create an account in: `http://127.0.0.1:8000/users/signup/`
2. Then go to `http://127.0.0.1:8000/users/login/`, login with the email and password you've chosen and
3. Copy the `access` token it apears on the page after successfuly login.

You can use Postman, or Thunder Client extension in VSCode to do the GET and POST, unfortunatelly you wont be able to do the entire CRUD since you are not admin.

For a better experience, you can go to `http://127.0.0.1:8000/api/schema/redoc/` or `http://127.0.0.1:8000/api/schema/swagger-ui/`


## Useful links:
- [How create trigger in Django Rest Framework to change booleanfield?](https://stackoverflow.com/questions/52439024/how-create-trigger-in-django-rest-framework-to-change-booleanfield)

- [API versioning in-depth](https://gearheart.io/articles/api-versioning-with-django-rest-framework/)

- Book: [DJANGO for APIs](https://djangoforapis.com/)
