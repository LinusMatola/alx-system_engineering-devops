#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

/**
 * main - zombies
 *
 * Description: make five zombies
 * Return: 0 for success
 */
int main(void)
{
	int i;
	pid_t ZOMBIE_PID;

	i = 0;
	while (i < 5)
	{
		pidme = fork();
		if (ZOMBIE_PID)
			printf("Zombie process created, PID: %i\n", ZOMBIE_PID);
		else
			exit(0);
		i++;
	}
	sleep(100);
	return (0);
}
