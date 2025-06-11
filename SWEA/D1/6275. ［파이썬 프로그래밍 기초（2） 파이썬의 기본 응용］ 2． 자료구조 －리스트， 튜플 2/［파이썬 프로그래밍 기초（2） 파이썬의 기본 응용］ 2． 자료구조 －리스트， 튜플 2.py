s = "Python is powerful... and fast; plays well with others; runs everywhere; is friendly & easy to learn; is Open."

print( "".join([ w for w in s if w not in list("aeiou")]))