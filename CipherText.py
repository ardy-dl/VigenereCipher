# create function
def encrypt_letters(message, key):
# convert inputs to uppercase
    message = message.upper()
    key = key.upper()
# convert inputs to corresponding letter values (0-25)
    message_number = [ord(letter) - 65 for letter in message if message.isupper()]
    key_number = [ord(letter) - 65 for letter in key if key.isupper()]
# repeat key to match length of message
    key_number = key_number * (len(message_number) // len(key_number) + 1)
    key_number = key_number [:len(message_number)]
# add both numbers
    encrypted_numbers = [(m + k) % 26 for m, k in zip(message_number, key_number)]
# convert encrypted numbers to corresponding letters (A-Z)
    ciphertext = ''.join([chr(value + 65) for value in encrypted_numbers])
# return/print value
    return ("Your ciphertext is: " + ciphertext)

# ask for input, then save
message = input("Enter a message: ")
key = input("Enter a key: ")

# call the functions
ciphertext = encrypt_letters(message, key)

# create design
# turtle graphics for output
# import module
# set up the screen
# set up the pen
# display the text