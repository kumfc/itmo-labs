#include <iostream>
#include <vector>
#include <set>
#include <tuple>

struct Point {
    explicit Point(int v, int type, int id = -1, int second = -1) : v(v), type(type), id(id), second(second) {}

    int v, type, id, second;
};

inline bool operator<(const Point &l, const Point &r) {
    return abs(l.second - l.v) < abs(r.second - r.v);
}

void swap(std::vector<Point> &list, int i, int k) {
    Point temp = list[i];
    list[i] = list[k];
    list[k] = temp;
}

int part(std::vector<Point> &list, int l, int r) {
    Point target = list[(l + r) / 2];
    while (true) {
        while (std::tie(list[l].v, list[l].type) < std::tie(target.v, target.type)) {
            l++;
        }
        while (std::tie(list[r].v, list[r].type) > std::tie(target.v, target.type)) {
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

void quickSort(std::vector<Point> &list, int l, int r) {
    if (l < r) {
        int q = part(list, l, r);
        quickSort(list, l, q);
        quickSort(list, q + 1, r);
    }
}

int main() {
    int n, m, l, r, t;
    std::cin >> n;
    std::vector<Point> points;

    for (int i = 0; i < n; i++) {
        std::cin >> l >> r;
        points.emplace_back(l, 0, i, r);
        points.emplace_back(r, 2, i, l);
    }

    std::cin >> m;
    for (int i = 0; i < m; i++) {
        std::cin >> t;
        points.emplace_back(t, 1);
    }

    quickSort(points, 0, (int) points.size() - 1);

    std::set<Point> ranges;
    for (auto point: points) {
        if (point.type == 0) {
            ranges.insert(point);
        } else if (point.type == 2) {
            ranges.erase(point);
        } else if (point.type == 1) {
            if (ranges.empty()) {
                std::cout << -1 << std::endl;
            } else {
                std::cout << ranges.begin()->id + 1 << std::endl;
            }
        }
    }

    return 0;
}