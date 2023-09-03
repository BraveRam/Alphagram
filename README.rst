==================
Alphagram Library
==================

Introduction
------------

Alphagram is a Python library designed to simplify the process of creating Telegram bots. It offers an easy-to-use interface for the Telegram Bot API.

Features
--------

- Send and receive messages
- Inline query handling
- Custom keyboards
- File uploads/downloads

Installation
------------

To install Alphagram, run the following command:

.. code-block:: shell

    pip install alphagram

Quick Start
-----------

Here's a simple example to get your bot up and running:

.. code-block:: python

    from alphagram.alphagram import Alphagram 

    bot = Alphagram('YOUR_API_KEY')

    @bot.message_handler(commands=['start'])
    def start(message):
        bot.send_message(message.chat.id, 'Hello, welcome to Alphagram!')

    bot.start()

Contribute
----------

- Issue Tracker: `GitHub Issues <https://github.com/really650a/alphagram/issues>`_
- Source Code: `GitHub <https://github.com/really650a/alphagram>`_

Support
-------

If you are having issues, please let us know.
You can contact us at `Alphalm1000@gmail.com <mailto:support@example.com>`_.

License
-------

The project is licensed under the MIT License.
