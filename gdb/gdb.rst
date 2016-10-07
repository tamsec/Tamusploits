GDB Basic Tutorial
==================

Setup
-----
You will need access to:  
Linux distribution of your choice with gcc and gdb installed  

Compile Code
++++++++++++
In order to debug an executable you must first find or create one.  
In this example we will be using the following code:  

.. literalinclude:: example.c

Now time to compile the program.  
In order for gdb to read symbols (names of variables, functions and types) from your program you need to compile the program with the `-g` flag. The `-o` flag gives the compiled executable the name that you pass it.

.. code-block:: console
	#gcc -g example.c -o exWithSymbols

