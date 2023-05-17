from jinja2 import Environment, FileSystemLoader

# Create a Jinja2 environment with a file system loader
env = Environment(loader=FileSystemLoader('.'))