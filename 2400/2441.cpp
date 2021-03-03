#include <stdio.h>
int main(void)
{
	int a,b,i,N;
	scanf("%d",&N);
	if(1<=N<=100)
	{
		for(i=1;i<=N;i++)
		{
			a=N-i+1;
			b=i-1;
			while(b>0)
			{
				printf(" ");
				b--;
			}

			while(a>0)
			{
				printf("*");
				a--;
			}
			printf("\n");
		}	
	}
	return 0;
}