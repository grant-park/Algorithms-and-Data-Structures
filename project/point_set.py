import point_pair

def getX(item):
	return item[0]

def getY(item):
	return item[1]

def bruteForce(x):
	minimum = float('inf')
	minimum_i = 0
	minimum_j = 0
	for i in range(0,len(x)-1):
		for j in range(i+1,len(x)):
			if point_pair.point_distance(x[i],x[j])<minimum:
				minimum = point_pair.point_distance(x[i],x[j])
				minimum_i = i
				minimum_j = j
	return(minimum,x[minimum_i],x[minimum_j])


def cp(x_list,y_list):

	if len(x_list)<=3:
		return bruteForce(x_list)
	else:
		# Divide
		x_left_half = x_list[:len(x_list)//2]
		x_right_half = x_list[len(x_list)//2:]

		y_left_half = []
		y_right_half = []

		x_middle = x_list[len(x_list)//2][0]
		for i in range(0,len(y_list)):
			if y_list[i][0] < x_middle:
				y_left_half.append(y_list[i])
			else:
				y_right_half.append(y_list[i])

		# Choose closer pair of the left and right halves
		(distance_left_half, l1, l2) = cp(x_left_half, y_left_half)
		(distance_right_half, r1, r2) = cp(x_right_half, y_right_half)

		if point_pair.closer_than((l1,l2),(r1,r2)) < 0:
			(chosen_distance, p1, p2) = (distance_left_half, l1, l2)
		else:
			(chosen_distance, p1, p2) = (distance_right_half, r1, r2)

		# compute the middle strip
		y_d = []

		# middle = (x_list[len(x_list)-1][0] - x_list[0][0])/2
		
		middle = x_list[len(x_list)//2][0]

		for each in y_list:
			if abs(middle - each[0]) < chosen_distance:
				y_d.append(each)

		for i in range(0,len(y_d)):
			point_middle = y_d[i][1]
			nearby_points_d = []
			for low in y_d[:i]:
				if abs(low[1]-point_middle) < chosen_distance:
					nearby_points_d.append(low)
			for high in y_d[i+1:]:
				if abs(high[1]-point_middle) < chosen_distance:
					nearby_points_d.append(high)
			for element in nearby_points_d:
				if point_pair.pair_distance(element,y_d[i]) < chosen_distance:
					(chosen_distance, p1, p2) = (point_pair.pair_distance(element,y_d[i]), element, y_d[i])

		return (chosen_distance,p1,p2)

def closest_pair(points):

	inputted_array = points

	# Preprocessing
	x_sorted_inputted_array = sorted(inputted_array, key=getX)
	y_sorted_inputted_array = sorted(inputted_array, key=getY)

	return cp(x_sorted_inputted_array, y_sorted_inputted_array)

	# return [(-2.05, 2.6), (1.56, 3.0), (-0.4, -0.6), (5, 1)]



if __name__ == '__main__':
	closest_pair()