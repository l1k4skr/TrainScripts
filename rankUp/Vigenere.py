class VigenereCipher():
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
    
    def get_code(self, text):
        coded = ""
        index = 0
        for i in range(len(text)):
            if text[i] in self.alphabet:
                coded += self.key[index]
            else:
                coded += text[i]
            if index >= len(self.key)-1:
                index = 0
            else:
                index += 1
        return coded
    def generate_list(self, index_):
        return self.alphabet[index_:] + self.alphabet[:index_]
    
    def found_letter(self, lettertext, lettercode):
        lstalp = list(self.alphabet)
        xtext_ent = lstalp.index(lettertext)
        ycode_int = lstalp.index(lettercode)
        lstalp = self.generate_list(xtext_ent)
        return lstalp[ycode_int]
    
    def found_letter_decode(self, lettertext, lettercode):
        lstalp = list(self.alphabet)
        xtext_ent = lstalp.index(lettertext)
        lstalp = self.generate_list(xtext_ent)
        ycode_int = lstalp.index(lettercode)
        return self.alphabet[ycode_int]
    
    def encode(self, text):
        code = self.get_code(text)
        encoded = ""
        for n, i in enumerate(code):
            if i in self.alphabet:
                encoded += self.found_letter(text[n], i)
            else:
                encoded += i
        return encoded 
    def decode(self, text):
        code = self.get_code(text)
        decoded = ""
        for n, i in enumerate(code):
            if i in self.alphabet:
                decoded += self.found_letter_decode(i, text[n])
            else:
                decoded += i
        return decoded

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
ciph = VigenereCipher(key, abc)
print(ciph.encode("it's a shift cipher!")) 
print(ciph.decode("xt'k o vwixl qzswej!")) 
# ovkpfsirmqcs diuuqpvoe
# ovkpfsirmqcs diuuqpvoe