import os
import shutil
from jinja2 import Environment, FileSystemLoader

# Create dist directory if it doesn't exist
if not os.path.exists('dist'):
    os.makedirs('dist')

# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))

# Copy static files
if os.path.exists('static'):
    shutil.copytree('static', 'dist/static', dirs_exist_ok=True)

# Render templates
templates = ['index.html', 'base.html']

for template_name in templates:
    template = env.get_template(template_name)
    output = template.render()
    
    with open(f'dist/{template_name}', 'w', encoding='utf-8') as f:
        f.write(output)

print("Build completed successfully!") 