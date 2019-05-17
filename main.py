from wiki import *

lieu = input("Que voulez vous savoir ? ")

wiki = WikiSearch(lieu)
print(wiki.extract_info())
