===================================================
Tests for text_indentation in 0-add_integer.py
===================================================

>>> say_my_name = __import__('3-say_my_name').say_my_name

>>> say_my_name("Douglas", "Ken")

My name is Douglas Ken

>>> say_my_name("Angaza", 4)

Traceback (most recent call last):

TypeError: last_name must be a string

>>> say_my_name("Douglas", None)

Traceback (most recent call last):

TypeError: last_name must be a string

>>> say_my_name("Douglas", {})

Traceback (most recent call last):

TypeError: last_name must be a string


>>> say_my_name("Douglas", 8)

Traceback (most recent call last):

TypeError: last_name must be a string

>>> say_my_name([], "Ken")

Traceback (most recent call last):

TypeError: first_name must be a string

>>> say_my_name(8, "Ken")

Traceback (most recent call last):

TypeError: first_name must be a string



>>> say_my_name([[1, 2, 3], [4, 5, 6], [7, 8, 9]], "Ken")

Traceback (most recent call last):

TypeError: first_name must be a string



>>> say_my_name("Angaza", 69)

Traceback (most recent call last):

TypeError: last_name must be a string



>>> say_my_name("Angaza", 1)

Traceback (most recent call last):

TypeError: last_name must be a string



>>> say_my_name(None, "Ken")

Traceback (most recent call last):

TypeError: first_name must be a string



>>> say_my_name([1, 2, 3], "Ken")

Traceback (most recent call last):

TypeError: first_name must be a string



>>> say_my_name()

Traceback (most recent call last):

TypeError: say_my_name() missing 1 required positional argument: 'first_name'
