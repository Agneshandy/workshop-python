print (2 + 2)
print (50 - 5*6)
print ((50 - 5*6) / 4)
print (8 / 5)

print (17 / 3)
print (17 // 3)
print (17 % 3)
print (5 * 3 + 2)

print (5 ** 2)
print (2 ** 7)

width = 20
height = 5 * 9
print (width * height)

print (4 * 3.75 - 1)

tax = 12.5 / 100
price = 100.50
price * tax

price + _
round(_, 2)

print ('spam eggs')
print ('doesn\'t')
print ("doesn't")
print ('"Yes," they said.')
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')

'"Isn\'t," they said.'
print('"Isn\'t," they said.')
s = 'First line.\nSecond line.'     # \n means newline
s                                   # without print(), \n is included in the output
print(s)

print('C:\some\name')
print(r'C:\some\name')

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print (3 * 'un' + 'ium')

print ('Py' 'thon')

text = ('Put several strings within parentheses '
        'to have them joined together.')
print (text)

prefix = 'Py'
print (prefix + 'thon') #If you want to concatenate variables or a variable and a literal, use +

word = 'Python'
print (word[0])     # character in position 0
print (word[5])     # character in position 5

print (word[-1])    # last character
print (word[-2])    # second-last character
print (word[-6])

print (word[0:2])   # characters from position 0 (included) to 2 (excluded)
print (word[2:5])   # characters from position 2 (included) to 5 (excluded)

print (word[:2])    # character from the beginning to position 2 (excluded)
print (word[4:])    # characters from position 4 (included) to the end
print (word[-2:])   # characters from the second-last (included) to the end

print (word[:2] + word[2:])
print (word[:4] + word[4:])

print (word[42])    # the word only has 6 characters

#Namun, indeks irisan di luar jangkauan ditangani dengan anggun saat digunakan untuk mengiris
print (word[4:42])
print (word[42:])

#String python tidak dapat diubah. Oleh karena itu, menugaskan ke posisi terindeks dalam string menghasilkan kesalahan
#word[0] = 'J'
#word[2:] = 'py'

#Jika Anda memerlukan string yang berbeda, Anda harus membuat yang baru
print ('J' + word[1:])
print (word[:2] + 'py')

s = 'supercalifragilisticexpialidocious'
print (len(s))      #Fungsi bawaan len()mengembalikan panjang string

squares = [1, 4, 9, 16, 25]
print (squares)

print (squares[0])      # indexing returns the item
print (squares[-1])
print (squares[-3:])    # slicing returns a new list

#Semua operasi irisan mengembalikan daftar baru yang berisi elemen yang diminta. Ini berarti potongan berikut mengembalikan salinan daftar yang dangkal
print (squares[:])

#Daftar juga mendukung operasi seperti penggabungan
print (squares + [36, 49, 64, 81, 100])

cubes = [1, 8, 27, 65, 125]  # something's wrong here
print (4 ** 3)  # the cube of 4 is 64, not 65!
cubes[3] = 64  # replace the wrong value
print (cubes)

#Anda juga dapat menambahkan item baru di akhir daftar, dengan menggunakan append() metode (kita akan melihat lebih banyak tentang metode nanti)
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print (cubes)

#Penugasan ke irisan juga dimungkinkan, dan ini bahkan dapat mengubah ukuran daftar atau menghapusnya seluruhnya
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)
# replace some values
letters[2:5] = ['C', 'D', 'E']
print (letters)
# now remove them
letters[2:5] = []
print (letters)
# clear the list by replacing all the elements with an empty list
letters[:] = []
print (letters)

#Fungsi bawaan len()juga berlaku untuk daftar
letters = ['a', 'b', 'c', 'd']
print (len(letters))

#Dimungkinkan untuk menyusun daftar (membuat daftar yang berisi daftar lain)

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)
print (x[0])
print (x[0][1])

#Dapat menggunakan Python untuk tugas yang lebih rumit daripada menjumlahkan dua dan dua. Misalnya, kita dapat menulis sub-urutan awal dari deret Fibonacci sebagai berikut

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

i = 256*256
print('The value of i is', i)

#Fungsi print()menulis nilai argumen yang diberikan.
#Ini berbeda dari hanya menulis ekspresi yang ingin Anda tulis (seperti yang kita lakukan sebelumnya pada contoh kalkulator)
#dengan cara menangani banyak argumen, kuantitas floating point, dan string

#Argumen kata kunci akhir dapat digunakan untuk menghindari baris baru setelah keluaran, atau mengakhiri keluaran dengan string yang berbeda
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
