#include <iostream>

int divide(int dividend, int divisor) {
    if (!divisor) return ((int)(~0U>>1));
    while ((divisor = divisor>>1) && divisor >= 1){
        dividend = dividend>>1;
    }
    return dividend;
}

int main(){
    std::cout<< divide(10, 3) << std::endl;
    return 0;
}