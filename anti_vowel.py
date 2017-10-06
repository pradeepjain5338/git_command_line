def anti_vowel(text):
    vowel=['a','e','i','o','u']
    for a in text:
        for b in vowel:
            if a==b:
                text=text.replace(a,"")
    return text


print (anti_vowel("pradeep"))
