import "../../src/everything.py" as E # imports main module

def cmd_test(args):
  E.pie("Test function called")

E.COMMANDS["TEST"] = {"args":[],"shell":"*","screen":0,"exec":cmd_test} # Insert newly made command into command store

E.PROMPT = ">>> " # Change prompt

E.repl() # Start main REPL process
