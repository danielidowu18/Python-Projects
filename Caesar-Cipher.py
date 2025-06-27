alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount *= -1
  for char in start_text:
    if char in alphabet:
        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
    else:
        end_text += char    
    
  print(f"Here's the {cipher_direction}d result: {end_text}")

logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""
print(logo)

userAnswer = "yes"
while userAnswer == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    userAnswer = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if userAnswer == "no":
        print("Goodbye.")
        

# OR 
# logo = """           
#  ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
# a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
# 8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
# "8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
#  `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
#             88             88                                 
#            ""             88                                 
#                           88                                 
#  ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
# a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
# 8b         88 88       d8 88       88 8PP""""""" 88          
# "8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
#  `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
#               88                                             
#               88           
# """
# print(logo)
# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
# text = input("Type your message: ").lower()
# shift = int(input("Type the shift number: "))

# def crypt(textParam, shiftParam, directionParam):
#     if directionParam == "encode":
#         cipher_text = ""
#         for letter in textParam:
#             location = alphabet.index(letter, 0)
#             new_location = location + shiftParam
#             listIndex = len(alphabet) - 1
#             if new_location > listIndex:
#                 new_location -= listIndex + 1
#             cipher_text += alphabet[new_location]
#         print(f"The encoded text is {cipher_text}")
#     elif directionParam == "decode":    
#         decipher_text = ""
#         for letter in textParam:
#             location = alphabet.index(letter, 0)
#             new_location = location - shiftParam
#             decipher_text += alphabet[new_location]
#         print(f"The decoded text is {decipher_text}")
#     else:
#         print("Choose between encode or decode.")

#     shift = shift % 26
        
# crypt(textParam=text, shiftParam=shift, directionParam=direction)                 
