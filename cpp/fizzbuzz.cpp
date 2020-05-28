#include <iostream>

void fizzbuzz(int max) {
    for (int i = 1; i <= max; i++) {
        // Determine if Fizz and/or Buzz will be displayed
        bool fizz = (i % 3) == 0;
        bool buzz = (i % 5) == 0;

        // If current number is not divisible by 3 or 5, output the number. 
        if (!fizz && !buzz) {
            std::cout << i;
        }
        else {
            // If current number is divisible by 3, output "Fizz"
            if (fizz) {
                std::cout << "Fizz";
            }
            // If current number is divisible by 5, output "Buzz"
            if (buzz) {
                std::cout << "Buzz";
            }
        }
        // Output a newline
        std::cout << "\n";
    }
}

int main() {
    // Run the FizzBuzz function on all numbers 1-100
    fizzbuzz(100);
    return 0;
}