#include <iostream>
#include <vector>


int main(){
    int m, t, i = 0, idx;
    std::cin >> m;
    std::vector<int> els;

    while (true) {
        std::cin >> t;
        if (t == -1) {
            break;
        }
        els.push_back(t);
    }

    int n = els.size();
    int sq_size = (int) sqrt (n + .0) + 1;
    std::vector<int> sqrt_max(sq_size);

    for(i = 0; i < n; i++) {
        idx = i / sq_size;
        if (els[i] > sqrt_max[idx]) {
            sqrt_max[idx] = els[i];
        }
    }

    int l, r, max;
    for (int q = 0; q < (n - m + 1); q++) {
        l = q, r = q + m - 1;
        max = -1;
        for (i = l; i <= r;) {
            if (i % sq_size == 0 && i + sq_size - 1 <= r) {
                idx = i / sq_size;
                if (sqrt_max[idx] > max) {
                    max = sqrt_max[idx];
                }
                i += sq_size;
            } else {
                if (els[i] > max) {
                    max = els[i];
                }
                ++i;
            }
        }
        std::cout << max << std::endl;
    }

    return 0;
}