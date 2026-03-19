# Tao danh sach mang
numbers = [1,2,3,4,5]
key = ['apple', 'android', 'samsung']
# tao mot list 
# numbers2 = list((1,2,3,4,5))

# Lay gia tri don le
print(key[1])
# Lay do dai mot mang danh sach
print(len(key))
# Them vao chuoi mang
key.append('vivo')
# Xoa chuoi trong mang
key.remove('samsung')
# Them vao vi tri mong muon
key.insert(2,'realme')
#Thay doi gia tri
key[0] = 'nano'
# Xoa chuoi o vi tri mong muon
key.pop(1)
# Dao nguoc danh sach
key.reverse()
# Sap xep mang theo bang chu cai
key.sort()
# Sap xep nguoc chu cai
key.sort(reverse = True) 

print(key)