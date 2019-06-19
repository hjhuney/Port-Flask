# Jose Portillo Flask Course

Notes and work from Jose Portillo's Flask course. 

## Table of Contents

Section 1: [Setting Everything Up](https://github.com/hjhuney/Port-Flask/blob/master/README.md#setting-everything-up)<br>
Section 7: [Flask Basics](https://github.com/hjhuney/Port-Flask/blob/master/README.md#flask-basics)<br>
Section 8: [Templates](https://github.com/hjhuney/Port-Flask/blob/master/README.md#templates)<br>

# Setting Everything Up

## Set up Conda Virtual Environment

To set up a virtual environment:

```
conda create -n environment_name python=3.7
```

Where "environment_name" is the name of the environment you want to create. For this exercise, I used "flaskenv".

## Activate Conda Environment

To activate Conda virtual environment:

```
conda activate flaskenv
```

or in Anaconda prompt, you can just use:

```
activate flaskenv
```

If you are using Bash / Linux:

```
source activate flaskenv
```

## Install All Flask Libraries Needed

We should have a requirements.txt file with all the necessary libraries. To install all of them at once, we use:

```
pip install -r requirements.txt
```

# Flask Basics

## Hello World

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

if __name__ == '__main__':
    app.run()
```

To run program:

```
python helloworld.py
```

## Basic Routes


```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello Puppy!</h1>'

@app.route('/information')
def info():
    return '<h1>Puppies are cute!</h1>'

if __name__ == '__main__':
    app.run()
```

## Dynamic Routes

```
@app.route('/puppy/<name>')
def puppy(name):
    # Page for an individual puppy.
    return '<h1>This is a page for {}<h1>'.format(name)
```

## Debugging

Set debug equal to True. 

```
if __name__ == '__main__':
    # Never have debug=True for production apps!
    app.run(debug=True)
```

# Templates

## Jinja Templating

Jinja templating allows us to directly insert variables from Python code into HTML. The syntax for inserting a variable is:

```
{{somePythonVariable}}
```

Set parameters in render_template function and then us {{}} syntax to insert them into template.

Example of creating a Python variable and inserting it into html

```
# our .py file

@app.route('/')
def index():
    some_variable = "Melvin"
    return render_template('basic.html', my_variable=some_variable)
```

And 

```
// our html file
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Basic</title>
  </head>
  <body>
    <h1>Welcome to {{my_variable}}'s</h1>
    <h2>Come on down for deals on mulch!</h2>
    <img src="../static/higg001.jpg" width="600" height="400">

  </body>
</html>
```

## Control Flow

For control flow (for loops, if statements), we use this syntax {% %}. For loops must be ended by tag of {% endfor %}. 

For loop example below:

```
<ul>
  {% for item in mylist %}
  <li>{{item}}</li>
  {% endfor %}    
</ul>
```

If-else statement example below:

```
{% if 'Xerxes' in cats %}
  <p>Found you Xerxes!</p>
{% else %}
  <p>Xerxes is not in this castle</p>
{% endif %}
```

## Template Inheritance

Set up base html template file with reusable aspects of our site. Then we use {% extend "base.html" %} and {% block %} statements to extend these reusable aspects to other pages.

We could use template inheritance by create a base html file (e.g. "base.html"), inserting something like this into the body of our code:

```
<body>

              {% block content %}
              
              {% endblock %}    
</body>
</html>
```

And then creating a page that uses that template like this:

```
{% extends "base.html" %}

{% block content%}
<h1>This is the homepage!</h1>
<h2>Go to /kitty/name </h2>

{% endblock %}
```

Our app might look like this:

```
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/kitty/<name>')
def cat_name(name):
    return render_template('cat.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
```


## Filtering

We can also use filters for variables which look like this:

```
{{ variable | filter ))
```

For example:

```
{{cat_name | capitalize}}
```

takes the variable cat_name and applies capitalization to it, so that "garfield" becomes "Garfield". 


## URL Links with Templates

Flask has a url_for() helper function that allows us to connect other template pages or files within our templates. 

Example; code in our app:

```
@app.route('/')
def index():
    return render_template('home.html')
```

Code creating link in the html template file. 

```
<a class="navbar-brand" href="{{url_for('index')}}">Jerky Cats!</a>
```

For linking to an image:

```
<a href={{ url_for('static', filename='image_name.jpg')}}>Here</a>
```

First argument is directory (here we are getting an image from the "static" subfolder), second argument is file name. 

## 404 Message

In the app:

```
# 404 message
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
```

We use .errorhandler instead of app.route. By contention, we use "e" for error as the argument in the function. 

# Forms with Flask

## Form Basics

* Configure a secret key for security
* create a WTForm Class
* Set up a view function
* Add methods = ['GET, 'POST']
* Create an instance of Form Class
* Handle form submission

