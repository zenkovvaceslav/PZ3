class CipherValidator:
    """дескриптор для параметров шифрования"""
    def __set_name__(self, owner, name):
        self.name = '_' + name
    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return getattr(obj, self.name, None)
    
    def __set__(self, obj, value):
        if not isinstance(value, int):
            raise TypeError(f"{self.name[1:]} должен быть целым числом")
        setattr(obj, self.name, value)


class CaesarCipher:
    """Шифр цезарь"""
    shift = CipherValidator()
    
    def __init__(self, shift=3):
        self.shift = shift
    
    def encrypt(self, text):
        """Шифрование текста"""
        result = []
        for char in text:
            if char.isalpha():
                if 'А' <= char <= 'Я':
                    base = ord('А')
                    alphabet_size = 32
                elif 'а' <= char <= 'я':
                    base = ord('а')
                    alphabet_size = 32
                elif 'A' <= char <= 'Z':
                    base = ord('A')
                    alphabet_size = 26
                elif 'a' <= char <= 'z':
                    base = ord('a')
                    alphabet_size = 26
                else:
                    if char == 'Ё':
                        base = ord('А')
                        char_code = 6
                        new_code = (char_code + self.shift) % 32
                        result.append(chr(base + new_code))
                        continue
                    elif char == 'ё':
                        base = ord('а')
                        char_code = 6
                        new_code = (char_code + self.shift) % 32
                        result.append(chr(base + new_code))
                        continue
                    result.append(char)
                    continue
                
                char_code = ord(char) - base
                new_code = (char_code + self.shift) % alphabet_size
                result.append(chr(base + new_code))
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text):
        """Дешифрование текста"""
        original_shift = self.shift
        self.shift = -self.shift
        decrypted = self.encrypt(text)
        self.shift = original_shift
        return decrypted


class AtbashCipher:
    """Щифр атбаш"""
    
    def __init__(self):
        self.rus_alphabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        self.rus_alphabet_lower = self.rus_alphabet.lower()
        
        self.eng_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.eng_alphabet_lower = self.eng_alphabet.lower()
        
        self.rus_cipher_map = {}
        self.eng_cipher_map = {}
        
        for i in range(len(self.rus_alphabet)):
            self.rus_cipher_map[self.rus_alphabet[i]] = self.rus_alphabet[-(i+1)]
            self.rus_cipher_map[self.rus_alphabet_lower[i]] = self.rus_alphabet_lower[-(i+1)]
        
        for i in range(len(self.eng_alphabet)):
            self.eng_cipher_map[self.eng_alphabet[i]] = self.eng_alphabet[-(i+1)]
            self.eng_cipher_map[self.eng_alphabet_lower[i]] = self.eng_alphabet_lower[-(i+1)]
    
    def encrypt(self, text):
        """Шифрование текста"""
        result = []
        for char in text:
            if char in self.rus_cipher_map:
                result.append(self.rus_cipher_map[char])
            elif char in self.eng_cipher_map:
                result.append(self.eng_cipher_map[char])
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, text):
        """Дешифрование текста"""
        return self.encrypt(text)



if __name__ == "__main__":
    user_text = input("\nшифруемый текст ")
    
    while True:
        try:
            shift_input = input("Сдвиг(для цезарь)")
            caesar_shift = int(shift_input)
            break
        except ValueError:
            print("должно быть целое число")
    
    caesar_cipher = CaesarCipher(caesar_shift)
    atbash_cipher = AtbashCipher()

    caesar_encrypted = caesar_cipher.encrypt(user_text)
    caesar_decrypted = caesar_cipher.decrypt(caesar_encrypted)
    
    print(f"\n1. шифр цезарь (сдвиг = {caesar_shift}):")
    print(f"   исходный текст:    {user_text}")
    print(f"   зашифрованный:     {caesar_encrypted}")
    print(f"   расшифрованный:    {caesar_decrypted}")
    
    atbash_encrypted = atbash_cipher.encrypt(user_text)
    atbash_decrypted = atbash_cipher.decrypt(atbash_encrypted)
    
    print(f"\n2. шифр атбаш:")
    print(f"   исходный текст:    {user_text}")
    print(f"   зашифрованный:     {atbash_encrypted}")
    print(f"   расшифрованный:    {atbash_decrypted}")