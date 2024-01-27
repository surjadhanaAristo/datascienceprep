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
    
    return arr
def increasingSub(str):
    ind_1 = 0
    ind_2 = 0
    counter =  0
    prev = str[0]
    flag = False
    size = [0,0]
    for x in str:
        if(flag == False):
            ind_1 = counter - 1
        if (prev < x):
            ind_2 = counter + 1
            flag = True
        else:
            if (flag == True and ind_2 - ind_1 > size[1] - size[0]):
                size[0] = ind_1
                size[1] = ind_2
                ind_1 = 0
                ind_2 = 0
                flag = False
            else:
                ind_1 = 0
                ind_2 = 0
                flag = False

        prev = x
        counter += 1
    if (flag == True and ind_2 - ind_1 > size[1] - size[0]):
                size[0] = ind_1
                size[1] = ind_2
                ind_1 = 0
                ind_2 = 0
    return size
def commonSub(str1, str2):
    size = [0, 0]
    ind_1 = 0
    ind_2 = 0
    counter = 0
    flag = False
    for x in str2:
        try:
            if (str1.index(x) > 0):
                ind_2 = str1.index1(x)
                ind_1 = str1.index1(x)
                count2 = counter
                while (str2[counter] == str1[ind_2]):
                    counter += 1
                    ind_2 += 1
                counter = count2
                if(ind_2 - ind_1 > size[1] - size[0]):
                    size[0] = ind_1
                    size[1] = ind_2
                    ind_1 = 0
                    ind_2 = 0
            break
        except ValueError:
            ind = 0
        counter += 1




def main():
    #readJson('/Users/asurj/Documents/GitHub/datascienceprep/MOCK_DATA.json')
    arr = [3 ,5 ,9 , 2, 6, 4, 7, 2, 9, 1, 3, 6, 2, 8]
    arr = mergeSort(arr)
    str = "hellabcao"
    print(increasingSub(str))
    print(arr)


if __name__ == "__main__":
    main()