#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by
    checking whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    tags = _extract_tags(html)
    stack = []
    if len(tags) == 0 and '<' in html:
        return False
    elif len(tags) == 0:
        return True
    if len(tags) == 1:
        return False
    for tag in tags:
        if '/' not in tag:
            stack.append(tag)
        elif len(stack) != 0:
            if stack[-1][1:len(stack[-1])] == tag[2:len(tag)]:
                stack.pop()
            else:
                return False
        else:
            return False
    if len(stack) == 0:
        return True
    return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be
    used directly by the user are prefixed with an underscore.

    This function returns a list of
    all the html tags contained in the input string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''
    stack = []
    tag = ''
    if '<' not in html or '>' not in html:
        return stack
    while '<' in html or '>' in html:
        if len(html) <= 1:
            return stack
        tag = html[html.index('<') : html.index('>')+1]
        stack.append(tag)
        html = html[html.index('>') + 1:]
    return stack
