import ctypes,subprocess,os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
_str_to_c_types={'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
                'char_p':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, 
                'int':ctypes.c_int, 'int16':ctypes.c_int16, 'int32':ctypes.c_int32, 
                'int64':ctypes.c_int64, 'int8':ctypes.c_int8, 'long':ctypes.c_long, 
                'longdouble':ctypes.c_longdouble, 'longlong':ctypes.c_longlong, 'short':ctypes.c_short,
                'size_t':ctypes.c_size_t, 'ssize_t':ctypes.c_ssize_t, 'ubyte':ctypes.c_ubyte, 
                'uint':ctypes.c_uint, 'uint16':ctypes.c_uint16,'uint32':ctypes.c_uint32, 
                'uint64':ctypes.c_uint64, 'uint8':ctypes.c_uint8, 'ulong':ctypes.c_ulong,
                'ulonglong':ctypes.c_ulonglong,'ushort':ctypes.c_ushort, 'void_p':ctypes.c_void_p,
                'voidp':ctypes.c_voidp,'wchar':ctypes.c_wchar, 'wchar_p':ctypes.c_wchar_p}
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
    return [[cpp.add,['longlong','longlong'],'longlong']]
f_type(py_type())
def py_main():
    import os
    while True:
        try:
            a=int(input())
            b=int(input())
            cpp.add(a,b)
            print("py:",a+b)
        except:
            os.sys.exit()           
py_main()