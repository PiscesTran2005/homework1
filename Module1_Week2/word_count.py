file_path = 'Module1_Week2\Data.txt'
with open(file_path, 'r') as f:
    document = f.read()

words = document.split()

counter = {}
for word in words:
    if word in counter:
        counter[word] += 1
    else:
        counter[word] = 1
print(counter)