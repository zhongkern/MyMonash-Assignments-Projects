"""
Author:     Fong Zhong Kern (30284104)
Timestamps:
"""


def longest_oscillation(L):
	"""
	Getting the longest_oscillation from an input list L using brute force method (adjacent element comparison).
	:param L: List L containing integers value only (Does not need to be in order)
	:return: Longest oscillation and index of the oscillations within a tuple
	Time complexity: Best case: O(1) where input list L is empty or has 1 element only
					 Worst case: O(N) where N is the length of input L
	Space complexity: O(N + P) where N is the length of input L + aux space
	Aux space complexity: O(P) where P is the number of peaks and valleys from L (P >= 1, P <= len(L)) stored in output
	"""

	# Step 1: Determining base cases. Intuitively, we should understand that if L is an empty list, there is no
	#         oscillation. Hence, we return 0,[]. However, if the input list L contains only 1 element, then we return
	#         the single oscillating element return 1,[0].
	# Step 2: I will begin initializing sub_output and output array and begin finding for peak and valley points by
	#         brute force method. Before implementing brute force, we should understand that the first element is always
	#         a peak or valley no matter what the value of the element represents. Hence, output = [0].
	#         If previous element is the same as current element, I will not append it to the output as required from
	#         assignment sheet and its neither peak or valley.
	#         Explanation of the brute force method, I can compare using current element and its
	#         adjacent element (if they exist or not out of bounds) to get the peak and valley points.
	#         Using logic checks such as checking if the element is increasing or decreasing and checking if the next
	#         element is larger or smaller, we can determine the peak and valleys respectively.
	#         Every peak and valley index will be stored into output.
	# Step 3: Finally, once all index of peak and valley are extracted, it will be returned as output.

	# Begin of longest_oscillation implementation.
	# If input is empty, return empty. Else if the list is a single element, return the single element.
	if not L:
		return 0, []

	if len(L) == 1:
		return 1, [0]

	# Base case, no matter what number is in the first element its always the peak or valley
	output = [0]

	# Begin iteration through list L to get peaks and valleys and store into sub_output. Using adjacent comparison method.
	for i in range(1, len(L)):
		# Checking if element of previous index is the same as the current element
		# As required from assignment sheet, it should not be stored in output.
		if (i - 1 >= 0) and (L[i-1] == L[i]):
			continue
		if find_peak(L, len(L), L[i], i - 1, i + 1):
			output.append(i)
		if find_valley(L, len(L), L[i], i - 1, i + 1):
			output.append(i)

	return len(output), output


# Auxiliary function for finding peak in longest oscillation
def find_peak(lst, length, current_element, previous_index, next_index):
	"""
	Using brute force method to determine peaks from the input list throughout iteration of input list by using
	logic checks.
	:param lst: Input list L
	:param length: Length of input list
	:param current_element: current element at iteration
	:param previous_index: contains the i-th - 1 value from iteration
	:param next_index: contains the i-th + 1 value from iteration
	:return: Boolean value True or False if the current element is the peak
	Time complexity: Best and worst case: O(1), it is a boolean function, just checks if and else and return appropriate
										  boolean values.
	Space complexity: O(N) where N is the length of the input list
	Aux space complexity: O(1), no space is created, only checks boolean values
	"""
	# Checking next index, if not out of right bound and next element > current_element
	# Increasing (not yet peak)
	if (next_index < length) and (lst[next_index] > current_element):
		return False

	# Checking previous index, if not out of left bound and element before > current_element
	# Decreasing in value (Definitely not peak)
	if (previous_index >= 0) and (lst[previous_index] > current_element):
		return False

	else:
		return True


# Auxiliary function for finding valley in longest oscillation
def find_valley(lst, length, current_element, previous_index, next_index):
	"""
	Using brute force method to determine valley from the input list throughout iteration of input list by using
	logic checks.
	:param lst: Input list L
	:param length: Length of input list
	:param current_element: Current element at i-th iteration
	:param previous_index: contains the i-th - 1 value from iteration
	:param next_index: contains the i-th + 1 value from iteration
	:return: Boolean value (True or False) which indicates whether the current element is a valley
	Time complexity: Best and worst case: O(1), it is a boolean function, just checks if and else and return appropriate
										  boolean values.
	Space complexity: O(N) where N is the length of the input list
	Aux space complexity: O(1), no space is created, only checks boolean values
	"""
	# Checking next index, if not out of right bound and next element < current_element
	# Decreasing (not yet valley)
	if (next_index < length) and (lst[next_index] < current_element):
		return False

	# Checking previous index, if not out of left bounds and current_element is larger than element before
	# Increasing in value (Definitely not valley)
	if (previous_index >= 0) and (lst[previous_index] < current_element):
		return False

	else:
		return True


def longest_walk(M):
	"""
	Function to find the longest walk from the given matrix M
	:param M: Input matrix containing only integers
	:return: A tuple containing the longest path and each path taken in a form of a tuple containing row and column
			 values in an array
	Time complexity: Best case: O(1) where matrix M from parameter is empty or its first element list is empty
					 Worst case: O(3NM + 2K) where N and M are the rows and columns of the input matrix M. K is fixed
					             constant of 8 where is represents the possible directions.
	Space complexity: O(3NM) where it is the matrix M + aux space complexity (memo table and worst case coordinates list).
	Aux space complexity: O(2NM) where N and M are the rows and columns of the input matrix M. They are the memo table
						  and worst case coordinates list.
	"""
	# Step 1: I check if the matrix is empty, if it is empty or if its first element is an empty list, I will return
	#         0, [] as there i no possible movements
	# Step 2: If it is neither of the base cases, I will initialize local variables that are needed for the algorithm.
	#         They include rows, columns, longest_path and memo with the size of input matrix M.
	# Step 3: Once all variables are initialized I will loop through the matrix and fill the memo table by doing a
	#         nested for loop which is O(NM + K) if the memo table at its current iteration is empty by using
	#         find_longest_path function and comparing the longest_path value using max(longest_path, recursion_longest)
	# Step 4: After the loop is done to fill in the memo table, I will have the longest path. I will then loop through
	#         memo to find the position of the longest path so that I can perform back tracking O(NM).
	# Step 5: Finally, I will call backtracking function which returns me the coordinate that was taken to produce the
	#         longest path O(NM + K).

	# Base case, if matrix row provided is empty or column is empty, return 0, [] (No possible movements)
	if not M or not M[0]:
		return 0, []

	# Initializing local variables
	longest_path = 0
	rows = len(M)
	# All columns must be of the same length in a matrix. So just get the length of first element's column
	cols = len(M[0])

	# Initializing memo to be same size as input matrix
	memo = []
	for i in range(rows):
		memo.append([None] * cols)

	# Main loop on matrix. Fills memo table when each elements are visited.
	for row in range(rows):
		for col in range(cols):
			# If memo on current iteration is empty, then I need to search for longest path and fill memo table.
			if memo[row][col] is None:
				longest_path = max(longest_path, find_longest_path(M, row, col, memo))

	# Looping through memo to find the longest path position
	longest_path_position = (-1, -1)
	for row in range(rows):
		for col in range(cols):
			if memo[row][col] == longest_path:
				longest_path_position = (row, col)
				break
	# From the longest path coordinate extracted from memo, I will perform backtracking to get every coordinate
	coordinate = backtracking(longest_path_position[0], longest_path_position[1], memo, M, longest_path)

	return longest_path, coordinate


# Function for finding longest path
def find_longest_path(matrix, row, col, memo):
	"""
	This function checks for the longest possible path from its current element, if memo does not have the
	longest path at its current iteration position, this function will be called. This function will perform recursion
	until there are no valid movements and stores the longest possible path from each selected direction.
	:param matrix: Input matrix M
	:param row: The row at current iteration
	:param col: The col at current iteration
	:param memo: Memoization table
	:return: Value of the longest path from this current_element
	Time complexity: Best case: O(1) where from current element there is no valid moves, surrounding elements are smaller
								than its current element.
					 Worst case: O(NM + K) where N and M are the rows and columns respectively. If every movement is
					             valid (a straight trail) it would recurse through every element once. K represents
					             all possible directions, K = 8
	Space complexity: Best case: O(2NM) where N and M are the rows and columns respectively from matrix and memo.
					  Worst case: O(3NM) where N and M are the rows and columns from matrix and memo along the addition
					              of aux space of worst case.
	Aux space complexity: Best case: O(1), where there is no valid moves from its current position. Surrounding elements
									 are equal or smaller than its current element and hence no recursion call is made.
						  Worst case: O(NM) where N and M are the rows and columns respectively. If every movement is
						              a valid move (again a straight line trail), it would recurse through the entire
						              matrix.
	"""
	# Step 1: From an element where memo has no record of its longest path, I have to check from every possible
	#         direction to see if it is a valid move.
	# Step 2: If it is a valid move, I will update my x and y direction and store it in dir_x and dir_y respectively.
	#         Recursion of its own function is called with the new x and y direction. The base case is when there is
	#         no more valid moves (out of matrix bounds and no surrounding value that is larger).
	# Step 3: On return from recursion calls, the memoization table is filled up from its valid moves position(s)
	#         with the longest_path + 1 where 1 represents the current element itself and longest_path from every past
	#         recursion call.
	# Step 4: Once all recursion calls are returned, I will return the value of memo[row][col] which will be the longest
	#         path from the current iteration to be stored in variable longest_path from longest_walk function.

	# If at current recursion / direction, if memo has record, use the value from its record
	if memo[row][col]:
		return memo[row][col]
	longest_path = 0

	# Checking each and every direction for current element (loops 8 time)
	for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
		dir_x, dir_y = row + i, col + j
		# Checking if within bounds and direction of next value in matrix M is larger than current element in matrix M
		if 0 <= dir_x < len(matrix) and 0 <= dir_y < len(matrix[0]) and matrix[dir_x][dir_y] > matrix[row][col]:
			longest_path = max(longest_path, find_longest_path(matrix, dir_x, dir_y, memo))
	memo[row][col] = longest_path + 1
	return memo[row][col]


def backtracking(row, col, memo, matrix, longest_path):
	"""
	This function is called once the longest path position is determined by looping through the memo matrix. This
	function backtracks from the longest path to get the path which was taken by using back tracking method.
	:param row: The row of the longest path position
	:param col: The column of the longest path position
	:param memo: The memoization matrix
	:param matrix: The input matrix M
	:param longest_path: The longest path that was received by performing find_longest_path on input matrix M
	:return: A list containing all the past path taken to get the longest path.
	Time complexity: Best case: O(1) where elements around longest path position is equal or smaller than itself.
					 Worst case: O(NM + K) where K is a fixed constant of checking through every direction
								 K = 8.
	Space complexity: Best case: O(2NM) where N and M are the rows and columns of input matrix M. It is the addition of
								 memo and matrix
					  Worst case: O(3NM) where it is the addition of memo, matrix, and coordinate
	Aux space complexity: Best case: O(1) where all numbers in the matrix are equal.
						  Worst case: O(NM) where N and M are the rows and columns of input list M. On the worst case
						  scenario, if the matrix M is a straight trail, every coordinate of the matrix has to be
						  recorded into coordinate which leads to O(NM).
	"""
	# Step 1: From the longest path position, if longest path is 1, it would return its coordinate as output. Else
	#         it would check from its current position and loop through every direction from its current path to back
	#         track and record every path it has taken.
	# Step 2: If the direction is a valid path, it would append that direction x and y values and update the new row and
	#         column value.
	# Step 3: Once there are no more valid movements, it has reached its initial starting point of the path. I will
	#         then return the list of coordinates for output purposes.

	# Its initial coordinate should also be taken. Hence, coordinate list is initialized with the beginning of row and
	# column value
	coordinate = [(row, col)]

	# Base case, if the longest path is 1, which means it is itself and there are no valid moves around it.
	if longest_path == 1:
		return coordinate

	# Looping through the longest_path to check from every direction to record the path that was taken to be stored in
	# coordinate list
	for _ in range(longest_path):
		for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
			dir_x, dir_y = row + i, col + j
			# If valid backtrack direction, append its coordinate and update row and column values.
			if 0 <= dir_x < len(matrix) and 0 <= dir_y < len(matrix[0]) and memo[row][col] - 1 == memo[dir_x][dir_y] and matrix[dir_x][dir_y] > matrix[row][col]:
				coordinate.append((dir_x, dir_y))
				row = dir_x
				col = dir_y
	return coordinate


if __name__ == "__main__":
	# driver for the test cases
	print("Running test")

	def test_q1():
		print(longest_oscillation([1,1,1,3,4,5,6,2,1,5,6,7,4]))
		print(longest_oscillation([1,2,1,2,1,2,1,2,1,2,1,2]))
		print(longest_oscillation([1, 2, 3, 2, 1, 1, 2, 3, 2, 3, 2, 1]))
		print("pass test Q1")

	def test_q2():
		print(longest_walk([[1, 200, 300],
		              [400, 500, 600],
		              [700, 800, 900],
		              [1, 2, 3],
		              [4, 5, 6],
		              [7, 8, 9],
		              [10, 11, 12],
		              [13, 14, 15],
		              [16, 17, 18],
		              [900, 800, 700],
		              [600, 500, 400],
		              [300, 200, 100]]))
		print(longest_walk(
			[[1,9,2],
			 [3,9,3],
			 [6,5,4]]
		))
		print(longest_walk(
			[[1, 23, 24],
			 [22, 2, 25],
			 [1, 21, 3],
			 [1, 4, 20],
			 [5, 19, 1],
			 [18, 6, 9],
			 [1, 17, 7],
			 [1, 8, 16],
			 [9, 15, 1],
			 [14, 10, 1],
			 [13, 12, 11]]
		))
		print(longest_walk(
			[[9,9,9],
			 [9,9,9],
			 [9,9,9]]
		))
		print("pass test Q2")

	# test_q2()
	# test_q1()
	print("pass all")
