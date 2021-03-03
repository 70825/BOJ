#include <stdio.h>
int a=0,b=0;
int k(int x);
void z(int y,int a);
int main(void)
{
	int x,y;
	scanf("%d %d",&x,&y);
	if(1<=x<=12&&1<=y<=31)
	{
		k(x);
		z(y,a);
	}

	return 0;
}

int k(int x)
{
	for(b=x-1;b>0;b--)
	{
		if(b==1||b==3||b==5||b==7||b==8||b==10||b==12)
			a+=31;
		else if(b==4||b==6||b==9||b==11)
			a+=30;
		else if(b==2)
			a+=28;
		else
			break;
	}
	return a;
}

void z(int y,int a)
{
	b=(y+a)%7;
	if(b==1)
		printf("MON");
	else if(b==2)
		printf("TUE");
	else if(b==3)
		printf("WED");
	else if(b==4)
		printf("THU");
	else if(b==5)
		printf("FRI");
	else if(b==6)
		printf("SAT");
	else
		printf("SUN");
}