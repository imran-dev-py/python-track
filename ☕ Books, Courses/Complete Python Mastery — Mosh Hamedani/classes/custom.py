# create custom class

class TagCloud:
    def __init__(self):
        self.__tags = {}
    
    # get length of the tags
    def __len__(self):
        return len(self.__tags)

    # set tag in tags
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count
    
    # get the tag
    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 'Invalid')

    # iterating the tags
    def __iter__(self):
        return iter(self.__tags)
    
    # add tag in the tags [increment by 1 each item same tag set]
    def addTag(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

cloud = TagCloud()
cloud.addTag('JavaScript')
cloud['javaScript'] = 15
print(len(cloud)) # 1
print(cloud['JavaScript'])  # 15
# print(cloud.__tags)
print(cloud)

for tag in cloud: 
    print(tag)