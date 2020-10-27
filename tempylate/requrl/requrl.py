"""
Construct and query urls.

.. warning::
    Work In Progress.

This package empulates some of the primitive behaviour of the "requests"
module, but using the inbuilt module urllib to decrease reliance on
external dependancies.
"""

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

