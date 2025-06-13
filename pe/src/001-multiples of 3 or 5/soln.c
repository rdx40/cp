#include <stdio.h>

int sum(int n, int a){
	int m = (int)((n-1)/a);
	return (int)(a*m*(m+1)/2);
}
int main(){
	printf("%d\n",sum(1000, 3) + sum(1000, 5) - sum(1000, 15));
}
