# hello_jinja.py

import jinja2

environment = jinja2.Environment()
template = environment.from_string("Hello, {{ name}}!")
template.render(name="World")
