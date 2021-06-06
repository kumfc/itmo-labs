#include "iostream"
#include <iomanip>

int main() {
    double n, s, e, temp, sum = 0;
    std::cin >> n >> s >> e;

    for (int i = 0; i < n; i++){
        std::cin >> temp;
        sum += 2 * (n - i) * temp;
    }

    double res = (s * n + e - sum) / (n + 1);

    std::cout << std::setprecision(2) << std::fixed << res;

    return 0;
}