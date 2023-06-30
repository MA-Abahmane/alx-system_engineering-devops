#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
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
int i = 0;
pid_t chld_PID;
int zombies_to_make = 5

while (i < zombies_to_make)
{
chld_PID = fork();

if (chld_PID > 0)
{
printf("Zombie process created, PID: %d\n", chld_PID);
sleep (1);
i++;
}
else
{
exit (0);
}
}

infinite_while();
return (EXIT_SUCCESS);
}
