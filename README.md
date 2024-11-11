Geocrypt
========

Installation
------------
To install, use::

    pip install geocrypt

Geocrypt requires `sympy`.

Use
---
Geocrypt can only encode hexadecimal (with capital letters).
To generate a key, use::

    k = geocrypt.Key()
    k.generate()

To encode a string::

    text = "Hello world!"
    ctext = geocrypt.encode(text, k)

To decode a string::

    dtext = geocrypt.decode(ctext, k)

Complete example::

    import geocrypt
    k = geocrypt.Key()
    k.generate()
    text = "Hello world!"
    ctext = geocrypt.encode(text, k)
    dtext = geocrypt.decode(ctext, k)

Source
------
Geocrypt's code is available `here <https://github.com/lolo859/geocrypt>`_.