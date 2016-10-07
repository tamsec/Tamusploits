#include <stdio.h>

void function1();
void function2();
void function7();
void secret();

int main(int argc, char** argv)
{
	int x = 0;
	int secretFlag = 0;
	char words[] = "Hello, world!";
	
	printf("%s\n", words);
	
	if(secretFlag)
		secret();
	
	function1();
	x = 6;
	function2();

	if(x == 7)
		function7();
}

void function1()
{
	printf("In function 1\n");
}

void function2()
{
	printf("In function 2\n");
}

void function7()
{
	printf("In function7\n");
}

void secret()
{
	printf("Luke, I am your Father!\n");
}