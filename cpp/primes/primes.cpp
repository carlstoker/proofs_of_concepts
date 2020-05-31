// Sieve of Eratosthenes

#include <iostream>
#include <math.h>
#include <vector>

/**
 * Generate a vector of prime numbers between 2 and the limit parameter.
 * @param limit Ending integer to test for prime numbers
 * @return Vector of prime numbers through limit.
 */
std::vector<int> prime_sieve(unsigned int limit) {
    // Create vector of numbers, with each number defaulted to a true value.
    std::vector<bool> sieve(limit, true);

    // 0 and 1 are not considered prime
    sieve[0] = false;
    sieve[1] = false;


    // Iterate through each integer between 2 and the square root of the target
    // integer.
    for (int i = 2; i <= (int(sqrt(limit)) + 1); i++) {
        int pointer = i * 2;

        // Mark each multiple of the pointer as not being prime
        while (pointer < limit) {
            sieve[pointer] = false;
            pointer += i;
        }
    }

    // Create primes vector from the elements with a true value in the sieve
    // vector.
    std::vector<int> primes;
    for (int i = 0; i < limit; i++) {
        if (sieve[i]) {
            primes.insert(primes.end(), i);
        }
    }

    return primes;
}

int main() {
    int limit;

    std::cout << "Enter maximum number: ";
    std::cin >> limit;

    std::vector<int> primes = prime_sieve(limit);

    std::cout << primes.size() << " primes found through " << limit << ": ";
    for (int i = 0; i < primes.size(); i++) {
        std::cout << primes[i] << " ";
    }
}
