def word_to_base26(word):
    word_b26 = [ord(ch)-97 for ch in word]
    return word_b26

def base26_to_word(word_b26):
    word = [chr(ch+97) for ch in word_b26]
    return ''.join(word)

def triple_letter(word):
    triple_indices = [i for i in range(len(word)-2) \
        if word[i] == word[i+1] - 1 and word[i+1] == word[i+2] - 1]
    return bool(triple_indices)

def letter_pairs(word):
    overlap = False
    last_letter = word[0]
    count = 0
    last_pair = 26
    for letter in word[1:]:
        if letter == last_letter and letter != last_pair:
            count += 1
            last_letter = 26
            last_pair = letter
        else:
            last_letter = letter
    return bool(count > 1)


#password = "cqjxjnds"
password = "cqjxxyzz"
new_password = ''
old_word = word_to_base26(password)

bad_list = word_to_base26("iol")

new_word = old_word[:]

while not new_password or not triple_letter(old_word) or not letter_pairs(old_word):
        l = len(old_word)
        k = l-1
        new_word[k] = (old_word[k] + 1) % 26
        if new_word[k] in bad_list:
            new_word[k] = (new_word[k] + 1) % 26
        while k >= 1:
            if new_word[k] < old_word[k]:
                new_word[k-1] = (old_word[k-1] + 1) % 26
                if new_word[k-1] in bad_list:
                    new_word[k-1] = (new_word[k-1] + 1) % 26
            else:
                break
            k -= 1
        old_word = new_word[:]
        new_password = base26_to_word(new_word)

print("Santa's next password is: ", new_password) 
                







