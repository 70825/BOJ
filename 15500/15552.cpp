#include <stdio.h>
int main(void)
{
	int T,i,A,B;
	int a[]={0,};
	int b[]={0,};

	scanf("%d",&T);
	for(i=0;i<T;i++)
	{
		scanf("%d %d",&A,&B);
		printf("%d\n",A+B);
	}

	return 0;
}