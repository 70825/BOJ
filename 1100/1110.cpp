#include <stdio.h>
int main(void)
{
	int N,a=0,b=0,c=0,d=0,i=0;
	scanf("%d",&N);
	if(0<=N&&N<=99)
	{
		d=N;
		while(1)
		{
			a=d/10;
			b=d%10;
			c=(a+b)%10;
			d=(b*10)+c;
			if(d!=N)
			{
				i++;
				continue;
			}
			else if(d==N)
			{
				i++;
				break;
			}
		}
		printf("%d",i);
	}
	return 0;
}
