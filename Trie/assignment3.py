'''
Skeletal code author: Wern Han Lim Ian
Code Author: Zhong Kern Fong (30284104)
'''


# import libraries as needed
# no external library is needed for this assignment

# no programming lines should be outside functions or if __name__ == "__main__":
# else you would use marks as it is bad programming practice and messes up with the tester

# The Node class
# Note: Node class can be an internal class in the Trie class


class Node:
	"""
	The Node class for the Trie
	"""

	def __init__(self):
		# Length of all alphabets = 26, size is 27 because of added terminal at index 0
		size = 27
		self.link = [None] * size
		self.prefix_freq = 0
		self.word_count = 0
		self.word_string = None


# The Trie class
class Trie:
	"""
	Something about the Trie class
	You might want to add a few other functions to make your code cleaner such as __setitem__ etc...
	"""

	def __init__(self, text):
		"""
		Pre-process text into the trie
		Precondition: None
		Arguments:          text = A list of strings where a string is a non-empty string consisting of lowercase
								   English alphabet characters. No empty strings and duplicates are allowed
		Time complexity:    Best case:  O(1) where text is an empty list, create a Node object at self.root
							Worst case: O(N) where N is the number of character over all strings in the list.
		Space complexity: O(N) where N is the number of elements from text input parameter
		Aux space complexity: O(1), storing of attributes in each node
		Return: None
		"""
		if text:
			self.root = Node()
			self.root.prefix_freq = len(text)
			for element in text:
				current = self.root
				for char in element:
					index = ord(char) - 97 + 1
					# if path exist
					if current.link[index] is not None:
						current = current.link[index]
						current.prefix_freq += 1
					else:
						# Creating a new node
						current.link[index] = Node()
						current = current.link[index]
						current.prefix_freq += 1
				# End of char in element, go to terminal and create new node if path doesn't exist
				index = 0
				if current.link[index] is not None:
					current = current.link[index]
				else:
					current.link[index] = Node()
					current = current.link[index]
				# End of word for current element, word count for this path += 1
				current.word_count += 1

				# Store the current word if its not duplicate
				if current.word_string is None:
					current.word_string = element
		else:
			self.root = Node()

	def string_freq(self, query_str):
		"""
		Word_count integer counter value that is stored in the terminal of a string.
		Precondition: A Trie class object must be instantiated with intended strings within a text list.
		Arguments:          query_str = A non-empty string consisting of lowercase English alphabet characters.
		Time complexity:    Best case: O(1) where query_str is of length 1 and the single character does not exist from
									   the text. Eg: Trie was instantiated with ["a"], query_str is "z".
							Worst case: O(N) where N is the length of the query_str.
		Space complexity: O(1), length of input string query_str
		Aux space complexity: O(1), storing memory location of function variables
		Return: An integer where it is the number of elements of the text which matches query_string.
		"""
		# step 1: Loops through each character of query_str and calculates the index of each character where terminal ($)
		#         is index 0 and a is index 1... till index 26
		# step 2: If there is a link (Node object), current variable will traverse through the Trie according to the index
		#         If there is no link, return 0, this is because the string does not exist in the Trie.
		# step last: At the end of the character from query_str, go to the terminal and return the attribute which
		#            records the number of word that matches the text which are exactly query_string.
		current = self.root
		for char in query_str:
			# $ = 0, a = 1, b = 2, c = 3 ...
			index = ord(char) - 97 + 1
			if current.link[index] is not None:
				current = current.link[index]
			else:
				return 0
		# Found query_str in trie, go to terminal $ at index = 0
		index = 0
		if current.link[index] is not None:
			current = current.link[index]
		return current.word_count

	def prefix_freq(self, query_str):
		"""
		Prefix frequency integer value that is stored at each node
		Precondition: A Trie class object must be instantiated with intended strings within a text list.
		Arguments:          query_str = An empty string as prefix for all strings or wanted prefix of a string.
		Time complexity:    Best case: O(1) where query_str is empty
							Worst case: O(N) where N is the length of the query_str
		Space complexity: O(1), length of query_str and memory locations for function variables
		Aux space complexity: O(1), storing memory locations for function variables
		Return: An integer which is the number of words in the text which have query_str as a prefix.
		"""
		# step 1: If query_str is an empty string, it will return the total number of strings from text.
		# step 2: Loop through each character in query_str input parameter. At each iteration, calculate the index, and
		#         traverse through the trie object if there is a path (Node object).
		# step last: At the end of the iteration, return an integer which corresponds to the number of words in the text
		#            which have query_str as a prefix.

		current = self.root
		# If query_str is empty, return the prefix_freq that is stored at self.root
		if query_str == "":
			return current.prefix_freq

		for char in query_str:
			# $ = 0, a = 1, b = 2, c = 3 ...
			index = ord(char) - 97 + 1
			if current.link[index] is not None:
				current = current.link[index]
			else:
				return 0
		return current.prefix_freq

	def wildcard_prefix_freq(self, query_str):
		"""
		A function that checks the wildcard prefix string frequency
		Precondition: A Trie class object must be instantiated with intended strings within a text list.
		Arguments:          query_str = a non-empty string consisting only of lowercase English alphabet characters
									   (possibly no characters), and exactly one `?' character, representing a wildcard.
		Time complexity:    Best case: O(q + S) where q and S are explained in worst case. The reason why best case and
									   worst case are the same is because there will always be 1 wildcard character from
									   query_str
							Worst case: O(q + S) where q is the length of query_str and S is from function call of
										find_longest_path()
		Space complexity: O(W), where W is explained in aux space complexity
		Aux space complexity: O(W) where W is the number of object which corresponds to the wildcard Node objects. Eg:
							  given text = ["aaa", "aba", "baa"] and query_str = "a?a", wildcard_pos will store 2 Node
							  objects.
		Return: A list of strings which corresponds to the number of string from input text and wildcard prefix query_str
		"""
		# step 1: Instantiation of local variable output list, wildcard_pos list and a char_counter which will act as a
		#         pointer when iterating query_str.
		# step 2: At self.root, I will first iterate through query_str to traverse through query_str with required
		#         prefix if the character is not '?' and increment my char_counter. If the character is '?', I will
		#         store all Node object that is not None in current.link into wildcard_pos list.
		# step 3: I will then loop through each of the Node object, at each Node object I will call find_longest_path.
		# step last: Once the iteration of all wildcard object Nodes are done, my output should store the required string

		# Instantiation of output array, possible wildcard positions and index_counter
		output = []
		wildcard_pos = []
		char_counter = -1

		current = self.root
		for char in query_str:
			# If it is not a wildcard
			if char != "?":
				char_counter += 1
				# $ = 0, a = 1, b = 2, c = 3 ...
				index = ord(char) - 97 + 1
				# If there is a link in trie of the current char
				if current.link[index] is not None:
					current = current.link[index]
				# If there is no link in trie of the current char
				else:
					return output
			# It is a wildcard char
			else:
				# I want to store every Node object except Node object that stores terminal
				for i in range(1, len(current.link)):
					if current.link[i] is not None:
						wildcard_pos.append(current.link[i])
				char_counter += 2
				break
		# From each wildcard positions, each element is a node
		for node in wildcard_pos:
			self.find_longest_path(node, output, char_counter, query_str)
		return output

	def find_longest_path(self, nodeObj, output, char_counter, query_str):
		"""
		Finding the deepest node using recursion and in order traversal
		Precondition: A Trie class object must be instantiated with intended strings within a text list.
		Arguments:          query_str = a non-empty string consisting only of lowercase English alphabet characters
									   (possibly no characters), and exactly one `?' character, representing a wildcard.
		Time complexity:    Best case: O(1), if there is no path and the current Node is the deepest Node
							Worst case: O(q + S) where q is the length of query_str and S is the total number of
										characters in all strings of the text which have a prefix matching query_str.
		Space complexity: O(L + S) where L is the length of output list which has worst case of S and S is explained in
						  aux space complexity.
		Aux space complexity: O(S) where S is the total number of characters in all strings of the text (inclusive of
							  duplicates) which have a prefix matching query_str
		Return: Updates parameters of output and char_counter.
		"""
		# step 1: If the char_counter is lesser than the length of query_str, this means that there is still character(s)
		# 		  that I have to traverse to. Else, I will recurse to the deepest node and store the word_string into
		# 		  output list on return.
		# step 2: During return, I will check if word_list is None, as the deepest node will only store the string and
		#         no strings will be stored mid-way. The number of times the strings is stored is based on word_count
		#         which is stored at the node

		# If there are still characters from query_str that has not been traversed through, then traverse to meet
		# output requirement.
		if char_counter < len(query_str):
			index = ord(query_str[char_counter]) - 97 + 1
			if nodeObj.link[index] is not None:
				self.find_longest_path(nodeObj.link[index], output, char_counter + 1, query_str)

		# End of query_str length, fully traversed through query_str
		if char_counter >= len(query_str):
			for path in nodeObj.link:
				if path is not None:
					# Traverse to deeper Node if there is a path (includes terminal traverse)
					(found_string, number) = self.find_longest_path(path, output, char_counter, query_str)
					if found_string is not None:
						# Loop the number of word_count to store the number of strings required to output
						for _ in range(number):
							output.append(found_string)
			return nodeObj.word_string, nodeObj.word_count


# Main driver
if __name__ == "__main__":
	# driver for the test cases
	print("Running test")


	def test_q2(my_trie):
		query_str = ""
		my_trie.prefix_freq(query_str)
		print("pass test")


	def test_q3(my_trie):
		print("pass test")


	def test_q4(my_trie):
		print("pass test")


	# run test Q2
	bla = Trie(
		["aa", "aab", "aaab", "abaa", "aa", "abba", "aaba", "aaa", "aa", "aaab", "abbb", "baaa", "baa", "bba", "bbab"])
	print(bla.string_freq("aa"))

	# run test Q3
	print(bla.prefix_freq("aa"))

	# run test Q4
	test = Trie(["aa", "aab", "aaab", "abaa", "aa", "abba", "aaba", "aaa", "aa", "aaab", "abbb", "baaa", "baa", "bba", "bbab"])
	print(test.wildcard_prefix_freq("?aa"))
	test2 = Trie(["aaa", "aba", "baa"])
	print(test2.wildcard_prefix_freq("aa?"))
	text = ""
	my_trie = Trie(text)
	test_q2(my_trie)
