def no_space(text):
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text

def reverse(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

def es_palindrome(text):
    text = no_space(text)
    reversed_text = reverse(text)
    return text.lower() == reversed_text.lower()

print("Abba", es_palindrome("Abba"))
print("Reconocer", es_palindrome("Reconocer"))
print("Amo la paloma", es_palindrome("Amo la paloma"))