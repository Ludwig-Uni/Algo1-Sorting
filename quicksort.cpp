
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <chrono>


int partition(double * array, int lo, int hi){
    /*
    Wählt das mittlere Element des Arrays (zwischen den Grenzen lo und hi)
    als Pivot-Element, sortiert alle x > pivor rechts und alle x < pivot links davon
    und gibt den Index des Pivot-Elements zurück.
     */
    double piv = array[(int) (lo+hi)/2];
    int i = lo;
    int j = hi;

    double tmp;
    while(true){
        while(array[i] < piv){
            ++i;
        }
        while(array[j] > piv){
            --j;
        }

        if(i >= j){
            return j;
        }
        tmp = array[i];
        array[i] = array[j];
        array[j] = tmp;
    }
}



void quicksort_worker(double * array, int lo, int hi){
    if(lo >= 0 and hi >= 0 and lo < hi){
        int p = partition(array, lo, hi);
        quicksort_worker(array, lo, p);
        quicksort_worker(array, p+1, hi);
    }
}

void quicksort(double * array, size_t length){
    //sortiere das gegebene Array 'array' mit länge 'length' mit einem Quicksort algorithmus
    quicksort_worker(array, 0, length-1);
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
		quicksort(array, tests[i]);
		
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

    g++ quicksort.cpp -o main.bin
    ./main.bin 
*/