# __AirBnB_clone__

The AirBnB clone utilizes higher level programming skills to deploy a copy of the AirBnB website.

## **The Console**

The console is a command interpreter that manages all AirBnB objects.

## *Usage*

The console is used in both interactive and non-interactive mode

## Interactive mode

The console is started by running the command
./console.py

A prompt (hbnb) should appear where you can type commands followed by a new line. After the command is run, you will be reprompted. Empty lines also reprompt the user. Type help to get a list of available commands. Type quit to end the session.

## *Example*

    $ ./console.py
    (hbnb) help
    
    Documented commands (type help <topic>):
    ========================================
    EOF      help  quit
    
    (hbnb)
    (hbnb)
    (hbnb) quit

## Non-Interactive Mode

The console is started by using "echo".

You can "pipe" an input into the command line by using echo

## *Example*

    $ echo "help" | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)

You can also pipe in a file with one command per line.

## *Example*

    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)

    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)

    $ cat test_help
    help
    $
    $ cat test_help | ./console.py
    (hbnb)
    
    Documented commands (type help <topic>):
    ========================================
    EOF  help  quit
    (hbnb)

## Contact info

If you have questions or suggestions, contact Maab Ibrahim at maababubakr1@gmail.com