from flask import Flask, render_template

app = Flask(__name__)

title = 'Isaac Johan Ziebarth'

# Example list of projects
projects = [
    {"name": "Project 1", "description": "Description of Project 1"},
    {"name": "Project 2", "description": "Description of Project 2"},
    {"name": "Project 3", "description": "Description of Project 3"}
]


@app.route('/')
def home():
    return render_template('home.html', title=title)


@app.route('/projects')
def show_projects():
    return render_template('projects.html', title=title, projects=projects)


@app.route('/contact')
def contact():
    # If you have additional information to pass to the template, you can do so here.
    return render_template('contact.html', title=title)


# Remember to create a 'contact.html' in your templates directory.

if __name__ == '__main__':
    app.run()
