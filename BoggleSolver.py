import sys

board = []
dictionary = set()
with open(sys.argv[1]) as f:
    for line in f:
        board.append([char for char in line.rstrip()])
dictionary = set(line.strip() for line in open(sys.argv[2]))
word_list = []


# check if a word is in the dictionary
def is_word(word, dictionary):
    return word in dictionary


def find_word(board, visited, i, j, string, dictionary):
    word = string + board[i][j]
    if is_word(word, dictionary) and len(word) >= 3:
        word_list.append(word)

    for offset in range(-1, 2):
        for offset2 in range(-1, 2):
            next_i = i + offset
            next_j = j + offset2
            if 4 > next_i > -1 and 4 > next_j > -1 and visited[next_i][next_j] is False:
                visited[next_i][next_j] = True
                find_word(board, visited, next_i, next_j, word, dictionary)
    visited[i][j] = False


visited = [[False, False, False, False], [False, False, False, False], [False, False, False, False],
           [False, False, False, False]]
for i in range(4):
    for j in range(4):
        string = ""
        visited[i][j] = True
        find_word(board, visited, i, j, string, dictionary)
words = []
[words.append(x) for x in word_list if x not in words]
sorted_words = sorted(words)
sorted_by_length = sorted(sorted_words, key=len)
print('\n'.join(map(str, sorted_by_length)))
print("Total Number of words formed:", len(words))
