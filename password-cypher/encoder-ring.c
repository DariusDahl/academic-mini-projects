/**
 * COSC 3250 - Project 1
 * This program encodes the string provided.
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
            int encryptedNum;
            int encryptedStrNum;
            char encryptedStr;

            upperChar = toupper(myChar); // Convert the character to uppercase for consistency

            if (upperChar >= 'A' && upperChar <= 'Z') { // Check if the character is an alphabetical character
                numChar = (int) upperChar - 'A' + 1; // Convert the character to a number between 1 and 26
                encryptedNum = numChar + key + total; // Add the key and total to the number to encrypt it
                encryptedStrNum = ((encryptedNum % 27) + 'A' - 1); // Convert the encrypted number back to a character
                if (encryptedStrNum < 'A' || encryptedStrNum > 'Z') { // If the encrypted character is not an alphabetical character, set it to a space
                    encryptedStrNum = 0;
                }
                encryptedStr = (char) encryptedStrNum; // Convert the encrypted character to a char
            } else { // If the character is not an alphabetical character, set it 0 and go from there
                numChar = 0;
                encryptedNum = numChar + key + total; 
                encryptedStrNum = ((encryptedNum % 27) + 'A' - 1);
                encryptedStr = (char) encryptedStrNum;
            } 
            total = encryptedNum; // Set the total to the encrypted number for the next iteration
            if (encryptedStr < 'A' || encryptedStr > 'Z') { // If the encrypted character is not an alphabetical character, set it to a space
                encryptedStr = ' ';
            }
            putchar(toupper(encryptedStr)); // Print the encrypted character
        } else { // If the character is a newline, print a newline
            printf("\n");
        }
        myChar = getchar(); // Get the next character from the input string until EOF is reached
    }
    return 0;
}