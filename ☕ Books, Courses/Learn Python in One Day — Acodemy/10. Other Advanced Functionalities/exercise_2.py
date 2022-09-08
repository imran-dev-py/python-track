import re
text = 'Here is some text that contains something'
pattern = 'that'

match = re.search(pattern, text)
if match:
    print(f'Yes {pattern} was found in the text spanning\
 from index {match.start()} to {match.end()}')
else:
    print(f'No, {pattern} was not found in the text')
