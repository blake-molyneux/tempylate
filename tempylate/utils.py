"""
General purpose utilities for the package.

This is a dumpster for all the "usefull" functions which are used
frequently throughout the package, but do not belong in any of the other
modules due to grouping or organizational rules.
"""

import json
import pathlib
import logging
import warnings

log = logging.getLogger(__name__)
cwd = pathlib.Path(__file__).absolute().parent

def logging_config(path: pathlib.Path = cwd/'docs/logs/config.json') -> None:
    """
    Load in global logging configuration from a logger config file.

    Parameters
    ----------
    path : pathlib.Path, optional
        The path to the logging.conf file. Default is:
        './docs/logs/logging.conf'. This file needs to be loaded for the
        logging framework to be functional.
    """

    if (not path.is_file()):
        # The logging configuration doesn't exists, raise a runtime warning
        # Fix dumb warning format
        warnings.formatwarning = warning_prettyprint

        # Construct and issue the warning
        warnings.warn((
            'Logging system not started.\n'
            'Configuration file not found.\n'
            'This will not effect functionality, however debugging issues '
            'will be made much more difficult. The expected location was: '
            f'"{path}"'), category=UserWarning, stacklevel=1)

    else:
        # The logging configuration exists
        # Load config dict from json
        logging_config = load(path)
        # Apply the dict logging config
        logging.config.dictConfig(logging_config)

    return None

def warning_prettyprint(message, category, filename, lineno, line=None) -> str:
    """
    Monkeypatch the default warning message printing so it's prettier.
    """

    result = (
        f'\nWARNING\n-------\n{message}\n\n'
    )

    return result

def load(path: pathlib.Path) -> dict:
    """Load a json file into a dictionary.

    Parameters
    ----------
    path : pathlib.Path
        The path to the json file to be loaded

    Returns
    -------
    dict
        A dictionary representation of the data in the provided json.
    """
    result = {}

    with open(path, 'r') as f:
        result = json.load(f)    

    return result

def save(data: dict, path: pathlib.Path) -> bool:
    """Save a provided dictionary to file in json.
    
    Parameters
    ----------
    data : dict
        The dictionary to be saved to file.
    path : pathlib.Path
        The path to the file to be saved. This path should included the
        file name, and any file extensions you wish, but ideal use the
        .json extension for transparency.

    Returns
    -------
    bool,
        Returns true if the save opperation terminated without error.
    """

    with open(path, 'w') as fp:
        json.dump(data, fp, indent=4, sort_keys=True)

    return True
