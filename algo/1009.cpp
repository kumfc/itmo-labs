#include <iostream>


int main(){
    int n, k;
    int els[18];
    std::cin >> n >> k;

    els[0] = 0;
    els[1] = k - 1;
    els[2] = (k - 1) * k;
    for(int i = 3; i <= n; i++){
        els[i] = (k - 1) * (els[i - 1] + els[i - 2]);
    }

    std::cout << els[n];

    return 0;
}