import pytils
import human_readable_numbers_transform_into_digit as subj

for i in range(999999999999):
    a = pytils.numeral.in_words(i).split()
    b = subj.func(a)
    if i != b:
        print('число -', i, 'словесная запись -', a, 'вывод -', b)
    if i % 1000000 == 0:
        print(i)

print('done')
