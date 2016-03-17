*****************************************
MarkovText: A Markov Chain text generator
*****************************************
.. image:: https://travis-ci.org/kwkelly/MarkovText.svg?branch=master
    :target: https://travis-ci.org/kwkelly/MarkovText

MarkovText is a simple Python library for reandomly generating strings of
text based on sample text. A Markov chain text generator uses the frequency of
words following the current state to generate plausible sentences that
hopefully are passable as human text. For example, given the input text "Hello,
how are you today? You look well." and a seed of "you", there is a 50% chance
that the next word is either "look" or "today". The current state may consist
of more than just a single word.

MarkovText is written in Python, and requires numpy (though this may be changed
in the future).


.. contents::
    :local:
    :depth: 1
    :backlinks: none


=============
Main Features
=============

* Simple API to generate single or multiple sentences.
* Ability to add to the sample corpus at any time.

============
Future Needs
============

* Remove dependency on numpy
* Create sentences that are related to each other

============
Installation
============

The recommended way to install this package is with pip

.. code-block:: bash

    $ pip install MarkovText

Alternatively you can download and instll it manually (not recommended)

.. code-block:: bash

    $ git clone https://github.com/kwkelly/MarkovText.git
    $ cd MarkovText
    $ python setup.py

