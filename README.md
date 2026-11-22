<details>
<summary>pymain_1_1说明书</summary>

---
1.下载和测试：  
下载： 
```bash
git clone https://github.com/huangziling0511/pymain.git
```
测试：直接运行pymain_1_1.py（不加命令行参数）就会输出版本号。
```bash
python3 pymain_1_1.py
```
---
2.编译
```bash
python3 pymain_1_1.py code.pymain code #把code.pymain编译成文件夹code
```
---
3.介绍： 这个语言(1.0)是2026年7月27日(星期一)21:04被发明的，它可以让python调用其他语言的函数更简单。

---
4.模式： 你可以创建一个.pymain文件，然后你要在文件第一行写use py;/use c++;/use cpp;/use c;来选择模式：  

use py; --------- 纯python模式  
use c; ---------- python加c语言模式  
use c++; -------- python加c++模式  
use cpp; -------- python加c++模式,和上一行一样

---
5.use py; ： 纯python模式，除了use py;这条声明都是纯python  

use py;声明不可以和后面的代码挤在一起  
use py;声明后面必须是换行符  
use py;声明后面不可以有空格

---
6.use c;/use cpp;/use c++; ： python加c/c++模式  
use c;/use cpp;/use c++;声明不可以和后面的代码挤在一起  
use c;/use cpp;/use c++;声明后面必须是换行符  
use c;/use cpp;/use c++;声明后面不可以有空格  
代码里要有  
```pymain
py main(){line n;  
     #^^^^^^^这几个地方不可以有空格  
}
```
n指的是整个py main()函数占用的行数（包括 **py main(){line n;** 这一行和最后的 **}**）  
py main()里边就写python了<br><br> 
代码里要有
```pymain
py type(){line n;  
     #^^^^^^^这几个地方不可以有空格  
}  
```
n指的是整个py type()函数占用的行数（包括 **py type(){line n;** 这一行和最后的 **}**）  
py type()里边就写c/c++函数的类型了  
格式： 
```python
return [[第一个函数的类型],[第二个函数的类型],[第三个函数的类型]……]
```
一个函数的类型格式： 
```python
[c/cpp.函数名字,[第一个参数的类型，第二个参数的类型……],结果的类型]或  
[c/cpp.函数名字,None,结果的类型] 
``` 
类型支持：
```python
{'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,  
'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float,   
'int':ctypes.c_int,'long':ctypes.c_long, 'long double':ctypes.c_longdouble,   
'long long':ctypes.c_longlong, 'short':ctypes.c_short} #char*对应python的byte类型
```
---
7.示范： 

1_1_c_add.pymain:
```pymain
use c;
#include <stdio.h>
long long add(long long a,long long b){
    printf("%s","c: ");
    printf("%lld",a+b);
    printf("%s","\n");
    return a+b;
}
py type(){line 3;
    return [[c.add,['long long','long long'],'long long']]
}
py main(){line 11;
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            c.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass       
}
```
编译：
```bash
python3 pymain_1_1.py 1_1_c_add.pymain 1_1_c_add
```
运行：
```bash
python3 1_1_c_add/main.py
```

1_1_cpp_add.pymain:
```pymain
use cpp;
#include <iostream>
extern "C"{
long long add(long long a,long long b){
    std::cout << "cpp: " << a+b << std::endl;
    return a+b;
}
}
py type(){line 3;
    return [[cpp.add,['long long','long long'],'long long']]
}
py main(){line 11;
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            cpp.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass         
}
```
编译：
```bash
python3 pymain_1_1.py 1_1_cpp_add.pymain 1_1_cpp_add
```
运行：
```bash
python3 1_1_cpp_add/main.py
```

1_1_py.pymain:
```pymain
use py;
print('hello')
```
编译：
```bash
python3 pymain_1_1.py 1_1_cpp_add.pymain 1_1_cpp_add
```
运行：
```bash
python3 1_1_cpp_add/main.py
```
</details>
<details>
<summary>pymain_1_2说明书</summary>

1.下载和测试：  
下载： 
```bash
git clone https://github.com/huangziling0511/pymain.git
```
测试：运行pymain_1_2.py,命令行参数:-v或-version就会输出版本号。
```bash
python3 pymain_1_2.py -v
python3 pymain_1_2.py -version
```
---
2.编译
```bash
python3 pymain_1_2.py code.pymain code #把code.pymain编译成文件夹code
```
---
3.介绍： 这个语言(1.0)是2026年7月27日(星期一)21:04被发明的，它可以让python调用其他语言的函数更简单。

---
4.模式： 你可以创建一个.pymain文件，然后你要在文件第一行写use py;/use c++;/use cpp;/use c;来选择模式：  

use py; --------- 纯python模式  
use c; ---------- python加c语言模式  
use c++; -------- python加c++模式  
use cpp; -------- python加c++模式,和上一行一样

---
5.use py; ： 纯python模式，除了use py;这条声明都是纯python,但又自带的变量version = "1.2" 

use py;声明不可以和后面的代码挤在一起  
use py;声明后面必须是换行符  
use py;声明后面不可以有空格

---
6.use c;/use cpp;/use c++; ： python加c/c++模式  
use c;/use cpp;/use c++;声明不可以和后面的代码挤在一起  
use c;/use cpp;/use c++;声明后面必须是换行符  
use c;/use cpp;/use c++;声明后面不可以有空格  
代码里要有  
```pymain
py main(){line n;  
     #^^^^^^^这几个地方不可以有空格  
}
```
n指的是整个py main()函数占用的行数（包括 **py main(){line n;** 这一行和最后的 **}**）  
py main()里边就写python了<br><br> 
代码里要有
```pymain
py type(){line n;  
     #^^^^^^^这几个地方不可以有空格  
}  
```
n指的是整个py type()函数占用的行数（包括 **py type(){line n;** 这一行和最后的 **}**）  
py type()里边就写c/c++函数的类型了  
格式： 
```python
return [[第一个函数的类型],[第二个函数的类型],[第三个函数的类型]……]
```
一个函数的类型格式： 
```python
[c/cpp.函数名字,[第一个参数的类型，第二个参数的类型……],结果的类型]或  
[c/cpp.函数名字,None,结果的类型] 
``` 
类型支持：
```python
{'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
 'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, #char*对应python的byte类型
 'int':ctypes.c_int,'long':ctypes.c_long, 
 'long double':ctypes.c_longdouble, 'long long':ctypes.c_longlong, 'short':ctypes.c_short,
 'null':None,'Null':None,'None':None,'none':None}
```
---
7.示范： 

<details>
<summary>1_2_c_add.pymain</summary>

```pymain
use c;
#include <stdio.h>
long long add(long long a,long long b){
    printf("%s","c: ");
    printf("%lld",a+b);
    printf("%s","\n");
    return a+b;
}
py type(){line 3;
    return [[c.add,['long long','long long'],'long long']]
}
py main(){line 11;
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            c.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass       
}
```
编译：
```bash
python3 pymain_1_2.py 1_2_c_add.pymain 1_2_c_add
```
运行：
```bash
python3 1_2_c_add/main.py
```
</details>
<details>
<summary>1_2_cpp_add.pymain</summary>

```pymain
use cpp;
#include <iostream>
extern "C"{
long long add(long long a,long long b){
    std::cout << "cpp: " << a+b << std::endl;
    return a+b;
}
}
py type(){line 3;
    return [[cpp.add,['long long','long long'],'long long']]
}
py main(){line 11;
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            cpp.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass         
}
```
编译：
```bash
python3 pymain_1_2.py 1_2_cpp_add.pymain 1_2_cpp_add
```
运行：
```bash
python3 1_2_cpp_add/main.py
```
</details>
<details>
<summary>1_2_py.pymain</summary>

```pymain
use py;
print('hello')
```
编译：
```bash
python3 pymain_1_2.py 1_2_cpp_add.pymain 1_2_cpp_add
```
运行：
```bash
python3 1_2_cpp_add/main.py
```
</details>
<details>
<summary>1_2_c.pymain</summary>

```pymain
use c;
#include <stdio.h>
void out1(){
    printf("Hello world!");
}
py type(){line 3;
    return [[c.out1,"null","null"]]
}
py main(){line 5;
    c.out1()
    print(version)
    return 0
}
```
编译：
```bash
python3 pymain_1_2.py 1_2_c.pymain 1_2_c
```
运行：
```bash
python3 1_2_c/main.py
```
</details>
</details>
<details>
<summary>pymain_1_3说明书</summary>

1.下载和测试：  
下载： 
```bash
git clone https://github.com/huangziling0511/pymain.git
```
测试：运行pymain_1_3.py,命令行参数:-v或-version就会输出版本号。
```bash
python3 pymain_1_3.py -v
python3 pymain_1_3.py -version
```
---
2.编译
```bash
python3 pymain_1_3.py code.pymain code #把code.pymain编译成文件夹code
```
---
3.介绍： 这个语言(1.0)是2026年7月27日(星期一)21:04被发明的，它可以让python调用其他语言的函数更简单。

---
4.系统：你可以创建一个.pymain文件，然后你要在文件第一行写system Mac;/system Linux;/system Win;/system Windows; 

system Mac; ------------ Mac模式  
system Linux; ---------- Linux模式  
system Win; ------------ Windows模式  
system Windows; -------- Windows模式,和上一行一样

---
5.模式： 你在第二行可以写use py;/use c++;/use cpp;/use c;来选择模式：  

use py; --------- 纯python模式  
use c; ---------- python加c语言模式  
use c++; -------- python加c++模式  
use cpp; -------- python加c++模式,和上一行一样

---
6.use py; ： 纯python模式，除了use py;这条声明都是纯python,但又有自带的变量version = "1.3" 

use py;声明不可以和后面的代码挤在一起  
use py;声明后面必须是换行符  
use py;声明后面不可以有空格

---
7.use c;/use cpp;/use c++; ： python加c/c++模式  
use c;/use cpp;/use c++;声明不可以和后面的代码挤在一起  
use c;/use cpp;/use c++;声明后面必须是换行符  
use c;/use cpp;/use c++;声明后面不可以有空格  
代码里要有  
```pymain
py main(){
     #^^^^^这几个地方不可以有空格  
}
``` 
py main()里边就写python了<br><br> 
代码里要有
```pymain
py type(){
     #^^^^^这几个地方不可以有空格  
}  
```
py type()里边就写c/c++函数的类型了  
格式： 
```python
return [[第一个函数的类型],[第二个函数的类型],[第三个函数的类型]……]
```
一个函数的类型格式： 
```python
[c/cpp.函数名字,[第一个参数的类型，第二个参数的类型……],结果的类型]或  
[c/cpp.函数名字,None,结果的类型] 
``` 
类型支持：
```python
{'bool':ctypes.c_bool, 'byte':ctypes.c_byte, 'char':ctypes.c_char,
 'char*':ctypes.c_char_p, 'double':ctypes.c_double, 'float':ctypes.c_float, #char*对应python的byte类型
 'int':ctypes.c_int,'long':ctypes.c_long, 
 'long double':ctypes.c_longdouble, 'long long':ctypes.c_longlong, 'short':ctypes.c_short,
 'null':None,'Null':None,'None':None,'none':None}
```
---
8.Bug：
python部分写多行字符串或多行注释时请不要有一行以}开头，你可以写成'''+'''}（use c/use cpp/use c++）  
比如：
```pymain
system Mac;
use c;
#include <stdio.h>
void out1(){
    printf("Hello world!\n");
}
py type(){
    return [[c.out1,[],"null"]]
}
py main(){
    c.out1()
    print('''1
}
1''')
    return 0
}
```
因该写成：
```pymain
system Mac;
use c;
#include <stdio.h>
void out1(){
    printf("Hello world!\n");
}
py type(){
    return [[c.out1,[],"null"]]
}
py main(){
    c.out1()
    print('''1
'''+'''}
1''')
    return 0
}
```
---
9.示范： 

<details>
<summary>1_3_c_add.pymain</summary>

```pymain
system Mac;
use c;
#include <stdio.h>
long long add(long long a,long long b){
    printf("%s","c: ");
    printf("%lld",a+b);
    printf("%s","\n");
    return a+b;
}
py type(){
    return [[c.add,['long long','long long'],'long long']]
}
py main(){
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            c.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass
    return 0
}
```
编译：
```bash
python3 pymain_1_3.py 1_3_c_add.pymain 1_3_c_add
```
运行：
```bash
python3 1_3_c_add/main.py
```
</details>
<details>
<summary>1_3_cpp_add.pymain</summary>

```pymain
system Mac;
use cpp;
#include <iostream>
extern "C"{
long long add(long long a,long long b){
    std::cout << "cpp: " << a+b << std::endl;
    return a+b;
}
}
py type(){
    return [[cpp.add,['long long','long long'],'long long']]
}
py main(){
    import os
    while True:
        try:
            input1=int(input())
            input2=int(input())
            cpp.add(input1,input2)
            print("py:",input1+input2)
        except:
            pass
    return 0    
}
```
编译：
```bash
python3 pymain_1_3.py 1_3_cpp_add.pymain 1_3_cpp_add
```
运行：
```bash
python3 1_3_cpp_add/main.py
```
</details>
<details>
<summary>1_3_py.pymain</summary>

```pymain
system Mac;
use py;
print('hello')
```
编译：
```bash
python3 pymain_1_3.py 1_3_cpp_add.pymain 1_3_cpp_add
```
运行：
```bash
python3 1_3_cpp_add/main.py
```
</details>
<details>
<summary>1_3_c.pymain</summary>

```pymain
system Mac;
use c;
#include <stdio.h>
void out1(){
    printf("Hello world!\n");
}
py type(){
    return [[c.out1,[],"null"]]
}
py main(){
    c.out1()
    print('version:',version)
    print('system:',system)
    return 0
}
```
编译：
```bash
python3 pymain_1_3.py 1_3_c.pymain 1_3_c
```
运行：
```bash
python3 1_3_c/main.py
```
</details>
</details>