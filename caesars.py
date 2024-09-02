"""
  Program that performs Caesar's Cipher, both encryption and decryption
  User is prompted to enter the shift number K
  User chooses between encrypt or decrypt mode
  User inputs the message
  The program outputs a valid ciphertext or plaintext depending on the selected operation mode
"""

import time

#Function to turn characters into numbers
def character_to_number(character):
  if character.isalpha():
    return ord(character.lower()) - ord('a')
  return False

def caesar_cipher(text, shift, mode):
  result = []
  for char in text:
    if char.isalpha():
      num = character_to_number(char)
      if mode == "encrypt":
        shifted_num = (num + shift) % 26
      elif mode == "decrypt":
        shifted_num = (num - shift) % 26
      
      if char.islower():
        result.append(chr(shifted_num + ord('a')))
      else:
        result.append(chr(shifted_num + ord('A')))
    else:
      result.append(char) # Non-alphabet characters are added unchanged
  return ''.join(result) 

def main():
    while True:
        st = time.time()
        key = input("Enter the key (0-26): ")
        if key.isdigit():
            shift = int(key)
            if 0 <= shift <= 26:
                break
            else:
                print("The key must be a number between 0 and 26.")
        else:
            print("Invalid input. Please enter a number between 0 and 26.")
    
    while True:
        mode = input("Do you want to 'encrypt' or 'decrypt'?: ").lower()
        if mode in ["encrypt", "decrypt"]:
            break
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    
    input_text = input("Enter your message: ")
    result_text = caesar_cipher(input_text, shift, mode)

    et = time.time()
    elapsed_time = et - st

    print(f"Result: {result_text}")
    print(f"Operation time: {elapsed_time} seconds")
  
if __name__ == "__main__":
  main()