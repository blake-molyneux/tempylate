"""
Create file and folder structures based on templates.
"""

import os
import jinja2

def main():
    jenv = jinja2.Environment(
        loader=jinja2.PackageLoader('fylr', 'templates'),
        autoescape=True)
    
    template = jenv.get_template('module.py')
    print(template.render(
        module_comment='Hello World!'))
    pass

if __name__ == "__main__":
    main()
