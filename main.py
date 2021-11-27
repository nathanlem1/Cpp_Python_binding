import time
import pybind_11_recursion as pybr


def fibonacci_py(x):
    if x < 0:
        print('Error!, fibonacci does not exist for negative numbers.')
        raise ValueError
    elif x < 2:
        return x
    else:
        return fibonacci_py(x - 1) + fibonacci_py(x - 2)


def factorial_py(x):
    if x < 0:
        print('Error!, factorial does not exist for negative numbers.')
        raise ValueError
    elif x == 0 or x == 1:
        return 1
    else:
        return x * factorial_py(x - 1)


n = 20

print('----Fibonnaci----: ')
print('Python:')
start_time_py = time.perf_counter_ns()
print('Answer:', fibonacci_py(n))   # Python function is called here
last_time_py = time.perf_counter_ns()
diff_time_py = last_time_py - start_time_py
print('Time:', diff_time_py / 1e9, 's')

print('C++:')
start_time_cpp = time.perf_counter_ns()
print('Answer:', pybr.fibonacci_cpp(n))  # C++ Python bound function is called here.
last_time_cpp = time.perf_counter_ns()
diff_time_cpp = last_time_cpp - start_time_cpp
print('Time:', diff_time_cpp / 1e9, 's')

print('C++ code runs %0.3f faster than Python code for fibonacci recursion.' % (diff_time_py / diff_time_cpp))
print()


print('----Factorial----: ')
print('Python:')
start_time_py = time.perf_counter_ns()
print('Answer:', factorial_py(n))   # Python function is called here
last_time_py = time.perf_counter_ns()
diff_time_py = last_time_py - start_time_py
print('Time:', diff_time_py / 1e9, 's')

print('C++:')
start_time_cpp = time.perf_counter_ns()
print('Answer:', pybr.factorial_cpp(n))  # C++ Python bound function is called here.
last_time_cpp = time.perf_counter_ns()
diff_time_cpp = last_time_cpp - start_time_cpp
print('Time:', diff_time_cpp / 1e9, 's')

print('C++ code runs %0.3f faster than Python code for factorial recursion.' % (diff_time_py / diff_time_cpp))

