"""
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
"""


def func(k, s):
    types = []
    for letter in s:
        for com in types:
            if com['status']:
                if len(com['letters']) == k:
                    if letter in com['letters']:
                        com['string'].append(letter)
                    else:
                        com['status'] = False
                else:
                    if letter not in com['letters']:
                        com['letters'].append(letter)
                    com['string'].append(letter)

        types.append({
            "letters": [letter],
            "string": [letter],
            "status": True
        })
    return max(["".join(ty['string']) for ty in types], key=len)


if __name__ == "__main__":
    ans = func(2, "abcba")
    if ans == "bcb":
        print("Success")
    else:
        print(ans)
