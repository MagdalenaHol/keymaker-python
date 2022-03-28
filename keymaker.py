import string 

def shift_characters(word, shift):
    alphabet = string.ascii_lowercase
    new = ""

    for letter in word:
        if letter in alphabet:
            new_position = alphabet.index(letter) + shift
            if new_position >= len(alphabet):
                new_position %= len(alphabet)
            new = new + alphabet[new_position]
    print(new)
    return new
        

# def pad_up_to(word, shift, n):
#     alphabet = string.ascii_lowercase
#     new = ""
#     cos_ = ""
#     cos = [] 
#     is_running = True
#     while is_running:
#         cos.append(word)
#         for letter in word:
#             if letter in alphabet:
#                 new_position = alphabet.index(letter) + shift
#                 new = new + alphabet[new_position]
#                 if new_position >= len(alphabet):
#                     new_position %= len(alphabet)
#                 if len(new) == len(word):
#                     cos.append(new)
#         for letter in new:
#             if letter in alphabet:
#                 new_position = alphabet.index(letter) + shift
#                 cos_ = cos_ + alphabet[new_position]
#                 if new_position >= len(alphabet):
#                     new_position %= len(alphabet)
#                 if len(cos_) == len(word):
#                     cos.append(cos_)
#         word = "".join(cos)
#         if len(word) == n:
#             print(word)
#         else:
#             print(word[:n])
#         print
#         return word[:n]


def pad_up_to(word, shift, n):
    alphabet = string.ascii_lowercase
    word_to_shift = word
    list_ = []

    for letter in word:
        list_.append(letter)
    while len(list_) <= n:
        new_word_to_shift_2 = ""
        for letter in word_to_shift:
            shifted_l = alphabet[string.ascii_lowercase.index(letter) + shift]
            list_.append(shifted_l)
            new_word_to_shift_2 += shifted_l
            print(new_word_to_shift_2)
        # if new_word_to_shift_2 >= len(alphabet):
        #     new_word_to_shift_2 %= len(alphabet)
        # print(new_word_to_shift_2)
        word_to_shift = new_word_to_shift_2
    print("".join(list_[:n]))
    return "".join(list_[:n])




def abc_mirror(word):
    alphabet = string.ascii_lowercase
    reversed_alph = alphabet[::-1]
    dict_of_letters = dict(zip(alphabet, reversed_alph))
    mirror = ""

    for letter in word:
        mirror = mirror + dict_of_letters[letter]
    print(mirror)
    return mirror
    

# def create_matrix(word1, word2):
#     alphabet = string.ascii_lowercase
#     # string.ascii_lowercase.index("p")  

#     print(string.ascii_lowercase.index("m") + string.ascii_lowercase.index("p") - 26)

#     for i in word1:
#         for i in word2:
#             alphabet.index(word1[i]) + alphabet.index(word2[i])
#             print(i)





    

def zig_zag_concatenate(matrix):
    chars = []

    for i in range(len(matrix[0])):
        for j in range(len(matrix)) if i % 2 == 0 else reversed(range(len(matrix))):
            chars.append(matrix[j][i])
    print(''.join(chars))
    return ''.join(chars)



def rotate_right(word, n):
    after_rotate = []
    the_rest = []

    for x in range(len(word)):
        word_ = word[::-1]
        elements = list(word_)
    after_rotate.append(elements[:n][::-1])
    the_rest.append(elements[n:][::-1])
    merge = after_rotate[0] + the_rest[0]
    return "".join(merge)


def get_square_index_chars(word):
    value_squared_position = []

    for i in range(len(word)):
        if i**0.5 == int(i**0.5):
            value_squared_position.append(word[i])
        #     print(f' {i, word[i]} is a pefect square')
        # else:
        #     print(f'{i, word[i]} is not a pefect square') 
    print("".join(value_squared_position))
    return "".join(value_squared_position)   


def remove_odd_blocks(word, block_length):
    block_list = []

    for i in range(0,len(word), block_length):
        block_list.append(word[:block_length])
        word = word[block_length:]
    
    print("".join(block_list[::2]))
    return "".join(block_list[::2])


def reduce_to_fixed(word, n):
    get_n_char = []
    word = word[:n]
    get_n_char.insert(1, word[2:])
    get_n_char.insert(2, word[0:2])
      
    print("".join(get_n_char)[::-1])
    return "".join(get_n_char)[::-1]


# def hash_it(word):
#     """
#     >>> hash_it('morpheus')
#     'trowdo'
#     """
#     padded = pad_up_to(word, 15, 19)
#     elongated = zig_zag_concatenate(create_matrix(padded, abc_mirror(padded)))
#     rotated = rotate_right(elongated, 3000003)
#     cherry_picked = get_square_index_chars(rotated)
#     halved = remove_odd_blocks(cherry_picked, 3)
#     key = reduce_to_fixed(halved, 6)
#     return key


# if __name__ == '__main__':
#     name = input("Enter your name! ").lower()
#     print(f'Your key: {hash_it(name)}')


# shift_characters("abz", 4)
# pad_up_to('abb', 5, 11)
# abc_mirror("alma")
# create_matrix("lol", "zol")
# zig_zag_concatenate(['abc', 'def', 'ghi', 'jkl'])
# rotate_right("abcdef", 4)
# get_square_index_chars("abcdefghijklmnopqrstuwvxyzabcdefghijk")
# remove_odd_blocks('abcdefghijklm', 3)
# reduce_to_fixed('abcdefghijklm', 6)
create_matrix('mamas', 'papas')
