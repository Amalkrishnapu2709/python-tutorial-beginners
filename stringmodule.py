def count_vowels(text):
    vowels="aeiouAEIOU"
    count=0
    for i in text:
        if i in vowels:
            count+=1
    if count==0:
        print("no vowels")
    else:
        print("vowels count:",count)
        
    
def count_consonants(text):
    vowels="aeiouAEIOU"
    count=0
    for i in text:
        if i not in vowels:
            count+=1
    if count==0:
        print("no cosonants")
    else:
        print("consonants count:",count)

def length_string(text):
    return len(text)

def palindrome(text):
    if text==text[::-1]:
        print(text,"is a palindrome")
    else:
        print(text,"is not a palindrome")

def word_count(text):
    #split() takes the words in a list
    
    return len(text.split())

def char_count(text):
    #replace is used to remove white spaces
    
    return len(text.replace(" ",""))

def check_substring(text,substr):
    return substr in text



def reverse_string(text):
    return text[::-1]

def replace_word(text,a,b):
    return text.replace(a,b)

def title_case(text):
    return text.title()

def remove_digits(text):
    result = ""
    for char in text:
        if char.isalpha():
            result += char
    return result

def remove_punctuation(text):
    result=""
    for char in text:
        if char.isalnum() or char==" ":
            result+=char
    return result
    


