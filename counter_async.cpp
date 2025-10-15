
#include <algorithm>
#include <iostream>
#include <mutex>
#include <thread>
#include <vector>

/*
std::mutex mut;
int counter = 0;

int count_seq() {
    return ++counter;
}

void counter_to_100() {
    // std::lock_guard lg(mut);
    int n = 100;
    while (n > 0) {
        count_seq();
        --n;
    }
}

template<size_t THREADS>
void run_threads() {
    std::vector<std::thread> thr;
    thr.reserve(THREADS);

    for (int i = 0; i < THREADS; ++i) thr.emplace_back(counter_to_100);
    for (auto &t : thr) t.join();
}

int main() {
    int n;
    std::cout << "Número de ejecuciones async: ";
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        run_threads<10>(); // resultado == 1000;
        if (counter != 1000) std::cout << "Se desincronizó en iteración " << i << std::endl;
        counter = 0;
    }
    return 0;
}
*/




int counter{};
std::mutex mux;

void sum_one() {
    std::lock_guard lg(mux);
    counter += 1;
}

void test_seq() {
    for (int i = 0; i < 100; ++i) {
        sum_one();
    }
}

void test_async() {
    auto total = std::min(10, static_cast<int>(std::thread::hardware_concurrency()));

    std::vector<std::thread> vec;
    vec.reserve(total);

    for (int i = 0; i < 10; ++i) {
        vec.emplace_back(test_seq);
    }

    for (auto &t : vec) {
        t.join();
    }
}

void try_async(int n) {
    for (int i = 0; i < n; ++i) {
        test_async();
        if (counter != 1000) std::cout << "Falla en iteración " << i << std::endl;
        counter = 0;
    }
}

int main() {
    try_async(1000);
    return 0;
}







