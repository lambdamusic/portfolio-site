# myutils.py

import sys
import click
from time import strftime
import json
import urllib.parse
import string
import re




######################
### UTILS
######################


def nice_titles(s):
    """good for generating titles - for human consumption"""
    return string.capwords(s)

def upperfirst(x):
    return x[0].upper() + x[1:]

# # http://stackoverflow.com/questions/1324067/how-do-i-get-str-translate-to-work-with-unicode-strings
def translate_non_alphanumerics(to_translate, translate_to=u''):
    not_letters_or_digits = u'!"#%\'()*+,-./:;<=>?@[\]^_`{|}~'
    translate_table = dict((ord(char), translate_to) for char in not_letters_or_digits)
    return to_translate.translate(translate_table)

def remove_non_alphanumerics(to_translate):
    """Python - keep only alphanumeric and space, and ignore non-ASCII
    https://stackoverflow.com/questions/55902042/python-keep-only-alphanumeric-and-space-and-ignore-non-ascii"""
    return re.sub(r'[^A-Za-z0-9 ]+', '', to_translate)

def url_encode(u):
    return urllib.parse.quote(u.strip().lower().replace(" ", "-").encode('utf8'))

def url_encode_search(u): # same as above, but nor white space replacing
	return urllib.parse.quote(u.strip().lower().encode('utf8'))

def nice_url_name(s):
    """ create strings for urls """

    out = remove_non_alphanumerics(s)
    return url_encode(out)

def get_firstletter(s):
    """ returns a first letter useful for indexing """
    if s:
        if (s[0] in string.punctuation) or (s[0] in string.digits):
            return "*"
        else:
            return s[0].lower()
    else:
        return ""


def print_json(your_json_string):
    print(json.dumps(your_json_string, indent=4))


def printDebug(text, mystyle="", err=True, **kwargs):
    """Wrapper around click.secho() for printing in colors with various defaults.
    :kwargs = you can do printDebug("s", bold=True)
    2018-12-06: by default print to standard error stderr (err=True)
    https://click.palletsprojects.com/en/5.x/api/#click.echo
    This means that the output is ok with `less` and when piped to other commands (or files)
    Styling output:
    <http://click.pocoo.org/5/api/#click.style>
    Styles a text with ANSI styles and returns the new string. By default the styling is self contained which means that at the end of the string a reset code is issued. This can be prevented by passing reset=False.
    This works also with inner click styles eg
    ```python
    uri, title = "http://example.com", "My ontology"
    printDebug(click.style("[%d]" % 1, fg='blue') +
               click.style(uri + " ==> ", fg='black') +
               click.style(title, fg='red'))
    ```
    Or even with Colorama
    ```
    from colorama import Fore, Style
    printDebug(Fore.BLUE + Style.BRIGHT + "[%d]" % 1 + 
            Style.RESET_ALL + uri + " ==> " + Fore.RED + title + 
            Style.RESET_ALL)
    ```
    Examples:
    click.echo(click.style('Hello World!', fg='green'))
    click.echo(click.style('ATTENTION!', blink=True))
    click.echo(click.style('Some things', reverse=True, fg='cyan'))
    Supported color names:
    black (might be a gray)
    red
    green
    yellow (might be an orange)
    blue
    magenta
    cyan
    white (might be light gray)
    reset (reset the color code only)
    New in version 2.0.
    Parameters:
    text – the string to style with ansi codes.
    fg – if provided this will become the foreground color.
    bg – if provided this will become the background color.
    bold – if provided this will enable or disable bold mode.
    dim – if provided this will enable or disable dim mode. This is badly supported.
    underline – if provided this will enable or disable underline.
    blink – if provided this will enable or disable blinking.
    reverse – if provided this will enable or disable inverse rendering (foreground becomes background and the other way round).
    reset – by default a reset-all code is added at the end of the string which means that styles do not carry over. This can be disabled to compose styles.
    """

    if mystyle == "comment":
        click.secho(text, dim=True, err=err)
    elif (mystyle == "important") or (mystyle == "bold"):
        click.secho(text, bold=True, err=err)
    elif mystyle == "normal":
        click.secho(text, reset=True, err=err)
    elif mystyle == "red" or mystyle == "error":
        click.secho(text, fg='red', err=err)
    elif mystyle == "green":
        click.secho(text, fg='green', err=err)
    else:
        click.secho(text, err=err, **kwargs)



def truncate_words(sentence, max):
    t = sentence.split(" ")
    if len(t) < max:
        return sentence
    else:
        return " ".join(t[:max]) + "..."


def split_list(L, n):
    """
	n is the size of the splitted list element (not the tot number of elements!)

	In [8]: for x in split_list(range(4), 1):
	   ...:		print x
	   ...:
	[0]
	[1]
	[2]
	[3]

	"""
    assert type(L) is list, "L is not a list"
    for i in range(0, len(L), n):
        yield L[i:i + n]


def blank_or_string(s):
    """If it's empty, output the string blank"""
    if not s.strip():
        return 'blank'
    return s


def preview_string(s, length):
    """If we have a value, returns the first [length] chars of the string.."""
    if s:
        if len(s) < length:
            result = unicode(s)
        else:
            result = unicode(s)[0:length] + "..."
        return result


def isint(s):
    """checks if a string is a number"""
    try:
        return int(s)
    except ValueError:
        return False


def findmin(rangen, n):
    e = 0
    while e < n:
        e += rangen
        # returns the one before
    return e - rangen


def findmax(rangen, n):
    e = 0
    while e < n:
        e += rangen
        # returns the one after
    return e


def buildranges(amin, amax, rangeval):
    """Retunrs a list of tuples, with the string-range first and then
     the numbers in a tuple: [('990-1020', (990, 1020)), ('1020-1050', (1020, 1050))]  """
    r = []
    allvalues = range(amin, amax, rangeval)
    for index, item in enumerate(allvalues):
        if (index + 1) < len(allvalues):
            a = "%d-%d" % (item, allvalues[index + 1])
            r.append((a, (item, allvalues[index + 1])))
    return r


def split_list_into_two(somelist):
    x = len(somelist)
    z = x / 2
    res1 = somelist[:(x - z)]
    res2 = somelist[(x - z):]
    return [res1, res2]


def group_list_items_by_two(lista, listaexit=None):
    lista_x = []
    listaexit = listaexit or []
    if lista:
        lista_x.extend(lista)
        lista_x.reverse()
        first_el = lista_x.pop()
        if len(lista_x) == 0:
            second_el = None
        else:
            second_el = lista_x.pop()
        listaexit.append([first_el, second_el])
        if lista[2:]:
            group_list_items_by_two(lista[2:], listaexit)
        #print(listaexit)
        return listaexit


filler = ["value_%s" % (i) for i in range(10)]


# given a center, returns a list of the neighbouring numbers according to the paramenters passed
def paginator_helper(
        center,
        max,
        howmany=5,
        interval=1,
        min=1,
):
    if center - howmany > min:
        min = center - howmany
    if center + howmany < max:
        max = center + howmany
    return range(min, (max + 1), interval)
