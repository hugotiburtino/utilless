"""
Unit Tests for the comma module
"""

from comma import commaspace, justcomma, commaand

tuple_spam = ('apples', 'bananas', 'tofu', 'cats')
list_spam = ['apples', 'bananas', 'tofu', 'cats']
all_kinds = [0, 'foo', 1.9]
# TODO: add test to dict. Ex.: dictio = {'to do': 'play', 'how many times': 100}
# TODO: test nested iterables. Ex.: [[1, 2], ['foo', 'bar']]

def test_commaspace():
    "Tests the function commaspace"
    assert commaspace(tuple_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(list_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(all_kinds) == "0, foo, 1.9"
    try:
        commaspace([])
    except ValueError as exc:
        assert 'is empty' in str(exc)
    print('test_commaspace passed')

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
    print('test_justcomma passed')

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
    print('test_commaand passed')

test_commaand()
