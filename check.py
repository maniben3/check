import ctypes
clibrary=ctypes.CDLL("home/ubuntu/ff/aws-fpga/test1/test_hello_world.so")
print(clibrary.main)
