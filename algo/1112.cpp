#include <iostream>
#include <vector>
#include <tuple>

struct RichardIII {
    RichardIII(int a, int b) {
        if(a < b) {
            this->a = a;
            this->b = b;
        } else {
            this->a = b;
            this->b = a;
        }
    }

    int a, b;
};

bool operator<(const RichardIII &x, const RichardIII &y) {
    return std::tie(x.a, x.b) < std::tie(y.a, y.b);
}

void swap(std::vector<RichardIII *> &list, int i, int k) {
    RichardIII *temp = list[i];
    list[i] = list[k];
    list[k] = temp;
}

int main() {
    int n, a, b;
    std::vector<RichardIII *> els;

    std::cin >> n;

    for (int i = 0; i < n; i++) {
        std::cin >> a >> b;
        els.push_back(new RichardIII(a, b));
        for (int j = i - 1; j >= 0; j--) {
            if (els[j + 1]->b < els[j]->b) {
                swap(els, j + 1, j);
            } else {
                break;
            }
        }
    }

    std::vector<RichardIII *> cool_guys;
    cool_guys.push_back(els[0]);
    for (int i = 1; i < n; i++) {
        if(els[i]->a >= cool_guys[cool_guys.size() - 1]->b){
            cool_guys.push_back(els[i]);

            for (int j = (int)cool_guys.size() - 2; j >= 0; j--) {
                if (*cool_guys[j + 1] < *cool_guys[j]) {
                    swap(cool_guys, j + 1, j);
                } else {
                    break;
                }
            }
        }
    }

    std::cout << cool_guys.size() << std::endl;
    for (auto & cool_guy : cool_guys) {
        std::cout << cool_guy->a << " " << cool_guy->b << std::endl;
    }

    return 0;
}