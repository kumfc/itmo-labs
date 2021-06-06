#include <iostream>
#include <queue>
#include <vector>
#include <stack>
#include <string>


struct Solution {
    int step;
    int length;

    explicit Solution(int s, int l) : step(s), length(l) {}
};


int main() {
    int t;
    std::cin >> t;

    std::vector<std::vector<Solution *>> els = {};
    for (int i = 0; i < 901; i++) {
        els.emplace_back(8101);
    }

    els[0][0] = new Solution(0, 0);

    std::queue<std::pair<int, int>> q;
    q.push(std::make_pair(0, 0));

    while (!q.empty()) {
        std::pair<int, int> idx = q.front();
        q.pop();

        Solution *current_s = els[idx.first][idx.second];
        for (int i = 1; i < 10; i++) {
            if (idx.first + i > 900 || idx.second + i * i > 8100) {
                break;
            }

            Solution *next_s = els[idx.first + i][idx.second + i * i];
            if (next_s == nullptr) {
                q.push(std::make_pair(idx.first + i, idx.second + i * i));
            }
            if (next_s == nullptr || (current_s->length + 1) < next_s->length) {
                els[idx.first + i][idx.second + i * i] = new Solution(i, current_s->length + 1);
            }
        }
    }

    int s, ss, b;
    for (int i = 0; i < t; i++) {
        std::cin >> s >> ss;
        if (s > 900 || ss > 8100 || els[s][ss] == nullptr) {
            std::cout << "No solution\n";
            continue;
        }
        //std::stack<int> answer = {};
        std::string answer = "";
        int k = 0;
        while (s > 0) {
            if(k > 100){
                break;
            }
            b = s;
            answer = std::to_string(els[s][ss]->step) + answer;
            s -= els[b][ss]->step;
            ss -= els[b][ss]->step * els[b][ss]->step;
            k++;
        }
        if(k > 100){
            std::cout << "No solution\n";
            continue;
        }
        std::cout << answer.c_str() << "\n";
    }
}