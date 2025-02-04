english_alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
morse_alphabet = [ ".-","-...","-.-.","-..",".","..-.","--.","....","..", ".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--..", ","]#comma is space 

def morse_to_english():
# asking for what to translate (morse)
    english_translation = []
    morse = input("Enter the Morse code you want to translate (use commas as space): ").strip()
    
# convert commas to spaces
    morse = morse.replace(",", " ") 
    morse_words = morse.split("   ")
#translating
    for word in morse_words:
        letters = word.split(" ")  
        word_translation = ""
        for code in letters:
            if code in morse_alphabet:
                word_translation += english_alphabet[morse_alphabet.index(code)]
        english_translation.append(word_translation)  

#printing results 
    print("English Text:", " ".join(english_translation))

    

#similar to morse to english 
def english_to_morse():
# asking for what to translate (english) 
    morse_translation = []
    english = input("Enter the English text you want to translate: ").upper()

# actual translations 
    for char in english:
        if char in english_alphabet:
            morse_translation.append(morse_alphabet[english_alphabet.index(char)])
#printing results 
    print("Morse Text:", ' '.join(morse_translation))   

#selector function
def main():
    while True:
        print("Morse Code Translators")
        print("1. Morse code to English translator")
        print("2. English to Morse code translator")
        print("3. Exit")
        choice = int(input("What would you like to use? "))
        if choice == 1: 
            morse_to_english()
        elif choice == 2: 
            english_to_morse()
        elif choice == 3: 
            break 


if __name__ == "__main__":
    main()
