import re


def extract_and_sort_numbers(message_file):
    numbers = []

    # Open the file in read mode
    with open(message_file, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if word.isdigit():
                    numbers.append(int(word))

    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize an empty string to store the pyramid structure
    pyramid = ''

    # Initialize a variable to keep track of the index of numbers list
    index = 0

    # Loop to construct the pyramid structure
    for i in range(1, len(numbers) + 1):
        pyramid += ' '.join(map(str, numbers[index:index + i])) + '\n'
        index += i

    return pyramid


def decode_number(array):
    # Find all numbers at the end of each line
    last_numbers = re.findall(r'\d+$', array, re.MULTILINE)

    return last_numbers


def decode_message(codedNumbers):
    message = ""
    with open('coding_qual_input.txt', 'r') as file:
        number_word_pairs = {}

        # Iterate over each line in the file
        for line in file:
            number, word = line.strip().split(' ')
            number_word_pairs[int(number)] = word

        # print(number_word_pairs)
    numbers_array = [int(num_str) for num_str in codedNumbers]
    # print("Dictionary Keys:", list(number_word_pairs.keys()))

    # Iterate over each number in the array
    for number in numbers_array:
        if number in number_word_pairs:
            word = number_word_pairs[number]
            message += ' ' + word
            # print(f"{number}: {word}")
        else:
            # If the number does not exist in the dictionary, print a message
            print(f"{number}: Not found")

    print(message)


# Example usage:
pyramid = extract_and_sort_numbers('coding_qual_input.txt')
codedMessage = decode_number(pyramid)
# print(codedNumbers)
decode_message(codedMessage)
