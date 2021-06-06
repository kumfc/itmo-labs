#include <iostream>
#include <vector>


struct Segment{
    int l, r, id;
    explicit Segment(int l, int r, int id) : l(l), r(r), id(id) {}
};

void swap(std::vector<Segment> &list, int i, int k){
    Segment temp = list[i];
    list[i] = list[k];
    list[k] = temp;
}

int part(std::vector<Segment> &list, int l, int r) {
    int val = list[(l + r) / 2].l;
    while (true) {
        while (list[l].l < val) {
            l++;
        }
        while (list[r].l > val) {
            r--;
        }
        if (l >= r) {
            return r;
        }
        swap(list, l, r);
        l++; r--;
    }
}

void quickSort(std::vector<Segment> &list, int l, int r) {
    if (l < r) {
        int q = part(list, l, r);
        quickSort(list, l, q);
        quickSort(list, q + 1, r);
    }
}

int main(){
    int n, l, r, max = 0, max_idx = 0;
    std::cin >> n;

    std::vector<Segment> segments = {};
    std::vector<int> depth(n);
    std::vector<int> path(n);
    std::fill(path.begin(), path.end(), -1);

    for(int i = 0; i < n; i++){
        std::cin >> l >> r;
        segments.emplace_back(l, r, i + 1);
    }
    quickSort(segments, 0, segments.size() - 1);

    for(int i = 0; i < n; i++){
        depth[i] = 1;
        for(int j = i - 1; j >= 0; j--){
            if(segments[i].l > segments[j].l && segments[i].r < segments[j].r){
                if(depth[j] + 1 > depth[i]){
                    depth[i] = depth[j] + 1;
                    path[i] = j;
                }
            }
        }
    }

    for(int i = 0; i < n; i++) {
        if(depth[i] > max){
            max = depth[i];
            max_idx = i;
        }
    }

    std::cout << max << std::endl;
    while(max_idx > -1) {
        std::cout << segments[max_idx].id << " ";
        max_idx = path[max_idx];
    }

    return 0;
}