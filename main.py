import json

def readJson(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    print(data)
def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
 
        # Dividing the array elements
        L = arr[:mid]
 
        # Into 2 halves
        R = arr[mid:]
 
        # Sorting the first half
        mergeSort(L)
 
        # Sorting the second half
        mergeSort(R)
 
        i = j = k = 0
 
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
 
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
 
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1



def main():
    #readJson('/Users/asurj/Documents/GitHub/datascienceprep/MOCK_DATA.json')
    arr = [3 ,5 ,9 , 2, 6, 4, 7, 2, 9, 1, 3, 6, 2, 8]
    arr = mergeSort(arr)
    print(arr)


if __name__ == "__main__":
    main()