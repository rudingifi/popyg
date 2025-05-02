import os
import shutil
import sys
from jinja2 import Environment, FileSystemLoader

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

try:
    # Create necessary directories
    create_directory('dist')
    create_directory('static')
    create_directory('netlify/functions')

    # Set up Jinja2 environment
    env = Environment(loader=FileSystemLoader('templates'))

    # Copy static files
    if os.path.exists('static'):
        shutil.copytree('static', 'dist/static', dirs_exist_ok=True)
        print("Copied static files")

    # Render templates
    templates = ['index.html', 'base.html']
    
    for template_name in templates:
        try:
            template = env.get_template(template_name)
            output = template.render()
            
            with open(f'dist/{template_name}', 'w', encoding='utf-8') as f:
                f.write(output)
            print(f"Rendered template: {template_name}")
        except Exception as e:
            print(f"Error rendering {template_name}: {str(e)}")

    print("Build completed successfully!")
except Exception as e:
    print(f"Build failed: {str(e)}")
    sys.exit(1) 