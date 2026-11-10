import ctypes,subprocess,os,sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
_str_to_c_types={'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
                'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, 
                'int':ctypes.c_int,'long':ctypes.c_long, 
                'long double':ctypes.c_longdouble, 'long long':ctypes.c_longlong, 'short':ctypes.c_short}
def str_to_c_types(str_,all=False):
    if all:
        return _str_to_c_types
    else:
        return _str_to_c_types[str_]
def list_to_c_types(list_,all=False):
    if all:
        return _str_to_c_types
    else:
        res=list_
        for i in range(len(list_)):
            res[i]=str_to_c_types(list_[i])
        return res
def f_type(func):
    for i in func:
        i[0].argtypes = list_to_c_types(i[1])
        i[0].restype = str_to_c_types(i[2])
cpp=ctypes.CDLL('cpp_function.dylib')
def py_type():
    return [[cpp.add,['long long','long long'],'long long']]
if __name__ == '__main__':
    f_type(py_type())
def py_main():
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            cpp.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass         
if __name__ == '__main__':
    py_main()