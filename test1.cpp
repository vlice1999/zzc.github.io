#include <stdio.h>
int main(){
	int num,M,step,head;
	int nums[100][100];
	int nums_m[100];
	scanf("%d",&num);
	for(int o=0;o<num;o++){
		scanf("%d%d",&M,&step);
		nums_m[o]=M;
		for(int i=0;i<M;i++){
			scanf("%d",&nums[o][i]);
		}
		for(int i=0;i<step;i++){
			head=nums[o][0];
			for(int j=0;j<M;j++){
				if (j==M-1){
					nums[o][j]+=head;
					nums[o][j]=nums[o][j]%100;}
				else{
					nums[o][j]+=nums[o][j+1];
					nums[o][j]=nums[o][j]%100;}
			}
		}
	}
	for(int i=0;i<num;i++){
		for(int j=0;j<nums_m[i]-1;j++){
		printf("%d ",nums[i][j]);
		}
		printf("%d",nums[i][nums_m[i]-1]);
       if(i!=num-1){printf("\n");} 
	}
	return 0;
} 
