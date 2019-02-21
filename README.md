# SR-CMD
### A (very buggy) command line language in python

## Intro

It is just a simple processer which splits spaces for commands and arguments, no lexers or tokenisers involved.

It is written in python3 and might only work on Linux??

## Features

* Supports REPL
* Supports parsing .SHL files with the PARSE command
* Has variables
* Has input statment (using ATSTATS)
* Can do basic file IO and deletion
* Supports curses terminal (Only for my screen size!)
* Antivirus scanner for .SHL files
* Has very basic conditionals and loops

## Usage:

./src/everything.py should do the trick, but I recomend you to create a spin-off (see tests/spinoffs) and run it for understanding the source code and ultimate customization!

## Known bugs:

###### IF command dosen't work!

###### LOOP syntax is very difficult to use, a missing space will make the statement useless. Should be solved soon
