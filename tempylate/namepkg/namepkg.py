"""
Determine if a module name is good.

.. warning::
    Work In Progress.

This module makes naming new packages easier by suggesting new names and
checking that those names aren't already taken on the PyPI.

This module is a component of the **tempylate** project.
"""


__author__ = "Blake Molyneux"
__email__ = "blake.molyneux@hotmail.com"
__docformat__ = "restructuredtext"
__license__ = "MIT"
__version__ = "0.0.1.dev0"


import os
import json
import pathlib
import urllib.request
import urllib.parse

class Name:
    """
    Name of a potential project.

    Parameters
    ----------
    theme : str, Optional
        A topic/theme subject area. Used to generate a new name.
    name : str, Optional
        An explicit name.
    save : bool, Optional
        If set to true, any json data recieved will be saved. False by
        default.
    out : pathlib.Path, Optional
        Specifies the dir to save the output json. Defaults to __file__.

    Attributes
    ----------
    theme : str
        A topic/theme subject area.
    name : str
        The name selected by the user, generated or specified.
    available : bool
        Whether or not the name is available on PyPI.
    save : bool
        If set to true, any json data recieved will be saved. False by
        default.
    out : pathlib.Path
        Specifies the dir to save the output json. Defaults to __file__.

    """
    def __init__(self, 
                 theme : str = '', 
                 name : str = '',
                 save : bool = False, 
                 out : pathlib.Path() = (pathlib.Path(
                       os.path.dirname(os.path.realpath(__file__)))
                       / pathlib.Path('data/cache.json'))):
        self.name = name
        self.theme = theme
        self.save = save
        self.out = out
        self.available = False

    def gen_new_name(self):
        """Make a new name."""

        raise NotImplementedError()
        pass

    def check(self):
        """Check to see if the name is available on PyPI."""
        self.mk_url() # Populate attributes
        ans = False # Assume the name is taken
        url = self.url
        
        request = urllib.request.Request(url)
        try:
            # Attempt to get a packages json data from pypi
            with urllib.request.urlopen(request) as f:
                dict_in = json.loads(f.read().decode("utf-8"))
            
            if (self.save):
                # Output the result to a local file
                output_path = self.out
                with open(output_path, 'a') as f:
                    f.write(json.dumps(dict_in, sort_keys=True, indent=4))

            available = False # Package is used by someone
        
        except urllib.error.HTTPError as e:
            available = True  # Package is available

        self.available = available
        pass

    def mk_url(self):
        """Construct the PyPI URL for the chosen name."""
        name = self.name
        url_base = 'https://pypi.org/pypi/'

        url_suffix = f'{name}/json'
        url = urllib.parse.urljoin(url_base, url_suffix)

        self.url = url
        pass

def main():
    """
    This function gets run when this module is run directly.

    Takes no arguments, and returns None.
    """

    while (True): # UI Loop
        print('\n#=================#')
        input_name = input('Input project name:\n')
        name = Name(name=input_name)
        name.save = True # Save the output
        name.check()
        
        if (name.available):
            print(f'{name.name} is available!')
        else:
            print(f'{name.name} is taken.')

    return None

if __name__ == "__main__":
    main()