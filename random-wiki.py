import wikipedia as wky

# get a random wiki page
rand_title = wky.random(pages=1)
print(rand_title)

# print the link to the user
rand_page = wky.WikipediaPage(title=rand_title).summary
print(rand_page)
