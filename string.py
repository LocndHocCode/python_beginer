name = "john"
age = 26

#noi chuoi
# print('Hello toi ten la ' + name + ' nam nay toi ' + str(age) + ' tuoi')

# Doi so theo vi tri
# print(' Toi ten la {name} va toi {age} tuoi'.format(name=name, age= age))

# f chuoi
# print(f'Toi ten la {name} va toi {age} tuoi')

s = 'hello world'
# chu thuong thanh hoa chu cai dau
print(s.capitalize())
# chu thuong thanh hoa toan bo chu cai
print(s.upper())    
# chu hoa thanh chu thuong
print(s.lower())
# lay du lieu do dai ky tu
print(len(s))
# tim kiem va thay the chuoi cu s.replace = ky tu cu , ky tu moi
print(s.replace('world', 'together'))
# dem so luong ky tu muon dem vd nhu l 
sub = 'l'
print(s.count(sub))
# tra ve gia tri true hay false chi lay ky tu dau la h va ky tu cuoi la d
print(s.startswith('h'))
print(s.endswith('d'))
# se lay chuoi va bien no thanh mang danh sach
print(s.split())
# find se tim ky tu trong mot chuoi 
print(s.find('r'))
