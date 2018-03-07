## Cookiecutter aiohttp web application

[Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/) template for easier creation of aiohttp web application 
hosted on [Heroku](https://www.heroku.com).


### Features

* Testing with [py.test](https://docs.pytest.org/en/latest/).
* Continuous integration with Travis.
* Template rendering with [Jinja2](http://jinja.pocoo.org/).
* JS packages management with [npm](https://www.npmjs.com/).
* CSS Framework using [siimple](https://siimple.juanes.xyz/documentation/).
* Command line interface using [Click](http://click.pocoo.org/6/) (_optional_).


### Quickstart

Install the latest Cookiecutter if you haven't installed it yet:

```
pip install -U cookiecutter
```

Generate a new aiohttp project

```
cookiecutter https://github.com/bmwant/templio.git
```

Then:

* Create a repo and put it there.
* Add the repo to your [Travis-CI]( http://travis-ci.org/) account (_optionally_).
* Install the requirements into a virtualenv (`pipenv install`).
* Deploy project with `git push heroku:master`.


### Customization

If you need different project structure of add any improvement - feel free to create a PR
or make your own modifications within the fork.
For more details about starting new project from this template refer to 
[this article](http://bmwlog.pp.ua/post/129).
More information about deployment can be found [here](https://devcenter.heroku.com/articles/getting-started-with-python#deploy-the-app).
