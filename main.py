import json

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

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
    indices = []
    ind_1 = 0
    ind_2 = 0
    counter = 0
    flag = False
    for x in str2:
        #print(x)
        try:
            if (str1.index(x) > 0):
                ind_2 = str1.index(x)
                ind_1 = str1.index(x)
                count2 = counter
                while (str2[counter] == str1[ind_2]):
                    #print(str1[ind_2])
                    counter += 1
                    ind_2 += 1
                    if (counter >= len(str2) or ind_2 >= len(str1)):
                        break
                counter = count2
                if(ind_2 - ind_1 > size[1] - size[0]):
                    #print("hi")
                    size[0] = ind_1
                    size[1] = ind_2
                    ind_1 = 0
                    ind_2 = 0
            
        except ValueError:
            ind = 0
        counter += 1
    return size
def printInOrder(root):
    if(root):
        printInOrder(root.left)
        print(root.val)
        printInOrder(root.right)
    return
def printInPreorder(root):
    if(root):
        print(root.val)
        printInPreorder(root.left)
        printInPreorder(root.right)
    return
def printInPostorder(root):
    if(root):
        
        printInPostorder(root.left)
        printInPostorder(root.right)
        print(root.val)
    return
def contSubarrays(arr, k):
    ind_1 = 0
    ind_2 = 0
    size = 0
    counter = 0
    index = 0
    for x in arr:
        counter = counter + x
        #print(counter)
        if (counter == k):
                counter = 0
                size += 1
                ind_2 = index
                ind_1 = index
        elif (counter > k):
            counter = 0
            ind_1 = index
            ind_2 = index
        index += 1
        ind_2 += 1
    return size
def medianTwoArr(num1, num2):
    c1 = 0
    c2 = 0
    even = False
    odd = False
    c_all = len(num1) + len(num2)

    if(c_all % 2 == 0):
        even = True
    total_length = num1 + num2
    flag = False
    while(flag == False):
        if (num1[c1] <= num2[c2]):

    return





def main():
    #readJson('/Users/asurj/Documents/GitHub/datascienceprep/MOCK_DATA.json')
    
    str = "hellabcao"
    str2 = "mnhlabc"
    #print(increasingSub(str))
    #print(commonSub(str,str2))
    #print(arr)
    


if __name__ == "__main__":
    main()
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    arr = [3, 5, 9, 2, 6, 4, 7, 2, 9, 1, 3, 6, 2, 8]
    print(contSubarrays(arr, 8))
    arr = mergeSort(arr)
    
    #printInOrder(root)
    #printInPreorder(root)
    #printInPostorder(root)
    