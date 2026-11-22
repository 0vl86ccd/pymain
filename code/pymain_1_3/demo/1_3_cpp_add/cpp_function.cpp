#include <iostream>
extern "C"{
long long add(long long a,long long b){
    std::cout << "cpp: " << a+b << std::endl;
    return a+b;
}
}
