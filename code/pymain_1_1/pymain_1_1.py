import sys
import ctypes
import subprocess,os
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
def get_c(pymain_):
    p_split=pymain_.split('\n')
    cpp=''
    i2=0
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if (i[:9] == 'py main()') or (i[:9] == 'py type()'):
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                cpp = cpp + i + '\n'
            else:
                i2 = i2-1
        return cpp
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if (i[:9] == 'py main()') or (i[:9] == 'py type()'):
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                cpp = cpp + i + '\n'
            else:
                i2 = i2-1
        return cpp
    else:
        return ''
def get_main(pymain_):
    p_split=pymain_.split('\n')
    py=''
    i2=0
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if i[:15] == 'py main(){line ':
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                pass
            else:
                py = py + i + '\n'
                i2 = i2-1
        return 'def py_main():\n'+'\n'.join(py.split('\n')[1:-2])
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if i[:15] == 'py main(){line ':
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                pass
            else:
                py = py + i + '\n'
                i2 = i2-1
        return 'def py_main():\n'+'\n'.join(py.split('\n')[1:-2])
    else:
        return ''
def get_type(pymain_):
    p_split=pymain_.split('\n')
    py=''
    i2=0
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if i[:15] == 'py type(){line ':
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                pass
            else:
                py = py + i + '\n'
                i2 = i2-1
        return 'def py_type():\n'+'\n'.join(py.split('\n')[1:-2])
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if i[:15] == 'py type(){line ':
                if i[-1] != ';':
                    sys.stderr.write(f'\033[91merror: {i}\n\033[0m')
                    sys.exit()
                i2=int(i[15:-1])
            if i2 == 0:
                pass
            else:
                py = py + i + '\n'
                i2 = i2-1
        return 'def py_type():\n'+'\n'.join(py.split('\n')[1:-2])
    else:
        return ''
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
    try:
        if all:
            return _str_to_c_types
        else:
            res=list_
            for i in range(len(list_)):
                res[i]=str_to_c_types(list_[i])
            return res
    except:
        if all:
            return _str_to_c_types
        else:
            return list_
def add_dyn_lib(c,name_,dyn_lib_name,cpp_or_c='c'):
    if cpp_or_c == 'c':
        with open(name_,'w') as add_dyn_lib_file:
            add_dyn_lib_file.write(c)
        subprocess.run(['gcc','-fPIC','-shared',name_,'-o',dyn_lib_name])
    else:
        with open(name_,'w') as add_dyn_lib_file:
            add_dyn_lib_file.write(c)
        subprocess.run(['g++','-fPIC','-shared',name_,'-o',dyn_lib_name])
def f_type(func):
    for i in func:
        i[0].argtypes = list_to_c_types(i[1])
        i[0].restype = str_to_c_types(i[2])
def load_dyn_lib(_NT):
    return ctypes.CDLL(_NT)
def comp(name,pymain_):
    os.makedirs(exist_ok=True,name=name)
    if pymain_[:7] == 'use c;\n':
        if get_c(pymain_) != '':
            add_dyn_lib(get_c(pymain_),name+'/c_function.c',name+'/c_function.dylib','c')
            if get_main(pymain_) != '':
                res_py='''import ctypes,subprocess,os,sys
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
c=ctypes.CDLL('c_function.dylib')
'''+get_type(pymain_)+'''
if __name__ == '__main__':
    f_type(py_type())
'''+get_main(pymain_)+'''
if __name__ == '__main__':
    py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\033[0m')
                sys.exit()
        else:
            if get_main(pymain_) != '':
                res_py=get_main(pymain_)+'''
py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\033[0m')
                sys.exit()
    elif (pymain_[:9] == 'use cpp;\n') or (pymain_[:9] == 'use c++;\n'):
        if get_c(pymain_) != '':
            add_dyn_lib(get_c(pymain_),name+'/cpp_function.cpp',name+'/cpp_function.dylib','cpp')
            if get_main(pymain_) != '':
                res_py='''import ctypes,subprocess,os,sys
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
'''+get_type(pymain_)+'''
if __name__ == '__main__':
    f_type(py_type())
'''+get_main(pymain_)+'''
if __name__ == '__main__':
    py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\n\033[0m')
                sys.exit()
        else:
            if get_main(pymain_) != '':
                res_py=get_main(pymain_)+'''
py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\n\033[0m')
                sys.exit()
    elif pymain_[:8] == 'use py;\n':
        os.makedirs(exist_ok=True,name=name)
        with open(name+'/main.py','w') as py_py_6666:
            py_py_6666.write(pymain_[8:])
    else:
        print(f'\033[91merror: {pymain_[:8]}\033[0m')
if len(sys.argv) == 3:
    try:
        with open(sys.argv[1],'r') as q:
            pm=q.read()
        comp(sys.argv[2],pm)
    except:
        print('\033[91merror\033[0m',file=sys.stderr)
else:
    print('version 1.1')
