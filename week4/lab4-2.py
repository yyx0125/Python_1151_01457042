str = input().lower().split()
dict = dict.fromkeys(str, 0)

for voca in list(dict):
    for word in str:
        if(word == voca):
            dict[voca] += 1

for k, v in dict.items():
    print(f"{k} {v}")