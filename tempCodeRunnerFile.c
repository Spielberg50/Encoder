#include <omp.h>
#include<stdio.h>
#include<stdlib.h>

int main()
{
    float moy=0.0; 
    int sum=0;
    int A[1000]; 
    int i;

    for (i=0;i< 1000; i++) 
    {
        A[i] = i;
    }

    #pragma omp parallel for reduction(+:moy)
    {
        for (i=0;i< 1000; i++) 
        {
            #pragma omp critical
            {
                sum += A[i];
            }
        }
    }

    moy= (float)moy/1000;
    printf("moyenne=%d",&sum);
    return 0;
}