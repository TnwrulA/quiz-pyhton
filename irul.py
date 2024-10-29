
A = [2, 2, 1, 3, 5, 5, 5, 7, 2, 10]
A.sort() 
u = int(input("Masukkan nilai u yang ingin dicari: "))


def binary_search_first(A, u):
    left, right = 0, len(A) - 1  
    result = -1  
    while left <= right:  
        mid = (left + right) // 2  
        if A[mid] == u:
            result = mid  
            right = mid - 1  
        elif A[mid] < u:
            left = mid + 1  
        else:
            right = mid - 1  
    return result  

def binary_search_last(A, u):
    left, right = 0, len(A) - 1  
    result = -1  
    while left <= right: 
        mid = (left + right) // 2  
        if A[mid] == u:
            result = mid  
            left = mid + 1  
        elif A[mid] < u:
            left = mid + 1  
        else:
            right = mid - 1 
    return result  

first_index = binary_search_first(A, u)  
last_index = binary_search_last(A, u)  

if first_index == -1:  
    print(f"Elemen {u} tidak ditemukan dalam list A.")
else:
    count = last_index - first_index + 1  
    indices = list(range(first_index, last_index + 1))  
    print(f"Elemen {u} ditemukan sebanyak {count} kali pada indeks: {indices}")
