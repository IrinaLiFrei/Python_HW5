# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc


def encode_text(string):
    encoded_string = ''
    i = 0
    while (i <= len(string)-1):
        count = 1
        char = string[i]
        j = i
        while (j < len(string) - 1): 
            if (string[j] == string[j + 1]): 
                count = count + 1
                j = j + 1
            else: 
                break
        encoded_string = encoded_string + str(count) + char
        i = j + 1
    return encoded_string


def decode_text(my_string):
    decoded_string = ""
    i = 0
    j = 0
    while (i <= len(my_string) - 1):
        run_count = int(my_string[i])
        run_word = my_string[i + 1]
        for j in range(run_count):
            decoded_string = decoded_string+run_word
            j = j + 1
        i = i + 2
    return decoded_string


my_string = open('python.txt', 'r')
my_string = str(my_string.readlines())
my_string = my_string.replace("['", '')
my_string = my_string.replace("']", '')

string_to_encode = encode_text(my_string)
string_to_decode = decode_text(string_to_encode)
print(f'Original string: {my_string}')
print(f'Encoded string: {string_to_encode}')
print(f'Decoded string: {string_to_decode}')

data = open('python2.txt', 'w')
my_data = string_to_decode
data.writelines(my_data)
