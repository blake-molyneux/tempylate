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
    
    Attributes
    ----------
    theme : str, Optional
        A topic/theme subject area. Used to generate a new name.
    name : str, Optional
        An explicit name.
    available : bool
        Whether or not the name is available on PyPI.
    
    """
    def __init__(self,
                 theme : str = '',
                 name : str = ''):

        self.name = name
        self.theme = theme
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
            urllib.request.urlopen(request)
            available = False
        except urllib.error.HTTPError as e:
            available = True

        self.available = available
        pass

    def mk_url(self):
        """Construct the PyPI URL for the chosen name."""
        name = self.name
        base = 'https://pypi.org/project/'
        
        self.url = urllib.parse.urljoin(base, name)
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
        name.check()
        
        if (name.available):
            print(f'{name.name} is available!')
        else:
            print(f'{name.name} is taken.')

    return None

if __name__ == "__main__":
    main()