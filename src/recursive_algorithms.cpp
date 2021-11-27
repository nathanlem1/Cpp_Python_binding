#include <iostream>
#include "recursive_algorithms.h"

unsigned long int fibonacci(const unsigned int n){

    if (n < 0){
        std::cout << "Error!, fibonacci does not exist for negative numbers." << std::endl;
    }
    else if (n < 2){
        return n;
    }
    else{
        return fibonacci(n - 1) + fibonacci(n - 2);
    }
}

unsigned long long int factorial(const unsigned int n){

    if (n < 0){
        std::cout << "Error!, factorial does not exist for negative numbers." << std::endl;
    }
    else if (n == 0 || n == 1){
        return 1;
    }
    else{
        return n * factorial (n - 1);
    }
}

