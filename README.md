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

For control flow (for loops, if statements), we use this syntax:

```
{% for item in mylist %}
```
