#include <iostream>
#include <cstring>
#include <cstdlib>
#include <chrono>

void selection_sort(double * array, int length){
	for(int i = 0; i < length; ++i){
		//find min index to swap with
		double m = array[i];
        int idx = i;
        //search from current element aka. unsorted part of the array
		for(int j = i; j < length; ++ j){
			if(array[j]< m){
				m = array[j];
				idx = j;
			}
		}
        //swap min and curren (i and idx)
        array[idx] = array[i];
        array[i] = m;
	}
}


int main(int argc, char ** argv){
	int tests[11] = {10, 100, 500, 1000, 1500, 2000, 2500, 3000, 5000, 7500, 10000};
	int m = 11;

	double * array = (double *) std::malloc(tests[m-1] * sizeof(double));

    std::cout << "[";
	for(int i = 0; i < m; ++i){
		//random fill array
		for(int k = 0; k < tests[i]; ++k){
			array[k] = (double) std::rand()/RAND_MAX;
		}
		//start times
		auto start = std::chrono::high_resolution_clock::now();
		
		//sort array
		selection_sort(array, tests[i]);
		
		//stop timer
		auto end = std::chrono::high_resolution_clock::now();

		//std::cout << std::endl;
		//std::cout << tests[i] << " elements sorted in: " << (double) std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count()/1000000000 << "s" << std::endl;
		std::cout << (double) std::chrono::duration_cast<std::chrono::nanoseconds>(end-start).count()/1000000000 << ", ";
	}
    std::cout << "\b\b]" << std::endl;
    std::free(array);
	
}


/** Run with:

    g++ selectionsort.cpp -o main.bin
    ./main.bin 
*/