# Caesar Cipher Program in Python

This program demonstrates a classic **Caesar Cipher encryption and decryption** system, broken down into reusable modules and functions for clarity and maintainability.

The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is "shifted" a certain number of places down the alphabet.

---

## What You'll Learn

- How to implement a Caesar Cipher algorithm in Python  
- How to modularize code using functions and separate files  
- How to work with strings and user input  
- How encryption and decryption work using symmetric keys

---

## Code Breakdown

### Main Script: `runCaesarCipherProgram()`
This function coordinates the entire process:
1. Defines the base alphabet: `A-Z`
2. Duplicates the alphabet (to handle wrap-around encryption)
3. Accepts a message and a cipher key from the user
4. Encrypts the message using the Caesar Cipher logic
5. Decrypts it to verify the result

### Supporting Modules:
| Module File           | Function Purpose                           |
|------------------------|--------------------------------------------|
| `getDoubleAlphabet.py` | Returns the alphabet repeated twice        |
| `getMessage.py`        | Prompts the user to input a message        |
| `getCipherKey.py`      | Prompts the user to input a numeric key    |
| `encryptMessage.py`    | Encrypts the input message using the key   |
| `decryptMessage.py`    | Decrypts the message using the same key    |

---

## Sample Output
Alphabet: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Alphabet2: ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ
Enter your message: HELLO
Enter a key (number 1–25): 3
Encrypted Message: KHOOR
Decrypted Message: HELLO



---

## Why This Matters

Encryption is a critical part of cybersecurity. This lab introduces you to:
- The concept of **symmetric key encryption**
- The importance of **modular programming**
- How to break problems down into **functions and files**

This is more than a beginner exercise — it’s your foundation in secure communication.

---

> Bonus Challenge: Try adding lowercase support, or extend this to support ROT13 or Vigenère Cipher.

Happy encrypting!
