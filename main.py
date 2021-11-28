logo = '''
                                                                                 
                                                                                 
 ,adPPYba,    ,adPPYYba,     ,adPPYba,    ,adPPYba,    ,adPPYYba,    8b,dPPYba,  
a8"     ""    ""     `Y8    a8P_____88    I8[    ""    ""     `Y8    88P'   "Y8  
8b            ,adPPPPP88    8PP"""""""     `"Y8ba,     ,adPPPPP88    88          
"8a,   ,aa    88,    ,88    "8b,   ,aa    aa    ]8I    88,    ,88    88          
 `"Ybbd8"'    `"8bbdP"Y8     `"Ybbd8"'    `"YbbdP"'    `"8bbdP"Y8    88          
                                                                                 
                                                                                 

                                                                            
              88                   88                                       
              ""                   88                                       
                                   88                                       
 ,adPPYba,    88    8b,dPPYba,     88,dPPYba,      ,adPPYba,    8b,dPPYba,  
a8"     ""    88    88P'    "8a    88P'    "8a    a8P_____88    88P'   "Y8  
8b            88    88       d8    88       88    8PP"""""""    88          
"8a,   ,aa    88    88b,   ,a8"    88       88    "8b,   ,aa    88          
 `"Ybbd8"'    88    88`YbbdP"'     88       88     `"Ybbd8"'    88          
                    88                                                      
                    88                                                      

'''

def greet(name, location, time):
  print(f"Hi {name} from {location}. Good {time}.")
  print(f"Hey {name} from {location}. Good {time}.")
  print(f"Hello {name} from {location}. Good {time}.")

#greet("Angela", location="London", time="evening")

def caeser(direction, text, shift):
  caeser_text =""
  shift = shift % 26
  if direction == "encode":
    shift = 26 - shift
  
  for letter in text:
    if letter in alphabet:
      caeser_text += alphabet[alphabet.index(letter)-shift]
    else:
      caeser_text += letter

  print(caeser_text)


def encrypt(text, shift):
  encrypt_text =""
  for letter in text:
    encrypt_text += alphabet[alphabet.index(letter)+shift-26]
  print(encrypt_text)


def decrypt(text, shift):
  decrypt_text =""
  for letter in text:
    decrypt_text += alphabet[alphabet.index(letter)-shift]
  print(decrypt_text)

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

run = "y"

while run == "y":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caeser(direction, text, shift)
  run = input('Type "y" to continue. Type any other key to end.\n').lower()
print("Goodbye from Caeser")