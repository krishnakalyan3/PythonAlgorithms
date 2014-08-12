list = [7,3,1,2,4,6]

def insertionSort(list):
	for index in range(1,len(list)):
		value = list[index]
		i = index - 1
		while i >= 0:
			if value < list[i]:
				list[i+1] = list[i]
				list[i] = value
				i = i - 1
			else:
				break

	return list

print insertionSort(list)