# given a multiline string, create a list of lists—each consisting of all the words in a line that have more than three characters.

text = """
Call me Ishmael. Some years ago - never mind how long precisely - having
little or no money in my purse, and nothing particular to interest me
on shore, I thought I would sail about a little and see the watery part
of the world. It is a way I have of driving off the spleen, and regulating
the circulation. - Moby Dick"""

new_text = []
for line in text.split('\n'):
	x = []
	for word in line.split():
		if len(word) > 3:
			x.append(word)
	new_text.append(x)

print(new_text)

print()
# one liner
word = [[word for word in line.split() if len(word) > 3] for line in text.split('\n')]

print(word)