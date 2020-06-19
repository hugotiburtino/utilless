from strings import comma_space

tuple_spam = ('apples', 'bananas', 'tofu', 'cats')
list_spam = ['apples', 'bananas', 'tofu', 'cats']
all_kinds = [0, 'foo', 1.9]

def test_comma_space():
    assert comma_space(tuple_spam) == 'apples, bananas, tofu, cats'
    assert comma_space(list_spam) == 'apples, bananas, tofu, cats'
    assert comma_space(all_kinds) == "0, foo, 1.9"
    try:
        comma_space([])
    except Exception as e:
        assert type(e) == "ValueError"
    return 'tests passed'

test_comma_space()