# solution of exercise of day 39
import random
import string

print("type encode to create your sentence, decode to decode a message, or quit to exit")
usr0 = input("enter your choice: ").strip().lower()

if usr0 == "quit":
    print("goodbye user 0")
    quit()

if usr0 not in {"encode", "decode"}:
    print("Invalid choice. Please run the program again and type encode, decode, or quit.")
    quit()

sent = input("enter your message: ").strip()
words = sent.split()


def random_letter_generator(length=3):
    return "".join(random.choices(string.ascii_letters, k=length))


def encode_secret_language(words):
    nwords = []
    for word in words:
        if len(word) >= 3:
            rstr = random_letter_generator()
            encoded = rstr + word[1:] + word[0] + rstr
            nwords.append(encoded)
        else:
            nwords.append(word[::-1])
    return " ".join(nwords)


def decode_secret_language(words):
    nwords = []
    for word in words:
        if len(word) <= 2:
            nwords.append(word[::-1])
        elif len(word) >= 7:
            core = word[3:-3]
            if core:
                decoded = core[-1] + core[:-1]
                nwords.append(decoded)
            else:
                nwords.append(word)
        else:
            nwords.append(word)
    return " ".join(nwords)

if usr0 == "encode":
    result = encode_secret_language(words)
    print("Encoded message:", result)
else:
    result = decode_secret_language(words)
    print("Decoded message:", result)
