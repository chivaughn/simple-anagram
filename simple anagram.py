def binS (dict,word):
    lo = 0
    hi = len(dict) - 1
    while (lo <= hi):
        mid = (lo + hi) // 2
        if dict[mid] == word:
            return True
        elif word < dict[mid]:
            hi = mid - 1
        elif word > dict[mid]:
            lo = mid + 1
    return False

def init_words(filename):
    words = {}
    count = 0
    with open(filename) as f:
        for line in f.readlines():
            word = line.strip()
            words[count] = word
            count = count + 1
    return words


def permute_string(str):
    if len(str) == 0:
        return ['']
    prev_list = permute_string(str[1:len(str)])
    next_list = []
    for i in range(0,len(prev_list)):
        for j in range(0,len(str)):
            new_str = prev_list[i][0:j]+str[0]+prev_list[i][j:len(str)-1]
            if new_str not in next_list:
                if new_str != word_to_anagram:
                    next_list.append(new_str)
    return next_list


def checker(an_words,dict,list_of_anagrams):
    flag = False
    flag = binS(dict,an_words)
    if flag == True:
        list_of_anagrams.append(an_words)
    return flag

count = 0
list_of_anagrams = []
dict = init_words('words.txt')
word_to_anagram = input("Please enter a word to see if there are any anagrams for it: ")
anagram_list = permute_string(word_to_anagram)
for an_words in anagram_list:
    flag = checker(an_words,dict,list_of_anagrams)
    if flag == True:
        count = count + 1

if count == 1:
    print(word_to_anagram," has ", count," anagram. It is as follows: ",list_of_anagrams)
elif count > 1:
    print(word_to_anagram," has ", count," anagrams. They are as follows: ",list_of_anagrams)
else:
    print(word_to_anagram," has no anagrams")
