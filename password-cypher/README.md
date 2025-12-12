# Password Cypher Projects

This directory contains a series of mini-projects aimed at working with encoding and decoding strings based on cyphers. These projects demonstrate techniques for encryption and decryption, utilizing basic inputs and modular arithmetic to perform transformations on the input text.

## Files Overview

### 1. [codebreaker.c](https://github.com/DariusDahl/academic-mini-projects/blob/main/password-cypher/codebreaker.c)
- **Description**: This program attempts to break a cyphertext by determining the most probable key used for encryption. It uses frequency analysis to identify the most likely key based on the occurrence of the letter 'E' in decoded strings, as 'E' is one of the most common letters in English text.
- **How It Works**:
  - Takes an encoded string as input.
  - Analyzes all possible key values to find the second-best probable match (to account for spaces being mistakenly counted).
  - Decodes the string using the key and prints the result.
- **Requirements**:
  - Input: Cyphertext to decode (via `stdin`).
  - No arguments are required when executing this program.

### 2. [decoder-ring.c](https://github.com/DariusDahl/academic-mini-projects/blob/main/password-cypher/decoder-ring.c)
- **Description**: This program decodes an encoded string based on a user-provided key. It maps character values and performs modular arithmetic to decode the string.
- **How It Works**:
  - Accepts a key as the first command-line argument.
  - Reads an encoded string from `stdin` and outputs the decoded text.
- **Requirements**:
  - Input: Encoded cyphertext to decode (via `stdin`).
  - Command-line arguments:
    - `key`: A numerical key used to decode the string. If no key is provided, the default key value is `0`.

### 3. [encoder-ring.c](https://github.com/DariusDahl/academic-mini-projects/blob/main/password-cypher/encoder-ring.c)
- **Description**: This program encodes a plain text string using a user-provided key. It creates an encrypted string by applying modular arithmetic transformations on the input characters.
- **How It Works**:
  - Accepts a key as the first command-line argument.
  - Reads a plain string from `stdin` and outputs the encoded (cyphertext) text.
- **Requirements**:
  - Input: Plain text to encode (via `stdin`).
  - Command-line arguments:
    - `key`: A numerical key used to encode the string. If no key is provided, the default key value is `0`.

## General Requirements
- All programs include the following:
  - Input comes from standard input (e.g., keyboard or redirected files).
  - Output is printed to standard output.
  - C99-compatible compiler (e.g., `gcc`).
- Compilation: To compile any of these files, use the following command:
  ```bash
  gcc -o <output_filename> <source_code_file.c>
  ```
- Example usage:
  - Encoding text:
    ```bash
    ./encoder-ring 4 < plaintext.txt
    ```
  - Decoding text:
    ```bash
    ./decoder-ring 4 < encoded.txt
    ```
  - Breaking a cypher (no key necessary):
    ```bash
    ./codebreaker < cyphertext.txt
    ```

## Instructor and Documentation
- Author: **Darius Dahl**
- Instructor: **Dr. Brylow**
- Contact: [darius.dahl@marquette.edu](mailto:darius.dahl@marquette.edu)

Explore these programs to better understand the fundamentals of encoding, decoding, and frequency analysis in cryptography!
