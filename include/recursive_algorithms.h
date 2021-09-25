#include <pybind11/pybind11.h>  // pybind11 — Seamless operability between C++11 and Python.

unsigned long fibonacci(const unsigned int n);
unsigned long factorial(const unsigned int n);

namespace py = pybind11;

PYBIND11_MODULE(pybind_11_example, mod) {
    mod.def("fibonacci_cpp", &fibonacci, "Recursive fibonacci algorithm.");
    mod.def("factorial_cpp", &factorial, "Recursive factorial algorithm.");
}
