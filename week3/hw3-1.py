n = int(input())
for i in range(n):
    str = input()
    words = set(str)
    max_count = 0
    for word in words:
        count = 0
        for letter in str:
            if letter == word:
                count += 1
        if count > max_count:
            max_count = count
            max_ch = word
    print(max_ch)