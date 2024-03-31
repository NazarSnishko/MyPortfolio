from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/projects/<project_id>')
def project_detail(project_id):
    # Logic to retrieve project details by ID
    # Example: project = get_project_by_id(project_id)
    project = {
        'id': project_id,
        'name': 'Project Name',
        'technologies': ['Flask', 'HTML', 'CSS', 'JavaScript'],
        'repository': 'https://github.com/yourusername/project_repo',
        'image': 'project_image.jpg',
        'description': 'Project Description'
    }
    return render_template('project_detail.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)
