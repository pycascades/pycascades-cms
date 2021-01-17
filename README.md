# PyCascdes CMS

The PyCascades website is deployed as a static website on **Netlify**. We switched in 2021 to using a Wagtail CMS running on Heroku as the **static site generator** to reduce the amount of coding required to make content changes.


## Setting up Locally

We are using [Poetry](https://python-poetry.org/) for local development. This manages the dependencies in the project file `pyproject.toml` and uses the `poetry.lock` file for pinning. 

Make sure that you have Poetry running and configured to use a version of Python 3.x. The Python version required is specified by Poetry in the `pyproject.toml` file.

### Install Poetry Environment

```
$ poetry install
```

### Running Django CMS

You can run active the shell for Poetry and start the Django server that way:

```
$ poetry shell
$ ./manage.py runserver
```

Alternatively you can also use the run command:

```
$ poetry run manage.py runserver
```