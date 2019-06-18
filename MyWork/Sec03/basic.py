from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = "Merfin Melvin"
    letters = list(name)
    cat_dict = {'cat_name': 'Xerxes'}
    mylist = [1,2,3,4,5]
    cats = ['Xerxes', 'Frank', 'Iris', 'Athena']

    return render_template('basic.html', my_variable=name, letters=letters, 
            cat_dict=cat_dict, mylist=mylist, cats=cats)
            
if __name__ == '__main__':
    app.run(debug=True)