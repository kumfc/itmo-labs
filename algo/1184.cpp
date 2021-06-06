#include <iostream>
#include <vector>
#include <iomanip>

int main() {
    int n, k, l = 1, r = 0, cnt, mid, guess = 0;
    double temp;
    std::cin >> n >> k;
    std::vector<int> els(n);

    for (int i = 0; i < n; i++) {
        std::cin >> temp;
        els[i] = (int) (temp * 100 + 0.1);
        if (els[i] > r) {
            r = els[i];
        }
    }

    while (l <= r) {
        cnt = 0;
        mid = (l + r) / 2;
        for (int i = 0; i < n; i++) {
            cnt += (int) els[i] / mid;
        }
        if (cnt >= k){
            guess = mid;
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }

    std::cout << std::setprecision(2) << std::fixed << (double) guess / 100 << std::endl;

    return 0;
}