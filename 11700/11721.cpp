#include <stdio.h>
#include <string.h>
int main(void)
{
	int i;
	char a[100]={0,};
	scanf("%s",a);

	for(i=0;i<strlen(a);i++)
	{
		printf("%c",a[i]);
		if(i!=0&&(i+1)%10==0)
			printf("\n");
	}
	
	return 0;
}