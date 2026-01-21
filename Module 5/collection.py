import collections

# print(collections.__doc__)
print(dir(collections))
fruits = ['apple','banana','apple','orange']

print(collections.Counter(fruits))
print(collections.Counter(fruits).most_common(3))

word_dict = collections.defaultdict(list)
word_dict['python'].append('programming')
print(word_dict)

