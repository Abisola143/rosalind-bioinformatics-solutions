from collections import Counter
with open(r"C:\Users\Akinyemi\Downloads\rosalind_dna (2).txt", "r") as file:
    a = file.readline()
print(a)
b = a.count("A")
c = a.count("C")
d = a.count("G")
e = a.count("T")
cnt = Counter(a)
print(cnt['A'], cnt['C'], cnt['G'], cnt['T'])
print(b,c,d,e)