#include <stdio.h>


int main()
{
	printf("Enter size1 and size2\n");
	int size1,size2;
	scanf("%d %d",&size1,&size2);
	printf("Enter vector 1\n");
	int v1,v2,v3;
	scanf("%d %d %d",&v1,&v2,&v3);
	printf("Enter vector 2\n");
	int vv1,vv2,vv3;
	scanf("%d %d %d",&vv1,&vv2,&vv3);

	printf("1) Add\n2) Sub\n3) Multiply\n4) Max\n5) Min\n6) Change\n7) Print\n8) Exit\n");
		int b;
	scanf("%d",&b);

if(b==1){
	int add[3];
	add[0]=v1+vv1;
	add[1]=v2+vv2;
	add[2]=v3+vv3;
	printf("%d %d %d",add[0],add[1],add[2]);
}
//int main1();
if(b==2){
	int min[3];
	min[0]=v1-vv1;
	min[1]=v2-vv2;
	min[2]=v3-vv3;
	printf("%d %d %d",min[0],min[1],min[2]);
}
//int main2();
if(b==3){
	int zarb;
	zarb=v1*vv1+v2*vv2+v3*vv3;
	printf("%d ",zarb);
}
//int main3();
if((b==4)||(b==5)||(b==6)||(b==7)){

printf("Choose vector\n");
int l;
scanf("%d",&l);
if(b==4){
	if(l==1)
	{
		if(v1>=v2){
			if(v1>=v3)
			printf("%d",v1);
			else
			printf("%d",v3);
		}
		else{
			if(v2>=v3)
			printf("%d",v2);
			else
			printf("%d",v3);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv1>=vv3)
			printf("%d",vv1);
			else
			printf("%d",vv3);
		}
		else{
			if(vv2>=vv3)
			printf("%d",vv2);
			else
			printf("%d",vv3);
		}
	}

}
if(b==5)
{	if(l==1)
	{
		if(v1>=v2){
			if(v2>=v3)
			printf("%d",v3);
			else
			printf("%d",v2);
		}
		else{
			if(v1>=v3)
			printf("%d",v3);
			else
			printf("%d",v1);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv2>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv2);
		}
		else{
			if(vv1>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv1);
		}
	}
}
if(b==7){
	if(l==1){
		printf("%d %d %d",v1,v2,v3);
	}
	else
		printf("%d %d %d",vv1,vv2,vv3);
}
if(b==6){

if(l==1){
	printf("Enter new vector %d\n",l);
	scanf("%d %d %d",&v1,&v2,&v3);
		printf("1) Add\n2) Sub\n3) Multiply\n4) Max\n5) Min\n6) Change\n7) Print\n8) Exit\n");		int b;
	scanf("%d",&b);

if(b==1){
	int add[3];
	add[0]=v1+vv1;
	add[1]=v2+vv2;
	add[2]=v3+vv3;
	printf("%d %d %d",add[0],add[1],add[2]);
}
//int main1();
if(b==2){
	int min[3];
	min[0]=v1-vv1;
	min[1]=v2-vv2;
	min[2]=v3-vv3;
	printf("%d %d %d",min[0],min[1],min[2]);
}
//int main2();
if(b==3){
	int zarb;
	zarb=v1*vv1+v2*vv2+v3*vv3;
	printf("%d ",zarb);
}
//int main3();
if((b==4)||(b==5)||(b==6)||(b==7)){

printf("Choose vector\n");
int l;
scanf("%d",&l);
if(b==4){
	if(l==1)
	{
		if(v1>=v2){
			if(v1>=v3)
			printf("%d",v1);
			else
			printf("%d",v3);
		}
		else{
			if(v2>=v3)
			printf("%d",v2);
			else
			printf("%d",v3);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv1>=vv3)
			printf("%d",vv1);
			else
			printf("%d",vv3);
		}
		else{
			if(vv2>=vv3)
			printf("%d",vv2);
			else
			printf("%d",vv3);
		}
	}

}
if(b==5)
{	if(l==1)
	{
		if(v1>=v2){
			if(v2>=v3)
			printf("%d",v3);
			else
			printf("%d",v2);
		}
		else{
			if(v1>=v3)
			printf("%d",v3);
			else
			printf("%d",v1);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv2>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv2);
		}
		else{
			if(vv1>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv1);
		}
	}
}
if(b==7){
	if(l==1){
		printf("%d %d %d",v1,v2,v3);
	}
	else
		printf("%d %d %d",vv1,vv2,vv3);
}
}
else{
	printf("Enter new vector %d\n",l);
	scanf("%d %d %d",&vv1,&vv2,&vv3);
		printf("1) Add\n2) Sub\n3) Multiply\n4) Max\n5) Min\n6) Change\n7) Print\n8) Exit\n");		int b;
	scanf("%d",&b);

if(b==1){
	int add[3];
	add[0]=v1+vv1;
	add[1]=v2+vv2;
	add[2]=v3+vv3;
	printf("%d %d %d",add[0],add[1],add[2]);
}
//int main1();
if(b==2){
	int min[3];
	min[0]=v1-vv1;
	min[1]=v2-vv2;
	min[2]=v3-vv3;
	printf("%d %d %d",min[0],min[1],min[2]);
}
//int main2();
if(b==3){
	int zarb;
	zarb=v1*vv1+v2*vv2+v3*vv3;
	printf("%d ",zarb);
}
//int main3();
if((b==4)||(b==5)||(b==6)||(b==7)){

printf("Choose vector\n");
int l;
scanf("%d",&l);
if(b==4){
	if(l==1)
	{
		if(v1>=v2){
			if(v1>=v3)
			printf("%d",v1);
			else
			printf("%d",v3);
		}
		else{
			if(v2>=v3)
			printf("%d",v2);
			else
			printf("%d",v3);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv1>=vv3)
			printf("%d",vv1);
			else
			printf("%d",vv3);
		}
		else{
			if(vv2>=vv3)
			printf("%d",vv2);
			else
			printf("%d",vv3);
		}
	}

}
if(b==5)
{	if(l==1)
	{
		if(v1>=v2){
			if(v2>=v3)
			printf("%d",v3);
			else
			printf("%d",v2);
		}
		else{
			if(v1>=v3)
			printf("%d",v3);
			else
			printf("%d",v1);
		}
	}
		if(l==2)
	{
		if(vv1>=vv2){
			if(vv2>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv2);
		}
		else{
			if(vv1>=vv3)
			printf("%d",vv3);
			else
			printf("%d",vv1);
		}
	}
}
if(b==7){
	if(l==1){
		printf("%d %d %d",v1,v2,v3);
	}
	else
		printf("%d %d %d",vv1,vv2,vv3);
}}}
}
}}}
/*
int main1(int v1,int v2,int v3,int vv1,int vv2,int vv3){
	int add[3];
	add[0]=v1+vv1;
	add[1]=v2+vv2;
	add[2]=v3+vv3;
	printf("%d %d %d",add[0],add[1],add[2]);
}
int main2(int v1,int v2,int v3,int vv1,int vv2,int vv3){
	int min[3];
	min[0]=v1-vv1;
	min[1]=v2-vv2;
	min[2]=v3-vv3;
	printf("%d %d %d",min[0],min[1],min[2]);
}
int main3(int v1,int v2,int v3,int vv1,int vv2,int vv3){
	int zarb;
	zarb=v1*vv1+v2*vv2+v3*vv3;
	printf("%d ",zarb);
}
/*int main4(int v1,int v2,int v3,int vv1,int vv2,int vv3){

}
int main5(int v1,int v2,int v3,int vv1,int vv2,int vv3){

}*/
