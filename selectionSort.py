numbers =[9,2,8,12,7]

def selSort(numbers):
	for curPos in range(len(numbers)):
		minPos = curPos
		for scanPos in range(curPos+1,len(numbers)):
			if numbers[scanPos] < numbers[minPos]:
				minPos = scanPos
		temp = numbers[minPos]
		numbers[minPos] = numbers[curPos]
		numbers[curPos] = temp
	return numbers




test = selSort(numbers)
print test