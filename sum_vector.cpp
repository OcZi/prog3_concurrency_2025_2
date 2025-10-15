

/*
#include <algorithm>
#include <functional>
#include <iterator>
#include <thread>
#include <vector>
#include <iostream>

template<typename It, typename T>
void sum_vector_seq(It start, It end, T& e) {
    for (auto it = start; it != end; ++it) *it += e;
}


void test_seq() {
    std::vector v{10, 2, 3};

    int i = 10;
    sum_vector_seq(v.begin(), v.end(), i);

    for (auto &e : v) {
        std::cout << e << std::endl;
    }
}

template<typename It, typename T>
void sum_vector_async(It start, It stop, T& e) {
    if (start == stop) return;

    auto total = std::thread::hardware_concurrency();
    auto dist = std::distance(start, stop);
    auto n_threads = std::min(static_cast<int>(total), static_cast<int>(dist));

    auto chunk = dist / total;
    auto res = dist % total;

    std::vector<std::thread> thr;
    thr.reserve(n_threads);

    auto begin = start;
    for (int i = 0; i < n_threads; ++i) {
        auto step = chunk + (i < res ? 1 : 0);
        auto end = std::next(begin, step);

        thr.emplace_back(sum_vector_seq<It, T>, begin, end, std::ref(e));
        begin = end;
    }

    for (auto &e : thr) e.join();
}

void test_parallel() {
    std::vector v{10, 2, 3};

    int i = 10;
    sum_vector_async(v.begin(), v.end(), i);

    for (auto &e : v) {
        std::cout << e << std::endl;
    }
}


int main() {
    test_parallel();
    return 0;
}
    
*/


#include <algorithm>
#include <iostream>
#include <iterator>
#include <thread>
#include <vector>


template<typename It, typename T>
void sum_vector_seq(It start, It stop, T n) {
    if (start == stop) return;

    for (auto it = start; it != stop; ++it) {
        *it += n;
    }
}

template<typename It, typename T>
void sum_vector_async(It start, It stop, T n) {
    if (start == stop) return;

    auto dist = std::distance(start, stop); // distancia == cantidad de elementos en el intervalo [start:end]
    auto total = std::min(static_cast<int>(dist), static_cast<int>(std::thread::hardware_concurrency()));

    int chunk = dist / total;
    int res = dist % total;

    std::vector<std::thread> thr;
    thr.reserve(total);

    auto curr_begin = start;
    for (int i = 0; i < total; ++i) {
        auto n_end = chunk + (i < res ? 1 : 0);
        auto curr_end = std::next(curr_begin, n_end);

        thr.emplace_back(sum_vector_seq<It, T>, curr_begin, curr_end, n);

        curr_begin = curr_end;
    }

    for (auto &t : thr) t.join();

    std::cout << "dist: " << dist << std::endl;
    std::cout << "chunks: " << chunk << ", residuo: " << res << ", threads: " << total << std::endl;
}


void test_seq() {
    std::vector v{10, 2, 3};
    sum_vector_seq(v.begin(), v.end(), 10);
    
    for (auto &e : v) {
        std::cout << e << std::endl;
    }
}

void test_async() {
    std::vector v{10, 2, 3, 8, 5, 2, 0, -1, 8, 3, 4, 5, 6, 2, 3, 4, 0};
    sum_vector_async(v.begin(), v.end(), 8);
    
    for (auto &e : v) {
        std::cout << e << std::endl;
    }
}


int main() {
    test_async();
    return 0;
}