#include <iostream>

struct LinkedAnton {
    LinkedAnton *prev;
    int value;

    explicit LinkedAnton(int v) : value(v), prev(nullptr) {}
};

class Stack {
private:
    LinkedAnton *last;
public:
    void push_back(int v) {
        auto *ins = new LinkedAnton(v);
        ins->prev = last;
        last = ins;
    }

    void pop() {
        last = last->prev;
    }

    int get() {
        return last->value;
    }
};


int main() {
    int n, t, max = 0;

    std::cin >> n;
    Stack els{};

    for (int i = 0; i < n; i++) {
        std::cin >> t;

        if (t > max) {
            for (int k = max + 1; k < t + 1; k++) {
                els.push_back(k);
            }
            els.pop();
            max = t;
        } else if (t == els.get()) {
            els.pop();
        } else {
            std::cout << "Cheater" << std::endl;
            return 0;
        }
    }

    std::cout << "Not a proof" << std::endl;

    return 0;
}