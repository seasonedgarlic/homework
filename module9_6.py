def all_variants(text):
    if not text:
        return
    for i in range(len(text)):
        for j in all_variants(text[i + 1:]):
            yield text[:i] + j
        yield text[:i + 1]

a = all_variants("abc")
for i in a:
    print(i)