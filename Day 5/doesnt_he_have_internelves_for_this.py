# PART 1: 
def part_one(data):
	count = 0
	disallowed = ['ab', 'cd', 'pq', 'xy']
	for word in data:
		vowels = {
			'a': 0,
			'e': 0,
			'i': 0,
			'o': 0,
			'u': 0
		}
		for i in word:
			if i in vowels:
				vowels[i] += 1
		if sum(vowels.values()) < 3:
			continue

		if sum([1 for each in disallowed if each in word]) > 0:
			continue

		present = False
		for i in range(0, len(word) - 1):
			present = present or (word[i] == word[i+1])

		if present:
			count += 1

	return count

# PART 2: 
def part_two(data):
	count = 0
	for word in data:
		two = False
		for i in range(0, len(word) - 1):
			if word[i+2:].find(word[i:i+2]) > -1:
				two = True
				break

		three = False
		for i in range(0, len(word) - 2):
			if word[i] == word[i+2]:
				three = True
				break

		if two and three:
			count += 1

	return count

def main():
	input = []

	with open("input.txt", "r") as file:
		input = file.read().split("\n")

	print("Part 1:", part_one(input))
	print("Part 2:", part_two(input))

if __name__ == '__main__':
	main()