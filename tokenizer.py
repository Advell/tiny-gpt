text = "hello world"

# Each unique character gets its own integer ID.
characters = sorted(set(text))
vocab_size = len(characters)

char_to_id = {char: i for i, char in enumerate(characters)}
id_to_char = {i: char for i, char in enumerate(characters)}

def encode(text):
    token_ids = []
    for char in text:
        token_ids.append(char_to_id[char])
    return token_ids
   
def decode(token_ids):
    decoded_string = ""
    for token_id in token_ids:
        decoded_string += id_to_char[token_id]
    return decoded_string

if __name__ == "__main__":
    print("\nCharacters:", characters)
    print("Vocabulary size:", vocab_size)
    print("Character -> ID:", char_to_id)
    print("ID -> Character:", id_to_char)
    
    encoded_string = encode("hello")    
    decoded_string = decode(encoded_string)
   
    print("\nEncoded hello:", encoded_string)
    print("Decoded IDs:", decoded_string)
