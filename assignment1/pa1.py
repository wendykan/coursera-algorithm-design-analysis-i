def split_list(a_list):
    half = len(a_list)/2
    return a_list[:half], a_list[half:]

# the main merge
def merge(left_list, right_list,count):
    result = []
    i = 0
    j = 0

    while i < len(left_list) and j < len(right_list):
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            count += len(left_list) - i 
            j += 1

    result.extend(left_list[i:]) 
    result.extend(right_list[j:]) 
    return result, count


# divide the list into left and right halfs, and call recursively
def merge_sort(fulllist, count):
    if len(fulllist) < 2: return fulllist, count 

    left_list, right_list = split_list(fulllist)
    merged_left, count = merge_sort(left_list, count)
    merged_right, count = merge_sort(right_list, count)
    merged_list, count =  merge(merged_left, merged_right, count)

    return merged_list, count



def main():

    #### test with file
    fname = 'IntegerArray.txt'
    with open(fname) as f:
        int_list = [int(x) for x in f.readlines()]

        print('read input file!')
        print(merge_sort(int_list, 0)[1])


    #### some test cases
    A = [1,3,5,2,4,6]
    print merge_sort(A, 0)
    assert merge_sort(A, 0)[1]==3
    B = [1,5,3,2,4]
    print merge_sort(B,0)
    assert merge_sort(B,0)[1]==4
    assert merge_sort([5,4,3,2,1],0)[1] == 10
    assert merge_sort([1,6,3,2,4,5],0)[1] == 5
    assert merge_sort([9, 12, 3, 1, 6, 8, 2, 5, 14, 13, 11, 7, 10, 4, 0],0)[1] == 56
    print merge_sort([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, \
        33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, \
        31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45],0)
    assert merge_sort([37, 7, 2, 14, 35, 47, 10, 24, 44, 17, 34, 11, 16, 48, 1, 39, 6, \
        33, 43, 26, 40, 4, 28, 5, 38, 41, 42, 12, 13, 21, 29, 18, 3, 19, 0, 32, 46, 27, \
        31, 25, 15, 36, 20, 8, 9, 49, 22, 23, 30, 45],0)[1] == 590
    

if __name__ == "__main__":
    main()
