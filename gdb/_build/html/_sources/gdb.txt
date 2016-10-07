GDB Basic Tutorial
==================
Gdb is the GNU Project debugger. It allows you to do things like run the program up to a certain point then stop and print out the values of certain variables at that point, or step through the program one line at a time and print out the values of each variable after executing each line. It uses a command line interface. The program being debugged can be written in many languages including Ada, C, C++, Objective-C, Pascal.  
You can learn more about it `Here. <https://www.gnu.org/software/gdb/>`_

Setup
-----
The examples in this tutorial will be done using a Linux console.

Compile Code
++++++++++++
In order to debug an executable you must first find or create one.  
In this example we will be using the following code:  

.. literalinclude:: example.c

Now time to compile the program.  
In order for gdb to read symbols (names of variables, functions and types) from your program you need to compile the program with the `-g` flag. The `-o` flag gives the compiled executable the name that you pass it. Here is an example:  

.. code-block:: console
	
	# gcc -g example.c -o exWithSymbols


Basic Debugging
---------------
Now it is finally time to start debugging! 
Here are some basic commands to get your way around gdb.

Starting GDB
++++++++++++
Here is how to start gdb:  

.. code-block:: console

	# gdb exWithSymbols

The console will look something like this:  

.. figure::	images/gdbStart.png
   :align:  center

Before we start running the program we are going to learn about a few commands first.  

List
++++
The `list` command by default prints out 10 lines of code to the console. This can be changed with `set listsize <count>`. This is very useful whenever you are using the console to write and edit code because it allows you to not have to quit gdb in order to look at the code.

.. figure::	images/list.png
   :align:  center

`list` can also be used display starting at a certain line number, range of lines, or function with `list <line number>`, `list <starting line>, <ending line>` or `list <function name>`  
Examples:

.. figure::	images/listRange.png
   :align:  center

.. figure::	images/listFunction.png
   :align:  center


Breakpoints
+++++++++++
Breakpoints are what allow you to pause, or break, a program when it reaches a certain line or function. When you reach a breakpoint while debugging a program you can examine and change variables before resuming execution. To set a breakpoint run `break <line number>` or `break <function name`. To continue after a breakpoint use the `continue` command. To delete a breakpoint user either `clear` to delete all breakpoints or `delete <breakpoint number>` to delete a specific breakpoint.  
Examples:  

.. figure::	images/break.png
   :align:  center

Run
+++
Now that we have some basics down we are going to run the program. In order run the program use the command `run`. To run the program with arguments you can either pass them in the command line `run <arg1> <arg2> <argN>` or you can set the arguments that the program will run with everytime with `set args <arg1> <arg2> <argN>`

.. figure::	images/run.png
   :align:  center

Notice how the program stopped at Breakpoint 2 which is the function main(). From here we can see some basic info already such as the breakpoint number, function currently being run and its arguments, and the current line number of the file we are in. Lets continue to the next breakpoint before looking around.

.. figure::	images/continue.png
   :align:  center

While the program was executing it printed out the first print statement "Hello, world!".  

Print
+++++
Now that we can start examining variables and arguments. In order to look at what is currently stored in a variable use the `print` command. To print a variable simply run `print <variable name>` if you would like to display the variable in different formats you can run the command `print/format <variable name>`

.. figure::	images/print.png
   :align:  center

Stepping
++++++++
Stepping allows us to move around in the program line by line without having to set a breakpoint at every line. The `step` command goes to the next instruction and enters into functions that it reaches. The `next` command goes to the next instruction but does not enter into functions that it reaches.

.. figure::	images/stepping.png
   :align:  center

Notice how when I reached function2() in main I used `step` instead of `next` and gdb started displaying the code insided of function2().

Backtrace
+++++++++
Backtrace is useful for when you want to see what functions have been called to get to where you are now in the code. The command is simply `backtrace`. One common way of using this is to help figure out segmentation faults. When you reach a seg fault the call stack is still preserved so you can still run commands like `backtrace` and `print` in order to figure out what caused the crash.

.. figure::	images/backtrace.png
   :align:  center

Changing Variables
++++++++++++++++++
Variables can be changed in run time with gdb. This can be useful when you want to see how a program will react with the variable changed. This is done with `set var <variable name> = <new value>`.

.. figure::	images/setvar.png
   :align:  center

Tips
----
Every command can be shortened to the point that gdb can still distinguish it from other commands. For example `run` can be shortened `r` or `backtrace` can be shortened to just `bt`.
 
Conclusion
----------
You have now learned some of the basic fundamentals of using gdb to debug programs. Knowing how to use gdb can be very useful when you are trying to debug a program through the command line. There are also several other features that are useful when reversing a program. In the next tutorial I will show you how to do some cool stuff with basic reversing using gdb.