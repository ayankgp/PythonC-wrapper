#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "header.h"

void add(parameters* params)
{
    multiply_h(params);
    for(int i=0; i<params->N; i++)
    {
        params->result[i] = params->numbers[i] * params->scale;
    }
    printf("%ld %ld \n", params->numbers_int[0], params->numbers_int[1]);
}
