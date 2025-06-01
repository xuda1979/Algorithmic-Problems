from typing import List

def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0
    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - j + 1
    return -1


def main() -> None:
    text = "abxabcabcaby"
    pattern = "abcaby"
    index = kmp_search(text, pattern)
    print(f'Text: {text}')
    print(f'Pattern: {pattern}')
    print(f'Pattern found at index: {index}')


if __name__ == "__main__":
    main()
