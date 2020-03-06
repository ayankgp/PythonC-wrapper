#include "struct.h"

void multiply_h(parameters* params)
{
    for(int i=0; i<params->N; i++)
    {
        params->numbers[i] = params->numbers[i] * params->scale;
    }
}
