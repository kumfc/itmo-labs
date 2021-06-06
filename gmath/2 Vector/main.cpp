#include <iostream>
#include <fstream>
#include <vector>
#include <string>

typedef std::vector<std::vector<double>> Matrix;

double vector_mul(const Matrix &mat, int N, std::string &res, bool root = false) {
    Matrix subsequent_matrix(N, std::vector<double>(N));
    double ching_chong = 0;

    if (N == 2) {
        return (mat[0][0] * mat[1][1]) - (mat[1][0] * mat[0][1]);
    } else {
        for (int k = 0; k < N; k++) {
            int q = 0;
            for (int i = 1; i < N; i++) {
                int p = 0;
                for (int j = 0; j < N; j++) {
                    if (j == k) {
                        continue;
                    }
                    subsequent_matrix[q][p] = mat[i][j];
                    p++;
                }
                q++;
            }
            if(root) ching_chong = 0;
            ching_chong += pow(-1, k) * mat[0][k] * vector_mul(subsequent_matrix, N - 1, res);
            if(root) {
                res += std::to_string(ching_chong) + " ";
            }
        }
        return ching_chong;
    }
}

double scalar_mul(const Matrix &mat, int N) {
    double res = 0, t;

    for (int j = 0; j < N; j++) {
        t = 1;
        for (int i = 0; i < N; i++) {
            t *= mat[i][j];
        }
        res += t;
    }
    return res;
}

int task(std::istream &in) {
    int N;

    std::cout << "Введите размер: " << std::endl;
    in >> N;

    Matrix m;
    m.resize(N);
    m[0].resize(N);

    for (int i = 0; i < N; i++) {
        m[0][i] = 1;
    }

    for (int i = 1; i < N; i++) {
        std::cout << "Введите вектор " << i << ":" << std::endl;
        m[i].resize(N);
        for (int j = 0; j < N; j++) {
            in >> m[i][j];
        }
    }

    std::cout << "Скалярное произведение: " << scalar_mul(m, N) << std::endl;

    std::string vm_res;
    vector_mul(m, N, vm_res, true);
    std::cout << "Векторное произведение: " << vm_res.c_str() << std::endl;

    return 0;
}

int main(int argc, char **argv) {
    setlocale(LC_ALL, "ru_RU.UTF-8");

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