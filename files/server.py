from flask import Flask, render_template # import modules for flask to work
app = Flask(__name__)

@app.route('/') # default route
def html_table():
    # list of dictionaries imitating a database query
    users = [ 
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'John', 'last_name' : 'Supsupin'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template('table.html', users = users)


if __name__ == '__main__':
    app.run(debug = True, port = 8000)