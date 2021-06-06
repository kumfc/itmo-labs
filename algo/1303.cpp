#include <iostream>
#include <vector>
#include <tuple>

struct RichardIV {
    RichardIV(int l, int r) {
        this->l = l;
        this->r = r;
    }

    int l, r;
};

int main() {
    int m, l, r;
    const int sizington = 5001;
    std::vector<RichardIV *> els, highest_jump(sizington), solve_chain(sizington);
    std::cin >> m;

    for (int i = 0; i < sizington; i++) {
        highest_jump[i] = new RichardIV(-50001, -50001);
    }

    while (true) {
        std::cin >> l >> r;
        if (l == 0 && r == 0) {
            break;
        }
        if (r < 0 || l > m) {
            continue;
        }
        els.push_back(new RichardIV(l, r));

        if (l >= 0 && r > highest_jump[l]->r) {
            highest_jump[l]->r = r;
            highest_jump[l]->l = l;
        }
    }

    for (auto el: els) {
        if (el->l <= 0 && el->r > 0) {
            if (!solve_chain[0] || el->r > solve_chain[0]->r) {
                solve_chain[0] = el;
            }
        }
    }
    if (solve_chain[0] == nullptr) {
        std::cout << "No solution" << std::endl;
        return 0;
    }
    for (int i = 1; i <= m; i++) {
        if (solve_chain[i - 1]->r >= highest_jump[i]->r) {
            solve_chain[i] = solve_chain[i - 1];
        } else {
            solve_chain[i] = highest_jump[i];
        }
    }

    std::vector<RichardIV *> cool_guys;
    int pos = 0;
    while (pos < m) {
        if(solve_chain[pos]->r == pos){
            std::cout << "No solution" << std::endl;
            return 0;
        }
        cool_guys.push_back(solve_chain[pos]);
        pos = solve_chain[pos]->r;
    }

    std::cout << cool_guys.size() << std::endl;
    for (auto &cool_guy : cool_guys) {
        std::cout << cool_guy->l << " " << cool_guy->r << std::endl;
    }

    return 0;
}