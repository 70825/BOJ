#include <stdio.h>
int main(void)
{
	int a,N;
	scanf("%d",&N);

	if(N<=100000)
		for(a=N;a>0;a--)
			printf("%d\n",a);

	return 0;
}