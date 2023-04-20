# VigenereCipher
#### A method of encrypting alphabetic text by using a series of interwoven Caesar ciphers based on the letters of a keyword. It employs a form of polyalphabetic substitution.
## Vocab
 ### Interwoven Caesar Ciphers 
  - one of the simplest and most widely known encryption techniques. 
  - Letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. 
  ### Polyalphabetic substitution
  - the use of multiple substitution alphabets.
## How it works?
#### It generates a ciphertext to encrypt your message
- You use a keyword as your key which you then convert into the corresponding letter values between 0 and 25. 
- Then, to encrypt, write a message on one row (letters 0 to 25) repeatedly write the keyword below it. add each column and take the result as a modulo of 26. 
- The ciphertext is made up of these number results and prints out your ciphertext.
## How to use?
#### 
1. Enter a message you want to encrypt (all caps with no spaces)
2. Enter the key to help with the encryption of the message (all caps with no spaces)
3. The program will print the ciphertext for your message.
