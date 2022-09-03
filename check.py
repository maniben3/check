import ctypes
clibrary=ctypes.CDLL("home/ubuntu/aws-fpga/test1/test_hello_world.so")
print(clibrary.main)
