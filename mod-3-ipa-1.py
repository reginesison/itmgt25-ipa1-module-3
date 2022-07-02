'''Module 3: Individual Programming Assignment 1

Thinking Like a Programmer

This assignment covers your intermediate proficiency with Python.
'''

from dataclasses import asdict
from imp import new_module
import math

def shift_letter(letter, shift):
    '''Shift Letter. 
    5 points.
    
    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter. 

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if shift == "_": 
        return letter
    elif (alphabet.index(letter) + shift) > 25:
        factor = math.floor((alphabet.index(letter) + shift)/ 26)
        new_index = alphabet.index(letter) + shift - (factor*26)
        return alphabet[new_index]
    else: 
        new_index = alphabet.index(letter) + shift
        return alphabet[new_index]

# shift_letter("X", 104)

def caesar_cipher(message, shift):
    '''Caesar Cipher. 
    10 points.
    
    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters. 

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    new_message = ""
    for m in message:
        if m == " ":
            shifted_letter = shift_letter(m, "_")
            new_message += shifted_letter
        else:
            shifted_letter = shift_letter(m, -shift)
            new_message += shifted_letter

    print(new_message)
    return new_message


# caesar_cipher("HELLO WORLD", 3)

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter. 
    10 points.
    
    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1, 
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    if letter_shift == "_": 
        return letter
    elif (alphabet.index(letter) + alphabet.index(letter_shift)) > 25:
        factor = math.floor((alphabet.index(letter) + alphabet.index(letter_shift))/ 26)
        new_index = alphabet.index(letter) + alphabet.index(letter_shift) - (factor*26)
        return alphabet[new_index]
    else: 
        new_index = alphabet.index(letter) + alphabet.index(letter_shift)
        return alphabet[new_index]

# shift_by_letter("B", "K")


def vigenere_cipher(message, key):
    '''Vigenere Cipher. 
    15 points.
    
    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the 
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.

    m_length = len(message)
    k_length = len(key)

    new_message = ""

    if m_length > k_length: 
        factor = math.floor(m_length / k_length)
        
        new_key = key.join([key]*factor)

        new_key = new_key[:-(m_length - (k_length * factor) - 1)] 

        for index_m, m in enumerate(message):
            for index_k, k in enumerate(new_key):
                if (index_m == index_k):    
                    if m == " ":
                        shifted_letter = shift_by_letter(m, "_")
                        new_message += shifted_letter
                    else:                        
                        shifted_letter = shift_by_letter(m, k)
                        new_message += shifted_letter
    else: 
        for index_m, m in enumerate(message):
            for index_k, k in enumerate(key):
                if (index_m == index_k):    
                    if m == " ":
                        shifted_letter = shift_by_letter(m, "_")
                        new_message += shifted_letter
                    else:                        
                        shifted_letter = shift_by_letter(m, k)
                        new_message += shifted_letter

    
    print(new_message)
    return new_message

# vigenere_cipher("LONGTEXT", "KEY")

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.
    
    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of 
        parchment that contained a string of apparent gibberish. The parchment, 
        when read using the scytale, would reveal a message due to every nth 
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number. 
        For this example, we will use "INFORMATION_AGE" as 
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of 
        the shift. If it is not, add additional underscores 
        to the end of the message until it is. 
        In this example, "INFORMATION_AGE" is already a multiple of 3, 
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message. 
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message. 
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case, 
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    m_length = len(message)

    count = 0
    new_m = ""

    if (m_length % shift == 0):
        parts = [message[i:i+int(m_length / shift)] for i in range(0, len(message), int(m_length / shift))]

        item_len = len(parts[0])
        
        message_array = []

        while count < item_len:
            message_array += [row[count] for row in parts]
            count += 1
        

        for letter in message_array:
            new_m += letter
        
    else:
        parts = [message[i:i+int((m_length / shift)+1)] for i in range(0, len(message), int((m_length / shift)+1))]

        item_len = len(parts[0])
        # print(int((m_length / shift)+1)*shift)
        
        message_array = []

        for i, p in enumerate(parts):
            if (item_len != len(p)):
                p_extra = item_len - int(len(p))
                p += "_"*p_extra
                parts[i] = p

        while count < item_len:
            message_array += [row[count] for row in parts]
            count += 1
        

        for letter in message_array:
            new_m += letter
        
        
    print(new_m)
    return new_m


# scytale_cipher("INFORMATION_AGE", 3)
# scytale_cipher("INFORMATION_AGE", 4)
# scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8)

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code. 
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    m_length = len(message)

    count = 0
    new_m = ""

    if (m_length % shift == 0):
        parts = [message[i:i+int(shift)] for i in range(0, len(message), int(shift))]

        item_len = len(parts[0])
        
        message_array = []

        while count < item_len:
            message_array += [row[count] for row in parts]
            count += 1
        

        for letter in message_array:
            new_m += letter
        
    else:
        parts = [message[i:i+int((shift)+1)] for i in range(0, len(message), int((shift)+1))]

        item_len = len(parts[0])
        
        message_array = []

        for i, p in enumerate(parts):
            if (item_len != len(p)):
                p_extra = item_len - int(len(p))
                p += "_"*p_extra
                parts[i] = p

        while count < item_len:
            message_array += [row[count] for row in parts]
            count += 1
        

        for letter in message_array:
            new_m += letter
        
        
    print(new_m)
    return new_m

# scytale_decipher("IMNNA_FTAOIGROE", 3)
# scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8)
# scytale_decipher("IRIANMOGFANEOT__", 4)