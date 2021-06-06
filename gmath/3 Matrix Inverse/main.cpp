#include <iostream>
#include <fstream>
#include <vector>
#include <string>

#define TDVector std::vector<std::vector<double>>

std::string scanLine(std::string &line) {
    int pos;
    std::string substring;

    pos = line.find(' ');
    if (pos == -1) {
        substring = line.substr(0, line.size());
        line.erase(0, line.size());
        return substring;
    }

    substring = line.substr(0, pos);
    line.erase(0, pos + 1);

    return substring;
}

class QMatrix {
private:
    TDVector matrix;
    int size;
    double eps;
public:
    explicit QMatrix(int s, double e) {
        size = s;
        eps = e;
        matrix = {};
    }

    explicit QMatrix(const TDVector& v) {
        size = v.size();
        eps = 0.0000001;
        matrix = v;
    }

    void addLine(std::string line) {
        std::string tmp;
        if (matrix.size() == size) {
            throw -1;
        }
        matrix.emplace_back(size);
        int idx = (int) matrix.size() - 1;

        for (int i = 0; i < size; i++) {
            tmp = scanLine(line);
            if (tmp.empty()) {
                throw -1;
            }
            matrix[idx][i] = std::stod(tmp);
        }
        if (!scanLine(line).empty()) {
            throw -1;
        }
    }

    bool sizeCheck() {
        return matrix.size() == size;
    }

    void print(){
        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < size; ++j) {
                std::cout << matrix[i][j] << " ";
            }
            std::cout << std::endl;
        }
    }

    double calculateDeterminant() {
        TDVector calc(matrix);
        int y = 0, temp, y_max;
        double max, k, ans = 1.0;
        std::vector<double> vec;

        for (int x = 0; x < size; x++) {
            max = calc[y][x];
            y_max = y;
            temp = y;
            for (temp = y; temp < size; temp++) {
                if (calc[temp][x] > max) {
                    max = calc[temp][x];
                    y_max = temp;
                }
            }

            temp = x;
            if (y_max != y) {
                ans *= -1;
                vec = calc[y];
                calc[y] = calc[y_max];
                calc[y_max] = vec;
            }

            temp = y + 1;
            for (int i = y + 1; i < size; i++) {
                k = -calc[i][x] / calc[y][x];
                for (int j = x; j < size; j++) {
                    calc[i][j] += calc[y][j] * k;
                    if (abs(calc[i][j]) < eps) {
                        calc[i][j] = 0;
                    }
                }
            }

            if (calc[y][y] == 0) {
                return 0;
            }
            y++;
        }

        for (int i = 0; i < size; i++) {
            ans *= calc[i][i];
        }
        return ans;
    }

    double minorDeterminant(int x, int y){
        TDVector minor(size - 1, std::vector<double>(size - 1, 0));
        int xx, yy;

        for(int i = 0; i < size; i++){
            if(i == x) continue;
            xx = i > x ? i - 1 : i;
            for(int j = 0; j < size; j++){
                if(j == y) continue;
                yy = j > y ? j - 1 : j;
                minor[xx][yy] = matrix[i][j];
            }
        }
        return QMatrix(minor).calculateDeterminant();
    }

    void invert() {
        double det;
        TDVector safe(matrix);

        det = calculateDeterminant();
        if (det == 0) {
            std::cout << "det() = 0" << std::endl;
            return;
        }

        transpose();
        for(int i = 0; i < size; i++){
            for(int j = 0; j < size; j++){
                safe[i][j] = minorDeterminant(i, j) / det;
            }
        }

        matrix = safe;
    }

    void transpose() {
        TDVector b(matrix);
        for (int i = 0; i < size; i++) {
            for (int j = 0; j < size; j++) {
                b[i][j] = matrix[j][i];
            }
        }
    }
};

void task(std::istream &in) {
    int size = 1;
    std::string line;

    getline(in, line);
    for (char i : line) {
        if (i == ' ') {
            size++;
        }
    }

    QMatrix m(size, 0.0000001);
    do {
        if (line.empty()) {
            if (!m.sizeCheck()) {
                printf("Wrong matrix");
                return;
            }
            break;
        }
        try {
            m.addLine(line);
        } catch (int) {
            printf("Wrong matrix");
            return;
        }
    } while (getline(in, line));

    double det, iDet;
    det = m.calculateDeterminant();
    printf("Matrix determinant: %f\n\n", det);

    m.invert();
    m.print();
    iDet = m.calculateDeterminant();
    printf("Inverted matrix determinant: %f\n\n", iDet);

    printf("Check 1/det() == det-1(): %d", (1/det - iDet) < 0.000001);
}

int main(int argc, char **argv) {
    if (argc > 1) {
        std::ifstream in(argv[1]);
        if (!in.is_open()) {
            printf("Failed to open file %s", argv[1]);
            return 0;
        }
        task(in);
        in.close();
    } else {
        task(std::cin);
    }
    return 0;
}