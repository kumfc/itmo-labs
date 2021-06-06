#include <iostream>
#include <string>

int main() {
    int a;
    std::cin >> a;

    if (!a) {
        std::cout << 10;
        return 0;
    }
    if(a == 1){
        std::cout << 1;
        return 0;
    }

    std::string str;
    for (int i = 9; i > 1; i--) {
        if (a % i == 0) {
            str += std::to_string(i);
            a /= i;
            i++;
        }
    }

    if (a > 1) {
        std::cout << -1;
    } else {
        std::reverse(str.begin(), str.end());
        std::cout << str.c_str();
    }

    return 0;
}