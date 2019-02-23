#!/usr/bin/env python3

"""

Multipurpose Shell

FEATURES:

5+ Types of shells: MAIN, FILE, WRITER, WEB, ANTIVIRUS

Supports batching commands in a *.SHL file

40+ Commands supported!

COMMANDS:

WHOAMI : Who are you? Find out!

WHOOWNS [path] : Finds owner of path

AVIRUS [?path] [?virustype] [?~del] [?~look] : The antivirus, Goto Antivirus shell by default

MK [path] : Creates the path, ending / for dirs

RM [path] [?~p] : Removes the end dir or file of path, if ~p, removes entire path

FIND [regex] [?start] [?stop] [?~fn] : Looks at content inside files and display the matches in current dir, ~fn for just scanning file name

REPLACE [regex] [string] [?path] [?~o] [?~p] : Replaces the regex with the text in all the files in the current dir, path to put the specific file

DISK [?OPEN/CLOSE] : Opens / Closes the disk drive

WWW [?website] [?~j] [?~c] : Starts a WWW shell, javascript and CSS3 optionally enabled

PRINT [...text] : Prints text

IF [condition] {block}








"""


from os import remove,mkdir,listdir,system,chdir,getcwd
from os.path import isfile,isdir
import importlib
from random import *
from curses import *
from time import sleep
from sys import argv
import asyncio



# KERNEL DATA
class Kernel:
	def __init__(self):
		self.__initd = []
		self.__encrypt_kernel()
		pass
	
	def AccessInit(self,passcode = None,variable = None):
		if passcode != 1608:
			return False

		globals()[variable] = self.__initd

		return True

	def __encrypt_kernel(self):
		alp = list("qwertyuiopasdfghjklzxcvbnm")
		genlist = []
		buff = ""
		for blah in range(0,100): 
			for whatever in range(0,30):
				buff += random.choice(alp)
			genlist.append(buff)
			buff = ""

		for v in genlist:
			eval("self.__" + v + " = \"" + v +"\"")

	def RandomizeMemoryLocations(self,passcode):
		if passcode != 1608:
			return False
		initd = self.__initd
		enckrnl = self.__encrypt_kernel
		del self.__initd
		del self.__encrypt_kernel
		self.__initd = initd
		self.__encrypt_kernel = enckrnl
		self.__encrypt_kernel()










# ANTIVIRUS DATA

DANGEROUS_SNIPPETS = ["DELETE C:\\Windows\\System32","DELETE C:/Windows/System32","DELETE everything.py","WRITE 0 everything.py","WRITE 0 C:\\Windows\\System32\\hal.dll","DELETE C:\\Windows","DELETE C:\\Windows\\py.exe","WRITE 0 C:\\Windows\\py.exe","LOOP FOREVER { WRITE %READ:1;everything.py% everything.py }","DELETE env.pyw","LOOP FOREVER { } "]
DANGEROUS_PATHS = ["C:\\Windows\\System32","C:\\Windows","/","C:/Windows/System32","everything.py","env.pyw"]
ERROR_PROTECTION = True
REAL_TIME_PREVENTION = False
LOG_ACTIONS = False
VARIABLE_INTEGRITY = False
CAN_FLASH = True
CAN_IMPORT_MODULES = True

SHELL = "MAIN"
SCREEN = 0
SCROBJ = None
VARS = {}
ECHO = True
PROMPT = "#$>"
DEBUG = True
PARSE_INBLOCK = False
PARSE_BLOCKLVL = 0
MODULES = []
DEBUG_TAG = "DEBUG: "
ECHO_TAG = ""
DEBUG_LOGS = []
COMMAND_LOGS = []
OUTPUT_LOGS = []

def pie(ar):
	if ECHO:
		print(ECHO_TAG+ar)
		
	OUTPUT_LOGS.append(ar)

def deb(ar):
	if DEBUG:
		print(DEBUG_TAG + ar)
		DEBUG_LOGS.append(ar)
	
def PREPROCESSER(cmd,args):
	...

def DANGEROUS_PATH_HANDLER(dpath,cmd):
	...

def EXECPTION_HANDLER(e,last_cmd,last_args):
	...

def SCAN_HANDLER(filname,content):
	...


# Parser funcs

def parser_input(arg):
	return input(str(arg))


# Parser for parsing some % funcs

PARSERS = {
	"INPUT" : {"args":["str"],"exec":parser_input}
}



####### CHATBOT IMPL ######

def cmd_chatbot():
	raise NotImplementedError
	
####### ASYNC FUNCTION ######

async def async_alert():
	while True:
		try:
			PREP("ALERT")
		except expression as Execption:
			return




# BEGIN [FUNC]:


def extract_varstr(st):
	global PARSE_INBLOCK,PARSE_BLOCKLVL
	st = st.replace("_"," ")
	st = st.replace("__","_")
	sts = list(st)
	invars = False
	varreplace = []
	buff = ""
	deb("parsing string: " + st)
	for i in range(len(sts)):
		if sts[i] == "{":
			deb("A block has started")
			PARSE_INBLOCK = True
			PARSE_BLOCKLVL += 1

		if sts[i] == "}":
			deb("A block has ended")
			if PARSE_BLOCKLVL == 1:
				deb("Exited all blocks, starting processing...")
				PARSE_BLOCKLVL = 0
				PARSE_INBLOCK = False
			else:
				deb("Exited nested block")
				PARSE_BLOCKLVL -= 1


		if(sts[i] == "%" and not PARSE_INBLOCK):
			if invars:
				varreplace.append(buff)
				deb(buff + " :% literal found in string")
				buff = ""
				invars = False
				deb("% literal ended")
				continue
			else:
				deb("% literal begin")
				invars = True
				continue
			

		if(invars and not PARSE_INBLOCK):
			buff = buff + sts[i]
	
	for i in varreplace:
		if "@" in i:
			the_pcmds = i.split("@")[1]
			the_cmd = the_pcmds.split(":")[0]
			the_arg = (the_pcmds.split(":")[1]).split(";")[1]
			deb("Found parser @"+the_cmd+" with argument "+the_arg)

			for key in PARSERS:
				if key == the_cmd:
					val = PARSERS[key]["exec"](the_arg)
					st = st.replace("%"+i+"%",val)
					continue

			deb("Parser for "+the_cmd+" not found")
			continue

		if(not i in VARS):
			deb("The variable "+i+" is not found in the global variable store")
			st = st.replace("%"+i+"%","NULL")
			continue
		st = st.replace("%"+i+"%",str(VARS[i]))
		
	return st




def extract_args(this_thing):
	if not this_thing.find(" "):
		return {"command":this_thing,"arg_count":0,"args":None}
	extracted_thing = this_thing.split(" ")
	this_command = extracted_thing[0]
	args_of_thing = extracted_thing
	args_of_thing.pop(0)
	arg_count = len(args_of_thing)
	return {"command":this_command,"arg_count":arg_count,"args":args_of_thing}

def resolve_type(tstr):
	strl = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_$?<>!@#$%^&()[]{}`~.':;|,\\=\"\n\a\t")
	ot = tstr
	tlist = list(tstr)
	if ot == "" or ot == "\t":
		deb(ot + " is nothing. Skipping now")
		return "<<<SKIP>>>"
	if(tlist[0] == "$"):
		tlist.pop(0)
		tlist = "".join(tlist)
		deb(ot + " is a integer->string")
		return tlist
	deb("String char set: " + "".join(strl))
	for i in range(len(strl)):
		if(strl[i] in ot):
			deb(ot + " is a string")
			deb(ot + " contained the char of " + strl[i])
			return str(ot)
	deb(ot + " is a integer")
	if tlist[0] == "-":
		deb("Negative integer detected")
		tlist.pop(0)
		return int("".join(tlist)) * (-1)
	return int(ot)
	
def ck_type(arr_of_vals,arr_of_types):
	for i in range(len(arr_of_vals)):
		if(not type(arr_of_vals[i]) == arr_of_types[i]):
			return False


def parse_args(args):
	arg = []
	for i in range(len(args)):
		
		deb(str(args[i]) + "is the value of the raw argument....")
		args[i] = extract_varstr(args[i])
		deb(str(args[i]) + "is the value of the parsed argument....")
		a = resolve_type(args[i])
		arg.append(a)
		a = resolve_type(args[i])
		if a == "<<<SKIP>>>":
			continue
	return arg


def parse_newline(tstr):
	deb("Begin parsing newlines...")
	tstr = tstr.replace("\t","")
	arr = list(tstr)
	in_block = False
	block_counter = 0
	for i in range(len(arr)):
		if arr[i] == "{":
			deb("Entered a block")
			in_block = True
			block_counter += 1
			continue

		if arr[i] == "}":
			if block_counter == 1:
				deb("Exited all blocks. Resuming newline processing")
				in_block = False
				block_counter -= 1
			else:
				deb("Exited a nested block")
				block_counter -= 1
			continue

		if (not in_block) and  arr[i] == "\n":
			deb("Newline found!")
			arr[i] = "<<<SPLIT>>>"

	al = "".join(arr).split("<<<SPLIT>>>")
	return al

def parse_prompt(prompt):
	prompt = prompt.replace("$(GREEN)[[","\033[92m")
	prompt = prompt.replace("$(RED)[[","\033[91m")
	prompt = prompt.replace("$(YELLOW)[[","\033[93m")
	prompt = prompt.replace("$(UNDERLINE)[[","\033[4m")
	prompt = prompt.replace("]](END)$","\033[0m")
	prompt = prompt.replace("$(SHELL)[[]]",SHELL)
	return prompt

def parse_module(cmd,args):
	for i in MODULES:
		if i["COMMAND"] == cmd and i["SHELL"] == SHELL:
			deb("Found command in a module")
			return i["FUNC"](args)
	deb("Command not found in any modules")
	return None

def import_module(export):
	if not CAN_IMPORT_MODULES:
		return pie("UAC prevented import of modules")
	for i in export:
		if "COMMAND" in i and "SHELL" in i and "FUNC" in i and type(i["FUNC"]) == type(parse_newline) and type(i["COMMAND"]) == type("") and type(i["SHELL"]) == type(""):
			deb("Valid module. Importing now")
			MODULES.append(i)
		else:
			deb("Invalid module")
			continue

def change_prompt(new):
	global PROMPT
	PROMPT = new


def prep(cmd):
	try:
		cmd_chain = extract_args(cmd)
		the_cmd = cmd_chain["command"]
		the_args = cmd_chain["args"]
		parsed_args = parse_args(the_args)
		COMMAND_LOGS.append({"command":the_cmd,"args":the_args})
		PREPROCESSER(the_cmd,the_args)
		return main_parse(the_cmd,parsed_args)
	except Exception as e:
		cmd_panic([str(e),cmd])





# COMMANDS

def cmd_print(args):
	deb("Command refrenced a PRINT statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	for i in range(len(args)):
		pie(args[i])


def cmd_var(args):
	global VARS
	deb("Command refrenced a VAR statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 2:
		pie("ERROR: Assignments asks exactly 2 arguments, [varname] and [varvalue]. None are optional")
		return
	VARS[args[0]] = args[1]
	pie("Assigned " + str(args[1]) + "to " + str(args[0]))

def cmd_loop(args):
	global VARS
	deb("Command refrenced a LOOP statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not args[1] == "{" and args[len(args)-1] == "}":
		pie("ERROR: A loop expects a block to follow the number, no block was given. LOOP [number<Int,FOREVER>] {block<Str>}. A block is not optional")
		deb("ArgumentError: Block expected, found none")
		return
	loopt = args[0]
	if (loopt == "FOREVER"):
		loopt = 10**10
	VARS["ITIR"] = 1
	args.pop(0) 
	args.pop(0)
	args.pop(len(args) - 1)
	for i in range(len(args)):
		args = str(args)
	cmd = " ".join(args)
	cmdl = cmd.split("\n")
	for blahblahblabubufbucbuebubcuebcuecbuebcucudcb3uc in range(0,loopt):
		for i in range(len(cmdl)):
			prep(cmdl[i])
		VARS["ITIR"] += 1
	del VARS["ITIR"]
	deb("Done loop")

def cmd_if(args):
	global VARS
	deb("Command refrenced a IF statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not args[2] == "{" and args[len(args)-1] == "}":
		pie("ERROR: A if statment expects a block to follow the two values, no block was given. IF [asvalue1] [asvalue2] {block}. A block is not optional")
		deb("ArgumentError: Block expected, found none")
		return
	as1 = args[0]
	as2 = args[1]
	args.pop(0) 
	args.pop(0)
	args.pop(0)
	args.pop(len(args) - 1)
	for i in range(len(args)):
		args = str(args)
	cmd = " ".join(args)
	cmdl = cmd.split("\n")
	if as1 == as2:
		deb("ASSERT is TRUE")
		for i in cmdl:
			prep(i)
	deb("Done if")

def cmd_parse(args):
	deb("Command refrenced a PARSE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. PARSE [filename]. The arguments are not optional")
		return
	file = args[0]
	deb("File name: " + file)
	try:
	  	a = open(file,"r")
	  	c = a.read()
	  	a.close()
	except Exception as e:
	  	pie("ERROR: Invalid filename")
	  	deb("TRUE ERROR: " + str(e))
	else:
		c = parse_newline(c)
		deb("CODE: " + str(c))
		for i in c:
			prep(i)

def cmd_write(args):
	deb("Command refrenced a WRITE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 2:
		pie("ERROR: Statement expected two and only two argument passed to it. WRITE [text] [filename]. The arguments are not optional")
		return

	file = str(args[1])
	text = str(args[0])

	if REAL_TIME_PREVENTION:
		for i in DANGEROUS_PATHS:
			if file == i:
				DANGEROUS_PATH_HANDLER(file,"WRITE")
				deb("UAC Prevented access of this path: " + i)
				return
	try:
		a = open(file,"w+")
		deb(file + " is present or created...")
		a.write(text)
		a.close()
	except Exception as e:
		pie("ERROR: Error in writing file")
		deb("TRUEERROR: " + str(e))
	else:
		deb("Success writing " + text + "to " + file + ".")

def cmd_inc(args):
	deb("Command refrenced a INC statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not (len(args) == 1 or len(args) == 2):
		pie("ERROR: Statement expected two or one argument(s) passed to it. INC [var] [?step=1]. The last argument is optional")
		return

	if len(args) == 1:
		deb("The incrementation value is 1")
		inc = 1
	else:
		deb("The incrementation value is " + str(args[1]))
		inc = args[1]

	VARS[args[0]] = VARS[args[0]] + int(inc)

def cmd_dec(args):
	deb("Command refrenced a DEC statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not (len(args) == 1 or len(args) == 2):
		pie("ERROR: Statement expected two or one argument(s) passed to it. DEC [var] [?step=1]. The last argument is optional")
		return

	if len(args) == 1:
		inc = 1
	else:
		inc = int(args[1])

	VARS[args[0]] = VARS[args[0]] - int(inc)


def cmd_delete(args):
	deb("Command refrenced a DELETE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. DELETE [filename]. The arguments are not optional")
		return

	file = str(args[0])
	if REAL_TIME_PREVENTION:
		for i in DANGEROUS_PATHS:
			if file == i:
				DANGEROUS_PATH_HANDLER(file,"DELETE")
				deb("UAC Prevented access of this path: " + i)
				return

	try:
		remove(file)
	except Exception as e:
		pie("ERROR: Error while deleting the file")
		deb("TRUEERROR: " + str(e))
	else:
		deb("Successfully deleted " + str(file))

def cmd_avirus(args):
	deb("Command refrenced a AVIRUS statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	global SHELL
	SHELL = "ANTIVIRUS"
	deb("To antivirus shell")
	pie("Welcome to the SHL Antivirus!")
	if len(args) == 0:
		return
	else:
		pass


def cmd_prompt(args):
	deb("Command refrenced a PROMPT statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. PROMPT [prompt]. The arguments are not optional")
		return

	global PROMPT

	PROMPT = args[0]
	deb("Changed the promptstring to " + str(args[0]))

def cmd_use(args):
	deb("Command refrenced a USE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. USE [module]. The arguments are not optional")
		return
	module = ""+str(args[0])+""
	
	try:
		__import__(module)
		importlib.import_module("EXPORTS",module)
	except Exception as e:
		pie("ERROR: Error parsing module")
		deb("TRUEERROR: "+str(e))
	else:
		import_module(EXPORTS)
		del EXPORTS
		return 0

def cmd_screen(args):
	deb("Command refrenced a SCREEN statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. SCREEN [number]. The arguments are not optional")
		return
	global SCREEN,SCROBJ,PROMPT,ECHO,DEBUG
	SCREEN = int(args[0])
	SCROBJ = initscr()
	if int(args[0]) == 0:
		nocbreak()
		SCROBJ.keypad(False)
		endwin()
		curs_set(True)
		deb("Screen returned to its original operating mode")
		PROMPT = "$> "
		ECHO = True
		DEBUG = True
		endwin()
		endwin()
	else:
		deb("If you are seeing this, it is not working!")
		SCROBJ = initscr()
		noecho()
		cbreak()
		curs_set(False)
		SCROBJ.keypad(True)
		start_color()
		PROMPT = ""
		DEBUG = False
		ECHO = False
		SCROBJ.clear()
		SCROBJ.border(0,0,0,0,0,0,0,0)
		SCROBJ.addstr(0,67,"GRAPHICS MODE",A_BOLD)
		SCROBJ.refresh()
		

def cmd_putchar(args):
	deb("Command refrenced a PUTCHAR statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 3:
		pie("ERROR: Statement expected three and only three arguments passed to it. PUTCHAR [xpos] [ypos] [char]. The arguments are not optional")
		return

	if SCREEN == 0:
		pie("ERROR: PUTCHAR is not supported in SCREEN 0")
		return

	SCROBJ.addch(args[1],args[0],str(args[2]))
	SCROBJ.refresh()

def cmd_putline(args):
	deb("Command refrenced a PUTLINE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 3:
		pie("ERROR: Statement expected three and only three arguments passed to it. PUTLINE [xpos] [ypos] [line]. The arguments are not optional")
		return

	if SCREEN == 0:
		pie("ERROR: PUTLINE is not supported in SCREEN 0")
		return

	SCROBJ.addstr(args[1],args[0],str(args[2]))
	SCROBJ.refresh()

def cmd_delay(args):
	deb("Command refrenced a DELAY statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 1:
		pie("ERROR: Statement expected one and only one argument passed to it. DELAY [time]. The arguments are not optional")
		return
	if SCREEN == 0:
		sleep(int(args[0]))
	else:
		napms(int(args[0])*1000)

def cmd_clear(args):
	deb("Command refrenced a CLEAR statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if SCREEN == 0:
		null = system("clear")
	else:
		SCROBJ.clear()


def cmd_alert(args):
	deb("Command refrenced a ALERT statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	flash()
	print("\a")
	sleep(0.75)
	flash()
	print("\a")

def cmd_shutdown(args):
	deb("Command refrenced a SHUTDOWN statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	while(True):
		sleep(0.25)
		flash()
		print("\a")


def cmd_pause(args):
	deb("Command refrenced a PAUSE statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if SCREEN == 0:
		input()
	else:
		SCROBJ.getch()
	

def cmd_panic(args):
	deb("Command refrenced a PANIC statment")
	deb("There are total of " + str(len(args)) + " passed to this statement" )
	if not len(args) == 2:
		pie("ERROR: Statement expected two and only two arguments passed to it. PANIC [error] [command]. The arguments are not optional")
		return
		
	if len(args[0]) > 150:
		args[0] = "<..too large to show>"

	if len(args[1]) > 100:
		args[1] = "<Cannot retrive>"
	global SCROBJ,SCREEN,DEBUG,ECHO,PROMPT
	SCROBJ = initscr()
	noecho()
	cbreak()
	curs_set(False)
	SCROBJ.keypad(True)
	start_color()
	PROMPT = ""
	DEBUG = False
	ECHO = False
	SCROBJ.clear()
	SCROBJ.border(0,0,0,0,0,0,0,0)
	SCROBJ.addstr(0,65,"PANIC MODE",A_BOLD)
	SCR_Y = SCROBJ.getmaxyx()[0]
	SCROBJ.addstr(SCR_Y-1,13,"C:Continue,H:Halt,D:Halt+Dump",A_BOLD)
	SCROBJ.addstr(3,59,"Fatal error in program",COLOR_RED)
	SCROBJ.addstr(5,30,"Command:"+args[1])
	SCROBJ.addstr(15,5,"Error: "+str(args[0]),A_BLINK)
	SCROBJ.refresh()


	def tempfs():
		ans = SCROBJ.getkey()
		if ans == "C":
			prep("SCREEN 0")
			return

		elif ans == "H":
			prep("SCREEN 0")
			exit()
		elif ans == "D":
			print(DEBUG_LOGS)
			prep("SCREEN 0")
			exit()
		else:
			tempfs()

	tempfs()
	del tempfs
		

# ANTIVIRUS FUNCTIONS


def avirus_scan(args):
	ll = listdir(getcwd())
	ret = True
	if not (len(args) == 0 or len(args) == 1):
		if (len(args) == 2):
			if(args[1] != ""):
				ret = False
				ll = listdir(args[1])
			else:
				ret = True
				
		else:
			ret = True
		if ret:
			pie("ERROR: Statement expected zero or one argument passed to it. SCAN [?filename] [!dir]. All arguments are optional")
			return

	if len(args) == 1:
		file = args[0]
		try:
			a = open(file,"r")
			b = a.read()
			a.close()
		except Exception as e:
			pie("ERROR: Error while reading file")
			pie("0 of 1 Files scanned")
			deb("TRUEEERROR: " + str(e))
		else:
			for i in DANGEROUS_SNIPPETS:
				if i in b:
					pie("1 of 1 Files scanned")
					pie("1 of 1 files are malicious")
					pie("Malicious file(s) " + file)
					pie("Recommended actions: DISINFECT")
					deb("Found " + i + "in file.")
					return
			pie("1 of 1 Files scanned")
			pie("0 of 1 files are malicious")
			pie("Recommedned actions: none")
	else:
		FILE_NUM = 0
		MAL_FILES = []
		for i in ll:
			if isdir(i):
				deb(i + "is a directory...")
				continue
			elif isfile(i):
				if not ".SHL" in i:
					deb("Non shell file... : " + i)
					continue
				FILE_NUM += 1
				a = open(i)
				b = a.read()
				a.close()
				deb("Content of " + i + " is : \"" + b + "\"")
				SCAN_HANDLER(i,b)
				for q in DANGEROUS_SNIPPETS:
					if q in b:
						if not i in MAL_FILES: 
							deb("HIT! "+ i + " Contains" + q)
							MAL_FILES.append(i)

				pie(str(FILE_NUM) + " of " + str(FILE_NUM) + "files and directories scanned")
				pie("There are " + str(len(MAL_FILES)) + " malicious files")
				pie("FILES: " + " , ".join(MAL_FILES))
				return MAL_FILES

def avirus_clean(args):
	the_malicious_files = prep("SCAN")
	for i in the_malicious_files:
		deb("Cleaning file: " + i)
		remove(i)

# MAIN CALL


COMMANDS = {
	"PRINT" : {"args":["any"],"shell":"MAIN","screen":0,"exec":cmd_print},
	"VAR" : {"args":["any","any"],"shell":"MAIN","screen":-1,"exec":cmd_var},
	"LOOP" : {"args":["any","block"],"shell":"MAIN","screen":-1,"exec":cmd_loop},
	"PARSE" : {"args":["any"],"shell":"MAIN","screen":-1,"exec":cmd_parse},
	"WRITE" : {"args":["str","str"],"shell":"MAIN","screen":-1,"exec":cmd_write},
	"INC" : {"args":["var","*int"],"shell":"MAIN","screen":-1,"exec":cmd_inc},
	"DELETE" : {"args":["str"],"shell":"MAIN","screen":-1,"exec":cmd_delete},
	"DELAY" : {"args":["int"],"shell":"MAIN","screen":-1,"exec":cmd_delay},
	"AVIRUS" : {"args":[],"shell":"MAIN","screen":-1,"exec":cmd_avirus},
	"EXIT" : {"args":["str","str"],"shell":"MAIN","screen":-1,"exec":exit},
	"USE" : {"args":["str"],"shell":"MAIN","screen":-1,"exec":cmd_use},
	"REBOOT" : {"args":[],"shell":"MAIN","screen":-1,"exec":lambda x: system("py everything.py")},
	"PROMPT" : {"args":["str"],"shell":"MAIN","screen":0,"exec":cmd_prompt},
	"PAUSE" : {"args":["int"],"shell":"MAIN","screen":-1,"exec":cmd_delay},
	"SCREEN" : {"args":["int"],"shell":"MAIN","screen":-1,"exec":cmd_screen},
	"PUTCHAR" : {"args":["int","int","str"],"shell":"MAIN","screen":1,"exec":cmd_putchar},
	"PUTLINE" : {"args":["int","int","str"],"shell":"MAIN","screen":1,"exec":cmd_putline},
	"ALERT" : {"args":[],"shell":"MAIN","screen":-1,"exec":cmd_alert},
	"SHUTDOWN" : {"args":[],"shell":"MAIN","screen":-1,"exec":cmd_shutdown},
	"CLEAR" : {"args":[],"shell":"MAIN","screen":-1,"exec":cmd_clear},
	"DEC" : {"args":["str","*int"],"shell":"MAIN","screen":-1,"exec":cmd_write},
	"IF" : {"args":["any","any","block"],"shell":"MAIN","screen":-1,"exec":cmd_if},
	"SCAN" : {"args":["*str"],"shell":"ANTIVIRUS","screen":-1,"exec":avirus_scan},
	"PANIC" : {"args":["str"],"shell":"*","screen":-1,"exec":cmd_panic}
}












def main_parse(cmd,args):
	global SHELL
	deb("The command is " + str(cmd))
	deb("The arguments are " + str(args))

	for key in COMMANDS:
		if cmd == key:
			if SHELL == COMMANDS[key]["shell"] or COMMANDS[key]["shell"] == "*":
				return COMMANDS[key]["exec"](args)

	return parse_module(cmd,args)

# REPL CALL

def repl():
	if len(argv) != 1:
		prep("PARSE "+argv[1])
		print (DEBUG_LOGS)
		exit()
	prep("PARSE STARTUP.SHL")
	global SCROBJ
	SCROBJ = initscr()
	endwin()
	while True:
		PPP = input(parse_prompt(PROMPT))
		try:
			prep(PPP)
		except Exception as e:
			EXECPTION_HANDLER(e,PPP,[])
			deb("Fatal error in program")
			prep("SCREEN 0")
			if ERROR_PROTECTION:
				if (len(str(e)) > 150):
					e = "<Too long to display>"
				cmd_panic([str(e),PPP])
				prep("SCREEN 0")
				deb(str(e))
				pass
			else:
				pie(str(e))
				exit()
		




if __name__ == '__main__':
	repl()
	print (DEBUG_LOGS)
else:
	# Compiler tools?
	pass
	
