#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>

/**
* infinite_while - runs an infinit loop
*
* Return: it has a return but it will never reach it
*/
int infinite_while(void)
{
while (1)
{
sleep(1);
}
return (0);
}


/**
* main - the main method
*
* Return: 1 in success/ 0 in failure
*/
int main(void)
{
int zombies_to_make = 5;

for (int i = 0; i < zombies_to_make; i++)
{
pid_t chld_PID;

chld_PID = fork();

if (chld_PID > 0)
{
printf("Zombie process created, PID: %d\n", chld_PID);
}
else if (chld_PID == 0)
{
return (0);
}
else
{
printf("fork failed");
return (-1);
}
}

infinite_while();
return (0);
}
