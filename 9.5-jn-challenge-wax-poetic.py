import random

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "glistening"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

def a_or_an(adj):
    if adj[0] in ("a", "e", "i", "o", "u"):
        return "An"
    else:
        return "A"

def generate_poem():

    random_nouns = [random.choice(nouns) for i in range(3)]
    random_verbs = [random.choice(verbs) for i in range(3)]
    random_adjectives = [random.choice(adjectives) for i in range(3)]
    random_prepositions = [random.choice(prepositions) for i in range(2)]
    random_adverb = random.choice(adverbs)

    poem_title = a_or_an(random_adjectives[0]) + " " + random_adjectives[0] + " " + random_nouns[0]  
    poem_line1 = f"{a_or_an(random_adjectives[0])} {random_adjectives[0]} {random_nouns[0]} {random_verbs[0]} {random_prepositions[0]} the {random_adjectives[1]} {random_nouns[1]}"
    poem_line2 = f"{random_adverb.capitalize()}, the {random_nouns[0]} {random_verbs[1]}"
    poem_line3 = f"The {random_nouns[1]} {random_verbs[2]} {random_prepositions[1]} {a_or_an(random_adjectives[2]).lower()} {random_adjectives[2]} {random_nouns[2]}"

    print(poem_title + "\n")
    print(poem_line1)
    print(poem_line2)
    print(poem_line3)

generate_poem()

# print(a_or_an(random_adjectives[0]) + " " + random_adjectives[0])
    



