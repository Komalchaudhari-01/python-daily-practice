
line = input('Enter your sentence')
word = input('Enter your word to remove')
if word in line:
    line = line.replace(word,'')
print(line)