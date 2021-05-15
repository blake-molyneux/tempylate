"""
Find suitable names for a file/module/package/project.

This module makes naming new packages easier by suggesting new names and
checking that those names aren't already taken on the PyPI.

This module is a component of the `tempylate` project.
"""

__version__ = '0.0.1.dev0'

import pathlib
import logging

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

import json
import time
import random
import argparse
import urllib.request
import urllib.parse

import markupsafe

class RequestFailedError(Exception):
    """Exception raised for errors in the input.

    Attributes
    ----------
    message :
        Explanation of the error.
    """
    def __init__(self, message):
        self.message = message

class Name:
    """
    Name of a potential project.

    Parameters
    ----------
    theme : str, Optional
        A topic/theme subject area. Used to generate a new name.
    name : str, Optional
        An explicit name.
    number : int, Optional
        If a new name is requested, this sets how many suggestions are
        to be provided.
    start : str, Optional
        A starting string upon which to add additional letters/text.
    save : bool, Optional
        If set to true, any json data received will be saved. False by
        default.
    path : pathlib.Path, Optional
        Specifies the dir to save the output json. Defaults to __file__.
    delay : int
        Sets the maximum possible time to wait between PyPI queries.
        Default is 3s.
    min : int
        Minimum character length to select package name set. Default 3.
    max : int
        Maximum character length to select package name set. Default 10.

    Attributes
    ----------
    theme : str
        A topic/theme subject area.
    name : str
        The name selected by the user, generated or specified.
    output : list of str
        List of all names generated by a generic search.
    available : bool
        Whether or not the name is available on PyPI.
    save : bool
        If set to true, any json data received will be saved. False by
        default.
    path : pathlib.Path
        Specifies the dir to save the output json. Defaults to __file__.
    """
    def __init__(self, theme : str = '', number : int = 3, name : str = '',
            output : list = [], min_ : int = 3, max_ : int = 10,
            delay : int = 3, start : str = '', save : bool = True,
            path : pathlib.Path() = (cwd / 'data/cache.json')):

        self.name = name
        self.theme = theme
        self.number = number
        self.output = output
        self.save = save
        self.min = min_
        self.max = max_
        self.start = start
        self.delay = delay
        self.path = path
        self.available = False
        self.payload = {}
        self.cached = {}

        pass

    def gen_new_name(self):
        """Generate new name(s) based on input parameters."""
        url_base = 'https://api.datamuse.com/words?'
        url_query = ''
        
        if self.theme != '':
            # A theme is specified by the user
            url_query = f'rel_trg={self.theme}'
            pass

        else:
            # Create a random theme
            if (self.start == ''):
                alphabet = 'abcdefghijklmnopqrstuvwxyz'
                theme = alphabet[random.randrange(26)]
            else:
                theme = self.start
            theme += '?'*random.randrange(self.min, self.max)
            url_query = f'sp={theme}'
            pass

        url = url_base + url_query
        print(f'Querying datamuse for words ...')
        request = urllib.request.Request(url)

        try:
            # Fetch the json data for a package
            with urllib.request.urlopen(request) as f:
                payload = json.loads(f.read().decode('utf-8'))
            print(f'{len(payload)} potential names found.')
            print('Querying PyPI for available packages...')

            count = 0
            index = 0
            names = []
            # Check each potential name until number of names fullfilled
            while ((count < self.number) and (index < (len(payload)-1))):
                self.name = payload[index]['word']
                wait = random.random()*self.delay
                time.sleep(wait)
                self.check()
                if self.available:
                    names.append(self.name)
                    count += 1
                print(f'name {count} of {self.number} found.\r', end='')
                index += 1
            print('')
            self.output = names
            pass

        except urllib.error.HTTPError as error:
            raise RequestFailedError('Data could not be loaded from web api.')
        pass

    def check(self):
        """Check to see if the name is available on PyPI."""
        self.mk_pypi_url() # Populate attributes
        available = True # Assume the name is available
        url = self.url
        
        request = urllib.request.Request(url)

        try:
            self.cached = self.load()
            if self.name in self.cached:
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
                if (error.code != 404):
                    raise RequestFailedError('PyPI request failed. Try again.')
                available = True  # Package is available
                pass

        self.available = available
        pass

    def mk_pypi_url(self):
        """Construct the PyPI URL for the chosen name."""
        name = self.name.replace(' ', '')
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
    
    def load(self):
        """Load a saved payload file."""
        with open(self.path, 'r') as f:
            cached = json.loads(f.read())
        return cached

def cli():
    """
    Manually check whether names are available on PyPI.

    Runs an infinite loop in the command line, where a name can be input
    and the avilability status of that name on PyPI is printed.

    Notes
    -----
    Please note that the input name is presently un
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

def find_names(theme, name, number, save, delay, minimum, maximum, start):
    name = namepkg.Name(
        theme=theme, name=name, number=number, save=save, delay=delay,
        min=minimum, max=maximum, start=start)

    if cla.name == '':
        name.gen_new_name()
        print(name.output)
    else:
        name.check()
        if name.available:
            end = 'available!'
        else:
            end = 'taken.'
        print(f'"{name.name}" is {end}')
    
def get_args():
    """Get Command Line Arguments."""
    parser = argparse.ArgumentParser(description='Query packages on PyPI.')
    
    parser.add_argument('-t', '--theme', type=str, default='',
        help='Topic or subject word to base suggestions upon.')
    parser.add_argument('-m', '--name', type=str, default='',
        help='Single input name.')
    parser.add_argument('-p', '--start', type=str, default='',
        help='Starting text to build names from (ie prefix).')
    parser.add_argument('-n', '--number', type=int, default=3,
        help='Number of results to be output.')
    parser.add_argument('-s', '--save', default=True, 
        action='store_false', help='Cache requested results?')
    parser.add_argument('-d', '--delay', type=int, default=1, 
        help='Max delay time (s) between sequential PyPI queries.')
    parser.add_argument('-min', '--minimum', type=int, default=3, 
        help='Min length of package names to search for.')
    parser.add_argument('-max', '--maximum', type=int, default=10, 
        help='Max length of package names to search for.')

    cla = parser.parse_args()

    return cla