### C++ Python bindings
We implement two recursive algorithms, fibonnaci and factorial, in C++ and make Python binding using [pybind11](https://github.com/pybind/pybind11). 
This is adapted from [here](https://www.blopig.com/blog/2021/03/c-python-bindings-in-5-minutes/), and we showed here how we can use more than one .cpp 
files when we make Python binding. The C++ functions are much faster when compared to the Python implementations.

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



