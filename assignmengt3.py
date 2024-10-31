#Create a function is_palindrome(word) that returns True if a given word is a palindrome (reads the same backward) and False otherwise.

def is_palindrome(word):
    # Normalize the word by converting it to lowercase
    normalized_word = word.lower()
    # Check if the normalized word is equal to its reverse
    return normalized_word == normalized_word[::-1]
print(is_palindrome("Radar"))