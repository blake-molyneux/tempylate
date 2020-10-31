"""
Construct and query urls.

.. warning::
    Work In Progress.

This package empulates some of the primitive behaviour of the "requests"
module, but using the inbuilt module urllib to decrease reliance on
external dependancies.
"""

__author__ = "Blake Molyneux"
__email__ = "blake.molyneux@hotmail.com"
__docformat__ = "restructuredtext"
__license__ = "MIT"
__version__ = "0.0.1.dev0"

import urllib.parse

class URL:
    """Parse and construct urls.
    
    Parameters
    ----------

    Attributes
    ----------
    
    """

    def __init__(self):
        pass

def parse(url: str = '') -> dict:
    """Decompose a url into its parts"""
    parts = urllib.parse.urlparse(url)
    return parts

def main():
    """PLACEHOLDER"""
    print("HELLO FROM REQURL")
    return None