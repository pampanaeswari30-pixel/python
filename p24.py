def stringMatching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j:
                if words[i] in words[j]:
                    result.append(words[i])
                    break
    return result
words = ["mass","as","hero","superhero","asper"]
print(stringMatching(words))           