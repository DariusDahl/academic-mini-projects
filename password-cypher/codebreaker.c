/**
 * COSC 3250 - Project 2
 * This program breaks a given cyphertext by determining it's key, then prints the decoded string with that key.
 * @author Darius Dahl
 * Instructor: Dr. Brylow
 * TA-BOT:MAILTO darius.dahl@marquette.edu
 */

/* Idea for this project:
decode should return a value, that value being a counter that increments every time an E is detected
after being decoded. That value should be stored in an array, and the index of that array should be
equivalent to the key value. Compare the values at each index (key) and return the key with the highest
value. If there is a tie, return the lower value key. print out the key with the second highest count of E's
We want the second highest count of E's because the highest count will likely be counting the key that is
counting spaces as E's. The second highest count will likely be the key that is counting the actual E's.
*/

#include <stdio.h> 
#include <string.h> // For strlen()
#include <stdlib.h> // For atoi()
#include <ctype.h> // For toupper()

#define MAX_STRING_LENGTH 1025 // one larger than required for null terminator, (supposed to be size 1024)

// Decode the given string with the given key, return the number of E's in the decoded string
int decode(int key, char *myString) {
    int total = 0;
    int count = 0; // count the number of E's in the string after being decoded

    for (int i = 0; i < strlen(myString); i++) {
        if (myString[i] != 10) { // 10 is the ASCII value for a newline
            char upperChar = toupper(myString[i]);
            int numChar = (int)upperChar - 'A' + 1; // Convert the character to a number between 1 and 26

            if (numChar < 1 || numChar > 26) { // If the character is not an alphabetical character, set it to 0
                numChar = 0;
            }

            int tempTotal = (numChar - key - total + 27) % 27; // Adjust for previous character's influence and ensure within bounds
            while(tempTotal < 0) { // If the tempTotal is negative, add 27 to it
                tempTotal += 27;
            }

            total = numChar; 

            char tempChar = tempTotal + 'A' - 1; // Convert the decrypted number back to a character
            if (tempChar < 'A' || tempChar > 'Z') { // If the decrypted character is not an alphabetical character, set it to a space
                tempChar = ' ';
            }

            if (tempChar == 'E') { // count the number of E's in the string after being decoded
                count++;
            }
        }
    } 
    total = 0; // Reset total for the new line
    return count;
}

// Print the decoded string with the given key
void printDecodedString(int key, char *myString) {
    int total = 0;

    for (int i = 0; i < strlen(myString); i++) {
        if (myString[i] != 10) { // 10 is the ASCII value for a newline
            char upperChar = toupper(myString[i]);
            int numChar = (int)upperChar - 'A' + 1; // Convert the character to a number between 1 and 26

            if (numChar < 1 || numChar > 26) { // If the character is not an alphabetical character, set it to 0
                numChar = 0;
            }

            int tempTotal = (numChar - key - total + 27) % 27; // Adjust for previous character's influence and ensure within bounds
            while (tempTotal < 0) { // If the tempTotal is negative, add 27 to it
                tempTotal += 27;
            }

            total = numChar; 

            char tempChar = tempTotal + 'A' - 1; // Convert the decrypted number back to a character
            if (tempChar < 'A' || tempChar > 'Z') { // If the decrypted character is not an alphabetical character, set it to a space
                tempChar = ' ';
            }
            putchar(tempChar);
        } else {
            printf("\n");
        }
    } 
    printf("\n");
    total = 0; // Reset total for the new line
}

// Find the index of the second-highest value in the given array and return it. That index is equal to the key value
int findSecondHighestIndex(int array[], int arraySize) {
    // Initialize variables to -1 so that the first value in the array will be higher than them
    int highestValue = -1;
    int secondHighestValue = -1;
    int highestIndex = -1;
    int secondHighestIndex = -1;

    for (int i = 0; i < arraySize; i++) { // Loop through the array to find the highest value
        if (array[i] > highestValue) {
            secondHighestValue = highestValue;
            secondHighestIndex = highestIndex;
            highestValue = array[i];
            highestIndex = i;
        } else if (array[i] > secondHighestValue) { // If the value is not higher than the highest value, check if it is higher than the second-highest value
            secondHighestValue = array[i];
            secondHighestIndex = i;
        }
    }
    return secondHighestIndex;  // Return the index of the second-highest value
}


int main() {
    int myChar = 0;
    int arraySize = 27;
    int i = 0;
    int key = 0;
    
    char *myString = NULL;
    myString = (char *) malloc(MAX_STRING_LENGTH * sizeof(char)); // dynamic allocation

    if (myString == NULL) { // Check if memory was allocated
        printf("Error allocating memory!\n");
        return -1;
    }

    while ((myChar = getchar()) != EOF /* && myChar != '\n' */ && i < MAX_STRING_LENGTH - 1) {
        myChar = toupper(myChar); // Convert the character to uppercase for consistency
        myString[i] = myChar;
        i++;
    }
    myString[i] = '\0'; // Add null terminator to end of string

    int arrayForEs[arraySize]; // array to store the number of E's for each key value
    for (int initVal = 0; initVal < arraySize; initVal++) { // initialize array to 0
        arrayForEs[initVal] = 0;
    }

    // idea for loop is to decode with all possible keys and store the number of E's for each key in an array
    for (int key = 0; key < arraySize; key++) {
        arrayForEs[key] = decode(key, myString);
    }
    printf("\n");

    int indexToCheck = 0;
    int valueAtIndex = arrayForEs[indexToCheck];

    // Call the findSecondHighestIndex function to find the second highest value in the array
    int probableKey = findSecondHighestIndex(arrayForEs, arraySize);
    if (strlen(myString) == 0) { // If the input string is empty, set the most probable key to 0
        probableKey = 0;
    }
    printf("Most probable key is %d\n", probableKey);
    printDecodedString(probableKey, myString);

    return 0;
}
