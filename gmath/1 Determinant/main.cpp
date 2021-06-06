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

    void addLine(std::string line) {
        std::string tmp;
        if (matrix.size() == size) {
            throw -1;
        }
        matrix.emplace_back(size);
        int idx = (int) matrix.size() - 1;

        for (int i = 0; i < size; i++){
            tmp = scanLine(line);
            if(tmp.empty()){
                throw -1;
            }
            matrix[idx][i] = std::stod(tmp);
        }
        if (!scanLine(line).empty()) {
            throw -1;
        }
    }

    bool sizeCheck(){
        return matrix.size() == size;
    }

    double calculateDeterminant() {
        int y = 0, temp, y_max;
        double max, k, ans = 1.0;
        std::vector<double> vec;

        for (int x = 0; x < size; x++) {
            max = matrix[y][x];
            y_max = y;
            temp = y;
            for (temp = y; temp < size; temp++) {
                if (matrix[temp][x] > max) {
                    max = matrix[temp][x];
                    y_max = temp;
                }
            }

            temp = x;
            if (y_max != y) {
                ans *= -1;
                vec = matrix[y];
                matrix[y] = matrix[y_max];
                matrix[y_max] = vec;
            }

            temp = y + 1;
            for (int i = y + 1; i < size; i++) {
                k = -matrix[i][x] / matrix[y][x];
                for (int j = x; j < size; j++) {
                    matrix[i][j] += matrix[y][j] * k;
                    if (abs(matrix[i][j]) < eps){
                        matrix[i][j] = 0;
                    }
                }
            }

            if (matrix[y][y] == 0) {
                return 0;
            }
            y++;
        }

        for (int i = 0; i < size; i++){
            ans *= matrix[i][i];
        }
        return ans;
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
        if(line.empty()){
            if(!m.sizeCheck()){
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

    printf("%f", m.calculateDeterminant());
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