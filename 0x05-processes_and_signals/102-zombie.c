#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>


int main()
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
}