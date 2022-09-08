# Our goal is to find a particular text query within a multiline string. 
# You want to find the query in the text and return its immediate environment,
# up to 18 positions around the found query. 

letters_amazon = """
We spent several years building our own database engine,
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible
service with the same or better durability and availability as
the commercial engines, but at one-tenth of the cost. We were
not surprised when this worked.
"""

# one liner
find = lambda txt, sub_str: txt[txt.find(sub_str)-18:txt.find(sub_str)+18] if sub_str in txt else -1

print(find(letters_amazon, 'SQL'))