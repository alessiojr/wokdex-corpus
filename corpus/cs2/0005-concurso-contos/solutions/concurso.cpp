#include <stdio.h>
#include <math.h>
#include <string>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int main(){
    int n,l,c,i,j;
    char atual[1000];
    vector<int> v;
    int somac,somal,cont;
    scanf("%d %d %d",&n,&l,&c);
    for(i=0;i<n;i++){
        scanf("%s",&atual);
        v.push_back(strlen(atual));
        atual[0]='\0';
    }
    somac=0;
    somal=0;
    cont=1;
    for(j = 0;j<n;j++){
        if((v[j]+somac+1)<c){
            somac=somac+v[j]+1;//espaço
        }else{
            if((v[j]+somac)==c || (v[j]+somac+1)==c){
                somal++;
                somac=0;
            }else{
                if((v[j]+somac)>c){
                    somal++;
                    if(v[j]==c || (v[j]+1)==c){
                        somal++;
                        somac=0;
                    }else{
                        somac=v[j]+1;
                    }
                }
            }
        }
        if(somal==l && somac==0 && j==n-1){
            cont--;
        }
        if(somal==l){
            cont++;
            somal=0;
        }else{
            while(somal>l){
                cont++;
                somal=somal-l;
            }
        }

    //printf("vet = %d soma c = %d somal = %d\n",v[j],somac,somal);
    }
//    if(somac==0 && l==somal){
//        printf("aaaa");
//    }
    printf("%d\n",cont);
    v.clear();
    atual[0]='\0';
}
