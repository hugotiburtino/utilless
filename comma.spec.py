"""
Unit Tests for the comma module
"""

from comma import commaspace, justcomma, commaand

tuple_spam = ('apples', 'bananas', 'tofu', 'cats')
list_spam = ['apples', 'bananas', 'tofu', 'cats']
all_kinds = [0, 'foo', 1.9]

def test_commaspace():
    "Tests the function commaspace"
    assert commaspace(tuple_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(list_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(all_kinds) == "0, foo, 1.9"
    try:
        commaspace([])
    except ValueError as exc:
        assert 'is empty' in str(exc)
    return 'tests passed'

test_commaspace()

def test_justcomma():
    "Tests the function justcomma"
    assert justcomma(tuple_spam) == 'apples,bananas,tofu,cats'
    assert justcomma(list_spam) == 'apples,bananas,tofu,cats'
    assert justcomma(all_kinds) == "0,foo,1.9"
    try:
        justcomma([])
    except ValueError as exc:
        assert 'is empty' in str(exc)
    return 'tests passed'


test_justcomma()

def test_commaand():
    "Tests the function commaand"
    assert commaand(tuple_spam) == 'apples, bananas, tofu, and cats'
    assert commaand(list_spam) == 'apples, bananas, tofu, and cats'
    assert commaand(all_kinds) == "0, foo, and 1.9"
    try:
        commaand([])
    except ValueError as exc:
        assert 'is empty' in str(exc)
    return 'tests passed'

test_commaand()
