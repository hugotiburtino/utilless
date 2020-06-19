from comma import commaspace, justcomma, commaand

tuple_spam = ('apples', 'bananas', 'tofu', 'cats')
list_spam = ['apples', 'bananas', 'tofu', 'cats']
all_kinds = [0, 'foo', 1.9]

def test_commaspace():
    assert commaspace(tuple_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(list_spam) == 'apples, bananas, tofu, cats'
    assert commaspace(all_kinds) == "0, foo, 1.9"
    try:
        commaspace([])
    except Exception as e:
        assert type(e) == ValueError
    return 'tests passed'

test_commaspace()

def test_justcomma():
    assert justcomma(tuple_spam) == 'apples,bananas,tofu,cats'
    assert justcomma(list_spam) == 'apples,bananas,tofu,cats'
    assert justcomma(all_kinds) == "0,foo,1.9"
    try:
        justcomma([])
    except Exception as e:
        assert type(e) == ValueError
    return 'tests passed'


test_justcomma()

def test_commaand():
    assert commaand(tuple_spam) == 'apples, bananas, tofu, and cats'
    assert commaand(list_spam) == 'apples, bananas, tofu, and cats'
    assert commaand(all_kinds) == "0, foo, and 1.9"
    try:
        commaand([])
    except Exception as e:
        assert type(e) == ValueError
    return 'tests passed'


test_commaand()