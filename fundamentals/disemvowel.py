def permutations(s):
    if len(s) == 1:
        return [s]
    else:
        perms = []
        for i in range(len(s)):
            print(i)
            perms += [s[i] + p for p in permutations(s[:i] + s[i+1:])]
        return perms
    
    
print(permutations('abcsxdrfcgvhj'))