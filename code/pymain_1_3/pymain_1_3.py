import sys
import ctypes
import subprocess,os
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
def get_c(pymain_):
    ispy=False
    p_split=pymain_.split('\n')
    cpp=''
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if (i == 'py main(){') or (i == 'py type(){'):
                ispy=True
            if ispy:
                if i == '}':
                    ispy=False
                    continue
                if i == '} ':
                    ispy=False
                    continue
            if not ispy:
                cpp = cpp + i + '\n'
        return cpp
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if (i == 'py main(){') or (i == 'py type(){'):
                ispy=True
            if ispy:
                if i == '}':
                    ispy=False
                    continue
                if i == '} ':
                    ispy=False
                    continue
            if not ispy:
                cpp = cpp + i + '\n'
        return cpp
    else:
        return ''
def get_main(pymain_):
    p_split=pymain_.split('\n')
    py=''
    ispy=False
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if i == 'py main(){':
                ispy=True
            if ispy:
                py = py + i +'\n'
                if i == '}':
                    ispy=False
                if i == '} ':
                    ispy=False
        return 'def py_main():\n'+'\n'.join(py.split('\n')[1:-2])
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if i == 'py main(){':
                ispy=True
            if ispy:
                py = py + i +'\n'
                if i == '}':
                    ispy=False
                if i == '} ':
                    ispy=False
        return 'def py_main():\n'+'\n'.join(py.split('\n')[1:-2])
    else:
        return ''
def get_type(pymain_):
    p_split=pymain_.split('\n')
    py=''
    ispy=False
    if p_split[0] == 'use c;':
        for i in p_split[1:]:
            if i == 'py type(){':
                ispy=True
            if ispy:
                py = py + i +'\n'
                if i == '}':
                    ispy=False
                if i == '} ':
                    ispy=False
        return 'def py_type():\n'+'\n'.join(py.split('\n')[1:-2])
    elif (p_split[0] == 'use c++;') or (p_split[0] == 'use cpp;'):
        for i in p_split[1:]:
            if i == 'py type(){':
                ispy=True
            if ispy:
                py = py + i +'\n'
                if i == '}':
                    ispy=False
                if i == '} ':
                    ispy=False
        return 'def py_type():\n'+'\n'.join(py.split('\n')[1:-2])
    else:
        return ''
def add_dyn_lib(c,name_,dyn_lib_name,cpp_or_c='c',system_='system Mac;'):
    if cpp_or_c == 'c':
        with open(name_,'w') as add_dyn_lib_file:
            add_dyn_lib_file.write(c)
        if system_ == 'system Mac;':
            subprocess.run(['gcc','-fPIC','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Linux;':
            subprocess.run(['gcc','-fPIC','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Win;':
            subprocess.run(['gcc','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Windows;':
            subprocess.run(['gcc','-shared',name_,'-o',dyn_lib_name])
        else:
            sys.stderr.write(f'\033[91merror:{system_} \033[0m')
            sys.exit()
    if cpp_or_c == 'cpp':
        with open(name_,'w') as add_dyn_lib_file:
            add_dyn_lib_file.write(c)
        if system_ == 'system Mac;':
            subprocess.run(['g++','-fPIC','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Linux;':
            subprocess.run(['g++','-fPIC','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Win;':
            subprocess.run(['g++','-shared',name_,'-o',dyn_lib_name])
        elif system_ == 'system Windows;':
            subprocess.run(['g++','-shared',name_,'-o',dyn_lib_name])
        else:
            sys.stderr.write(f'\033[91merror:{system_} \033[0m')
            sys.exit()
def load_dyn_lib(_NT):
    return ctypes.CDLL(_NT)
def comp(name,pymain_n):
    pymain_='\n'.join((pymain_n.split('\n'))[1:])
    system_=(pymain_n.split('\n'))[0]
    os.makedirs(exist_ok=True,name=name)
    if pymain_[:7] == 'use c;\n':
        if get_c(pymain_) != '':
            if system_ == 'system Mac;':
                add_dyn_lib(get_c(pymain_),name+'/c_function.c',name+'/c_function.dylib','c',system_)
            elif system_ == 'system Linux;':
                add_dyn_lib(get_c(pymain_),name+'/c_function.c',name+'/c_function.so','c',system_)
            elif system_ == 'system Win;':
                add_dyn_lib(get_c(pymain_),name+'/c_function.c',name+'/c_function.dll','c',system_)
            elif system_ == 'system Windows;':
                add_dyn_lib(get_c(pymain_),name+'/c_function.c',name+'/c_function.dll','c',system_)
            else:
               sys.stderr.write(f'\033[91merror:{system_} \033[0m')
               sys.exit()
            if get_main(pymain_) != '':
                res_py='''system="'''+system_+'''"
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
'''+get_type(pymain_)+'''
if __name__ == '__main__':
    f_type(py_type())
'''+get_main(pymain_)+'''
if __name__ == '__main__':
    ret=py_main()
    try:
        sys.exit(ret)
    except:
        sys.exit()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\033[0m')
                sys.exit()
        else:
            if get_main(pymain_) != '':
                res_py='''
version="1.2"
'''+get_main(pymain_)+'''
py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\033[0m')
                sys.exit()
    elif (pymain_[:9] == 'use cpp;\n') or (pymain_[:9] == 'use c++;\n'):
        if get_c(pymain_) != '':
            if system_ == 'system Mac;':
                add_dyn_lib(get_c(pymain_),name+'/cpp_function.cpp',name+'/cpp_function.dylib','cpp',system_)
            elif system_ == 'system Linux;':
                add_dyn_lib(get_c(pymain_),name+'/cpp_function.cpp',name+'/cpp_function.so','cpp',system_)
            elif system_ == 'system Win;':
                add_dyn_lib(get_c(pymain_),name+'/cpp_function.cpp',name+'/cpp_function.dll','cpp',system_)
            elif system_ == 'system Windows;':
                add_dyn_lib(get_c(pymain_),name+'/cpp_function.cpp',name+'/cpp_function.dll','cpp',system_)
            else:
               sys.stderr.write(f'\033[91merror:{system_} \033[0m')
               sys.exit()
            if get_main(pymain_) != '':
                res_py='''system="'''+system_+'''"
import ctypes,os,sys
os.chdir(os.path.dirname(os.path.abspath(sys.argv[0])))
_str_to_c_types={'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
                'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, 
                'int':ctypes.c_int,'long':ctypes.c_long, 
                'long double':ctypes.c_longdouble, 'long long':ctypes.c_longlong, 'short':ctypes.c_short,
                'null':None,'Null':None,'None':None,'none':None}
version="1.3"
def load():
    if system == "system Mac;":
        return ctypes.CDLL('cpp_function.dylib')
    elif system == "system Linux;":
        return ctypes.CDLL('cpp_function.so')
    elif system == "system Win;":
        return ctypes.CDLL('cpp_function.dll')
    elif system == "system Windows;":
        return ctypes.CDLL('cpp_function.dll')
def str_to_c_types(str_,all=False):
    if all:
        return _str_to_c_types
    else:
        try:
            return _str_to_c_types[str_]
        except:
            return str_
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
cpp=load()
'''+get_type(pymain_)+'''
if __name__ == '__main__':
    f_type(py_type())
'''+get_main(pymain_)+'''
if __name__ == '__main__':
    ret=py_main()
    try:
        sys.exit(ret)
    except:
        sys.exit()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\n\033[0m')
                sys.exit()
        else:
            if get_main(pymain_) != '':
                res_py='''
version="1.3"
'''+get_main(pymain_)+'''
py_main()'''
                with open(name+'/main.py','w') as py_py:
                    py_py.write(res_py)
            else:
                sys.stderr.write('\033[91merror: your code have not main\n\033[0m')
                sys.exit()
    elif pymain_[:8] == 'use py;\n':
        os.makedirs(exist_ok=True,name=name)
        with open(name+'/main.py','w') as py_py_6666:
            py_py_6666.write('version="1.3"\n'+pymain_[8:])
    else:
        print(f'\033[91merror: {pymain_[:8]}\033[0m')
#====================#
if __name__ == '__main__':
    try:
        if len(sys.argv) == 3:
            try:
                with open(sys.argv[1],'r') as q:
                    pm=q.read()
                comp(sys.argv[2],pm)
            except:
                print('\033[91merror\033[0m',file=sys.stderr)
        elif (sys.argv[1] == '-v') or (sys.argv[1] == '-version'):
            print('version="1.3"')
        else:
            pass
    except:
        print(f'\033[91merror\033[0m')
