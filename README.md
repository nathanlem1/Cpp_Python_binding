### C++ Python bindings
<<<<<<< HEAD
We implement two recursive algorithms, fibonnaci and factorial, in C++ and make Python bindings using 
[pybind11](https://github.com/pybind/pybind11), without even using CMake. We show here how we can use more than 
one C++ functions when we make Python bindings. The C++ functions are much faster than the Python implementations. 
We borrow some ideas from [here](https://www.blopig.com/blog/2021/03/c-python-bindings-in-5-minutes/).

=======
We implement two recursive algorithms, fibonnaci and factorial, in C++ and make Python bindings using [pybind11](https://github.com/pybind/pybind11), without even using CMake. We show here how we can use more than one C++ functions when we make Python bindings. The C++ functions are much faster than the Python implementations. We borrow some ideas from [here](https://www.blopig.com/blog/2021/03/c-python-bindings-in-5-minutes/).

### Dependencies
- C++11
- pybind11

pybind11 can be installed using:
```bash
pip install pybind11
```

### Running Example Code
This module can be compiled and installed using:
```bash
pip install -e . -vvv
```

And you can run this module using:
```bash
python main.py
```



