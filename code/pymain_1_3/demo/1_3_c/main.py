system="system Mac;"
import ctypes,os,sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
_str_to_c_types={'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
                'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, 
                'int':ctypes.c_int,'long':ctypes.c_long, 
                'long double':ctypes.c_longdouble, 'long long':ctypes.c_longlong, 'short':ctypes.c_short,
                'null':None,'Null':None,'None':None,'none':None}
version="1.3"
def str_to_c_types(str_,all=False):
    if all:
        return _str_to_c_types
    else:
        try:
            return _str_to_c_types[str_]
        except:
            return str_
def load():
    if system == "system Mac;":
        return ctypes.CDLL('c_function.dylib')
    elif system == "system Linux;":
        return ctypes.CDLL('c_function.so')
    elif system == "system Win;":
        return ctypes.CDLL('c_function.dll')
    elif system == "system Windows;":
        return ctypes.CDLL('c_function.dll')
def list_to_c_types(list_):
    try:
        res=list_.copy()
        for i in range(len(list_)):
            res[i]=str_to_c_types(list_[i])
        return res
    except:
        return str_to_c_types(list_)
def f_type(func):
    for i in func:
        i[0].argtypes = list_to_c_types(i[1])
        i[0].restype = str_to_c_types(i[2])
c=load()
def py_type():
    return [[c.out1,[],"null"]]
if __name__ == '__main__':
    f_type(py_type())
def py_main():
    c.out1()
    print('version:',version)
    print('system:',system)
    return 0
if __name__ == '__main__':
    ret=py_main()
    try:
        sys.exit(ret)
    except:
        sys.exit()