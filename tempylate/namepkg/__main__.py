"""

"""

import argparse
import namepkg

def main(cla):
    name = namepkg.Name(theme=cla.theme,
                        name=cla.name,
                        number=cla.number,
                        save=cla.save,
                        delay=cla.delay,
                        min=cla.minimum,
                        max=cla.maximum,
                        start=cla.start)
    name.gen_new_name()
    print(name.output)

def gcla():
    """Get Command Line Arguements"""
    parser = argparse.ArgumentParser(description='Query packages on PyPI.')
    
    parser.add_argument('-t', '--theme', type=str, default='',
        help='Topic or subject word to base sugggestions upon.')
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

if __name__ == "__main__":
    cla = gcla()
    main(cla=cla)
