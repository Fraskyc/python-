def preloz_do_morseovky(text):
  morseovka = {
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "/": "-..-.--"
  }
  
  morseovka_text = ""
  for znak in text:
    if znak.upper() in morseovka:
      morseovka_text += morseovka[znak.upper()] + " "
    else:
      morseovka_text += " "

  return morseovka_text

text = input("Zadejte text, který chcete přeložit do morseovky: ")

morseovka_text = preloz_do_morseovky(text)
