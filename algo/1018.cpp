#include <iostream>

int apple_count[105][105];
int dp[105][105];
int graph[105][105];
int child_count[105];

int max(int a, int b) {
    return a > b ? a : b;
}

bool used[105];

void build_dp(int idx, int q) {
    used[idx] = true;
    for (int i = 1; i <= child_count[idx]; i++) {
        if (!used[graph[idx][i]]) {
            build_dp(graph[idx][i], q);
            for (int j = q; j >= 0; j--) {
                for (int k = q - j - 1; k >= 0; k--) {
                    dp[idx][j + k + 1] = max(dp[graph[idx][i]][k] + dp[idx][j] + apple_count[idx][graph[idx][i]],
                                             dp[idx][j + k + 1]);
                }
            }
        }
    }
}

int main() {
    int n, q, a, b, c;

    std::cin >> n >> q;
    for (int i = 1; i < n; i++) {
        std::cin >> a >> b >> c;
        child_count[a]++;
        child_count[b]++;
        apple_count[a][b] = c;
        apple_count[b][a] = c;
        graph[a][child_count[a]] = b;
        graph[b][child_count[b]] = a;
    }

    used[0] = true;
    build_dp(1, q);

    std::cout << dp[1][q] << std::endl;

    return 0;
}