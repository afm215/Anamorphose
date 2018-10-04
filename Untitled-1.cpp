#include <malloc.h>

#include <iostream>
using namespace std;

int main()
{
	int *ptr;
    ptr = (int*)malloc(sizeof(int) * 5);
    free(ptr);
    ptr =NULL;
	return 0;
}
