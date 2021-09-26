#include <pybind11/pybind11.h>  // pybind11 — Seamless operability between C++11 and Python.

unsigned long int fibonacci(const unsigned int n);
unsigned long long int factorial(const unsigned int n);

PYBIND11_MODULE(pybind_11_recursion, mod) {
    mod.def("fibonacci_cpp", &fibonacci, "Recursive fibonacci algorithm.");
    mod.def("factorial_cpp", &factorial, "Recursive factorial algorithm.");
}

