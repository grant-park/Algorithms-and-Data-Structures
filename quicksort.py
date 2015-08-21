def quicksort(array):
	less = []
	equal = []
	greater = []

	if len(array)>1:
		print array
		pivot = array[0]
		for each in array:
			if each < pivot:
				less.append(each)
			if each == pivot:
				equal.append(each)
			if each > pivot:
				greater.append(each)
		return quicksort(less) + equal + quicksort(greater)
	else:
		print array
		return array

print quicksort([1,5,8,7,9,8,6,-1,-2,0])


