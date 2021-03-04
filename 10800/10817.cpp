#include <stdio.h>
int main(void)
{
	int a,b,c;
	scanf("%d %d %d",&a,&b,&c);

	if(1<=a,b,c&&a,b,c<=100)
	{
		if(a<=b&&b<=c||a>=b&&b>=c)
			printf("%d",b);
		else if(a<=c&&c<=b||a>=c&&c>=b)
			printf("%d",c);
		else if(c>=a&&a>=b||c<=a&&a<=b)
			printf("%d",a);
	}

	return 0;
}