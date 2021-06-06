#include <iostream>


int main() {
    int n, r;
    std::cin >> n;
    int m = (int) sqrt(n + .0) + 1;

    for (int i = 0; i <= m; i++) {
        for (int j = 0; j <= m; j++) {
            for (int k = 0; k <= m; k++) {
                for (int q = 0; q <= m; q++) {
                    r = i * i + j * j + k * k + q * q;
                    if (r == n) {
                        std::cout << (int)(i != 0) + (int)(j != 0) + (int)(k != 0) + (int)(q != 0);
                        return 0;
                    }
                }
            }
        }
    }
}