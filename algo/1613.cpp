#include <iostream>
#include <vector>
#include <tuple>

struct Dababy {
    Dababy(int k, int v) {
        this->idx = k;
        this->val = v;
    }

    int idx;
    int val;
};

bool operator<(const Dababy &x, const Dababy &y) {
    return std::tie(x.val, x.idx) < std::tie(y.val, y.idx);
}

bool operator>(const Dababy &x, const Dababy &y) {
    return std::tie(x.val, x.idx) > std::tie(y.val, y.idx);
}

bool operator<=(const Dababy &x, const Dababy &y) {
    return std::tie(x.val, x.idx) <= std::tie(y.val, y.idx);
}

bool operator>=(const Dababy &x, const Dababy &y) {
    return std::tie(x.val, x.idx) >= std::tie(y.val, y.idx);
}

bool operator==(const Dababy &x, const Dababy &y) {
    return std::tie(x.val, x.idx) == std::tie(y.val, y.idx);
}


void swap(std::vector<Dababy *> &list, int i, int k) {
    Dababy *temp = list[i];
    list[i] = list[k];
    list[k] = temp;
}

int part(std::vector<Dababy *> &list, int l, int r) {
    Dababy val = *list[(l + r) / 2];
    while (true) {
        while (*list[l] < val) {
            l++;
        }
        while (*list[r] > val) {
            r--;
        }
        if (l >= r) {
            return r;
        }
        swap(list, l, r);
        l++;
        r--;
    }
}

void quickSort(std::vector<Dababy *> &list, int l, int r) {
    if (l < r) {
        int q = part(list, l, r);
        quickSort(list, l, q);
        quickSort(list, q + 1, r);
    }
}

int binSearch(std::vector<Dababy *> &list, Dababy &value, int mode = 0) {
    int l = 0, r = (int) list.size() - 1, mid = (l + r) / 2;
    while ((l + 1) < r) {
        if ((mode == 0 && *list[mid] >= value) || (mode == 1 && *list[mid] > value)) {
            r = mid;
        } else {
            l = mid;
        }
        mid = (l + r) / 2;
    }

    //std::cout << "l: " << l << " r: " << r << " mode: " << mode << std::endl;

    if(*list[l] == value){
        return l;
    } else {
        return r;
    }
}

int check(std::vector<Dababy *> &list, int from, int to, int value) {
    int l_idx = binSearch(list, *new Dababy(from, value), 0),
            r_idx = binSearch(list, *new Dababy(to, value), 1);

    if (r_idx == l_idx && list[l_idx]->val == value && list[l_idx]->idx >= from && list[l_idx]->idx <= to) {
        return 1;
    } else if(r_idx == 1 && l_idx == 1 && list[l_idx - 1]->val == value && list[l_idx - 1]->idx >= from && list[l_idx - 1]->idx <= to){
        return 1;
    } else {
        return (int) (r_idx != l_idx);
    }
}


int main() {
    int cnt, from, to, t;
    std::cin >> cnt;
    std::vector<Dababy *> els(cnt);

    for (int i = 0; i < cnt; i++) {
        std::cin >> t;
        els[i] = new Dababy(i + 1, t);
    }
    quickSort(els, 0, cnt - 1);

//    for (auto & el : els) {
//        std::cout << el->val << " ";
//    }
//    std::cout << std::endl;

    std::cin >> cnt;
    for (int i = 0; i < cnt; i++) {
        std::cin >> from >> to >> t;
        std::cout << check(els, from, to, t);
    }

    return 0;
}