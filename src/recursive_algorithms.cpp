#include "recursive_algorithms.h"

unsigned long fibonacci(const unsigned int n){

    if (n < 2){
        return n;
    }
    else{
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}


unsigned long factorial(const unsigned int n){

    if (n == 0 || n == 1){
        return 1;
    }
    else{
        return n * factorial (n - 1);
    }
}
