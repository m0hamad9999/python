from collections import Counter

with open('book2.txt', 'r+') as book:

    new_book = book.read().replace('Анна Павловна', 'Anna Pavlovna')


    words = new_book.replace('\n', ' ').split()

    book.seek(0)
    book.write(new_book)
    book.truncate()

count_words = len(words)
count_letters = sum(map(len, words))
average_length = count_letters / count_words

ten_longest_words = sorted(set(words), key=len, reverse=True)[:10]
ten_most_common_letters = Counter(''.join(words)).most_common(10)
count_paragraphs = sum(paragraph == '\n' for paragraph in new_book) + 1

print('in this book are ' ,count_words ,'words')
print('in this book are ', count_letters, ' letters')
print('the average length of wprds is : ', average_length)
print('ten longest words are :' , ten_longest_words)
print('the most common letters are :' , ten_most_common_letters)
print('in this book we have ',count_paragraphs, ' paragraphs')
