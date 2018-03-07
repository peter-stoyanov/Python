#!/usr/bin/env python
"""Replace in a HTML document given as string all the tags <a href=…>…</a>"""

__author__ = "Petar Stoyanov"

import re

def main():
    """
    replace <a> with: [URL href=".."]...[/URL]
    """

    text = []
    line = input()
    while line != 'end':
        text.append(line)
        line = input()
        
    #text = [
        # '<ul>',
        #     '<li>',
        #         '<a href="http://softuni.bg">SoftUni</a>',
        #     '</li>',
        # '</ul>']

    regex = re.compile(r"""
        <a
            (?P<link>
                [^>]+?
            )
        >
            (?P<text>
                [^<>]*?
            )
        </a>
        """, re.VERBOSE)

    for (index, line) in enumerate(text):
        for match in regex.finditer(line):
            modified_part = f'''[URL{match.group('link')}]{match.group('text')}[/URL]'''
            text[index] = line.replace(match.group(), modified_part)
    
    print('\n'.join(text))


if __name__ == '__main__':
    main()
