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
    path : pathlib.Path, Optional
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
    path : pathlib.Path
        Specifies the dir to save the output json. Defaults to __file__.
    pyload : dict
        The raw dictionary data returned from this pypi request. Only 
        exists if the package name exists.
    cached : dict
        The raw dictionary data cached from pypi. Contains all previous
        payloads and names previously searched while save was enabled.
    """
    def __init__(self, 
                 theme : str = '', 
                 name : str = '',
                 save : bool = False, 
                 path : pathlib.Path() = (pathlib.Path(
                       os.path.dirname(os.path.realpath(__file__)))
                       / pathlib.Path('data/cache.json'))):
        self.name = name
        self.theme = theme
        self.save = save
        self.path = path
        self.available = False
        self.payload = {}
        self.cached = {}

    def gen_new_name(self):
        """Make a new name."""

        raise NotImplementedError('Sorry this function is not built yet')
        pass

    def check(self):
        """Check to see if the name is available on PyPI."""
        self.mk_url() # Populate attributes
        available = True # Assume the name is available
        url = self.url
        
        request = urllib.request.Request(url)

        try:
            self.read()
            if self.name in self.cached:
                print("It's in the cache.")
                available = False
            pass
        except FileNotFoundError as error:
            pass
        
        if available:
            try:
                # Attempt to get a packages json data from pypi
                with urllib.request.urlopen(request) as f:
                    self.payload = json.loads(f.read().decode('utf-8'))
                    self.payload = {self.name : self.payload}

                if self.save:
                    self.write()

                available = False # Package is used by someone
                pass
            
            except urllib.error.HTTPError as error:
                error.code
                available = True  # Package is available
                pass

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

    def write(self):
        """Save the request payload to a file."""
        # Output the result to a local file
        data = {**self.cached, **self.payload}
        with open(self.path, 'w') as f:
            f.write(json.dumps(data, sort_keys=True, indent=4))
        pass
    
    def read(self):
        """Load a saved payload file."""
        with open(self.path, 'r') as f:
            self.cached = json.loads(f.read())
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
        print('#=================#\n')

    return None

if __name__ == "__main__":
    main()