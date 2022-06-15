#include<stdio.h>
#include<stdbool.h>
int main(){
	float temp=25;
	bool sunny=true;
	if(temp>=10&&temp<=45&&sunny){
		printf("The Weather is good");
	}
	else{
		printf("The weather is bad");
	}
	return 0;
}
