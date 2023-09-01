def es_palindrome(text):
    reversed_text = text[::-1]
    formatted_text = reversed_text.replace(" ", "").lower()

    if(text.lower() == formatted_text):
        return True
    
    return False

print("Abba", es_palindrome("Abba"))
print("Reconocer", es_palindrome("Reconocer"))
print("Amo la paloma", es_palindrome("Amo la paloma"))