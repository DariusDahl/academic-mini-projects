/**
 * COSC 3250 - Project 1
 * This program decodes the encoded string.
 * @author Darius Dahl
 * Instructor: Dr. Brylow
 * TA-BOT:MAILTO darius.dahl@marquette.edu
 */

#include <stdio.h>
#include <stdlib.h> // For atoi()
#include <ctype.h> // For toupper()

int main(int argc, char *argv[]) {
    // instance variables
    int key;
    int total = 0;

    if (argc > 1) { // Check if a key was provided, set key as the first argument value
        key = atoi(argv[1]);
    } else { // If no key was provided, set key to 0
        key = 0;
    }

    char myChar = getchar(); // Get the first character from input string

    while (myChar != EOF) { // Loop through the input string until EOF is reached
        if (myChar != 10) { // 10 is the ASCII value for a newline
            // instance variables
            char upperChar;
            int numChar;

            upperChar = toupper(myChar); // Convert the character to uppercase for consistency
            numChar = (int) upperChar - 'A' + 1; // Convert the character to a number between 1 and 26

            if (numChar < 1 || numChar > 26) { // If the character is not an alphabetical character, set it to 0
                numChar = 0;
            }

            int tempTotal = (numChar - key - total) % 27; // Subtract the key and total from the number to decrypt it 

            while (tempTotal < 0) { // If the tempTotal is negative, add 27 to it
                tempTotal += 27;
            }

            total = numChar; 

            char tempChar = tempTotal + 'A' - 1; // Convert the decrypted number back to a character
            if (tempChar < 'A' || tempChar > 'Z') { // If the decrypted character is not an alphabetical character, set it to a space
                tempChar = ' ';
            }
            putchar(tempChar);
        } else { // If the character is a newline, print a newline
            printf("\n");
        }
        myChar = getchar(); // Get the next character from the input string until EOF is reached
    }
    return 0;
}