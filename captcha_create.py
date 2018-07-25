# creating word and captcha image
from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha
from PIL import Image
import random
import string

# font types for testing
font_types = ['ALGER', 'ANTQUAI', 'ITCBLKAD', 'BRADHITC']


def gen_random_word(wordLen=6):
        allowedChars = string.ascii_letters+string.digits
        word = ""
        for i in range(0, wordLen):
                word = word + allowedChars[random.randint(0,0xffffff) % len(allowedChars)]
        return word

# opening text file with list of words or generating word

#words = open('words.txt').readlines()
#word = words[random.randint(0,len(words)-1)]

image = ImageCaptcha(width=300, height=100, fonts=[font_types[random.randint(0,0xffffff) % len(font_types)],font_types[random.randint(0,0xffffff) % len(font_types)]], font_sizes=(60, 75))
word = gen_random_word()
print(word)
data = image.generate(word)
image.write(word, 'out.png')

original = Image.open('out.png')
original.show()
