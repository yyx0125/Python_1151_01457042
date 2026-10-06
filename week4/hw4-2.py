mirror = {
    'A':'A', 'E':'3', 'H':'H', 'I':'I',
    'J':'L', 'L':'J', 'M':'M', 'O':'O',
    'S':'2', 'T':'T', 'U':'U', 'V':'V',
    'W':'W', 'X':'X', 'Y':'Y', 'Z':'5',
    '1':'1', '2':'S', '3':'E', '5':'Z', '8':'8'
}

while True:
    try:
        str = input().strip()
    except EOFError:
        break

    isPalindrome = False
    isMirror = True

    reverse = str[::-1]

    if str == reverse:
        isPalindrome = True

    for i in range(len(str)):
        if mirror.get(str[i]) != reverse[i]:
            isMirror = False
            break

    if isPalindrome and isMirror:
        print(f"{str} -- is a mirrored palindrome.")
    elif isPalindrome:
        print(f"{str} -- is a regular palindrome.")
    elif isMirror:
        print(f"{str} -- is a mirrored string.")
    else:
        print(f"{str} -- is not a palindrome.")

    print()