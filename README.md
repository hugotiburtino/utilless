# utilless
Useless library if you have time for puzzles, a useful one if you don't

## Quickstart
Install using pip: `pip install utilless`  
and import package into your script, v.g. `from utilless.comma import justcomma`

## Comma module
Manipulates iterables and gets results with commas

iterable: any element that has __ iter __ method, like
list, tuple, set, dict or even str.

* justcomma(iterable)

`>>> justcomma(['apples', 'bananas', 'tofu', 'cats'])`  
`'apples,bananas,tofu,cats'`


* commaspace(iterable)

`>>> commaspace(['apples', 'bananas', 'tofu', 'cats'])`  
`'apples, bananas, tofu, cats'`

* commaand(iterable)

`>>> commaand(['apples', 'bananas', 'tofu', 'cats'])`  
`'apples, bananas, tofu, and cats'`

or commaand(iterable, str)  
`>>> commaand(['apples', 'bananas', 'tofu', 'cats'], ' & ')`  
`'apples, bananas, tofu & cats'`