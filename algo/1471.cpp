#include <iostream>
#include <vector>

#pragma comment(linker, "/STACK:16777216")

struct Node {
    explicit Node(int to, int weight) : to(to), weight(weight) {}

    int to, weight;
};

typedef std::vector<std::vector<Node>> Graph;

int sq_size;
std::vector<int> lca_height, lca_list, lca_first, sqrt_min;
std::vector<bool> lca_used;

void lca_dfs(Graph &g, int u, int h) {
    lca_used[u] = true;
    lca_height[u] = h;
    lca_list.push_back(u);
    for (auto i: g[u]) {
        if (!lca_used[i.to]) {
            lca_dfs(g, i.to, h + i.weight);
            lca_list.push_back(u);
        }
    }
}

void lca_build(int size){
    lca_first.assign (size, -1);
    for (int i = 0; i < lca_list.size(); ++i)
    {
        int v = lca_list[i];
        if (lca_first[v] == -1)
            lca_first[v] = i;
    }
}

void sqrt_build(){
    sq_size = (int) sqrt (lca_list.size() + .0) + 1;
    sqrt_min.assign (sq_size, 1e8);;
    int idx;
    for(int i = 0; i < lca_list.size(); i++) {
        idx = i / sq_size;
        if (lca_height[lca_list[i]] < sqrt_min[idx]) {
            sqrt_min[idx] = lca_height[lca_list[i]];
        }
    }
}

int sqrt_solve(int left, int right){
    if(left > right){
        int t = left;
        left = right;
        right = t;
    }

    int r = lca_first[right], l = lca_first[left];
    if(l > r){
        int t = l;
        l = r;
        r = t;
    }

    int min = 1e8, idx;
    for (int i = l; i <= r;) {
        if (i % sq_size == 0 && i + sq_size - 1 <= r) {
            idx = i / sq_size;
            if (sqrt_min[idx] < min) {
                min = sqrt_min[idx];
            }
            i += sq_size;
        } else {
            if (lca_height[lca_list[i]] < min) {
                min = lca_height[lca_list[i]];
            }
            ++i;
        }
    }

    return (lca_height[right] - min) + (lca_height[left] - min);
}

int main() {
    int n, m, u, v, w;

    std::cin >> n;
    Graph tree(n);
    std::fill(tree.begin(), tree.end(), std::vector<Node>{});

    for (int i = 0; i < n - 1; i++) {
        std::cin >> u >> v >> w;
        tree[u].emplace_back(v, w);
        tree[v].emplace_back(u, w);
    }

    lca_used = std::vector<bool> (n);
    lca_height = std::vector<int> (n);

    lca_dfs(tree, 0, 0);
    lca_build(n);
    sqrt_build();

    std::cin >> m;
    for (int i = 0; i < m; i++) {
        std::cin >> u >> v;
        std::cout << sqrt_solve(u, v) << std::endl;
    }

    return 0;
}