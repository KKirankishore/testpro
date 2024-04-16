import random
import string

def generate_captcha(length=6):
    # Define characters to use in captcha
    characters = string.ascii_letters + string.digits
    
    # Generate random captcha string
    captcha = ''.join(random.choice(characters) for _ in range(length))
    
    return captcha

if __name__ == "__main__":
    captcha_text = generate_captcha()
    print("Generated CAPTCHA:", captcha_text)
