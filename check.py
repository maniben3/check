import ctypes
clibrary=ctypes.CDLL("aws-fpga/test1/test_hello_world.so")
print(clibrary.main)
