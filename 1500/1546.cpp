#include <stdio.h>
int main(void)
{
	int n,i,max;
	double a=0;
	int arr[1000]={0,};
	double arr1[1000]={0,};
	scanf("%d",&n);
	if(n<1000)
	{
		for(i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
			if(arr[i]<0||arr[i]>100)
				return 0;
		}
		max=arr[0];
		for(i=1;i<n;i++)
		{
			if(arr[i]>max)
				max=arr[i];
		}
		if(max==0)
			return 0;
		for(i=0;i<n;i++)
		{
			arr1[i]=(double)arr[i]/max*100;
			a+=arr1[i];
		}
		printf("%.2f",a/n);
		
	}
return 0;
}