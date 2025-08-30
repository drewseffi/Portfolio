import random
from runes import runes

def randomRunes():
    trees = ["Precision", "Domination", "Sorcery", "Resolve", "Inspiration"]
    primary_tree = random.choice(trees)
    secondary_tree = random.choice([t for t in trees if t != primary_tree])

    # Gets keystone and minors for primary tree
    keystone = random.choice([r for r in runes if r.tree == primary_tree and r.type == "Keystone"])
    minor1 = random.choice([r for r in runes if r.tree == primary_tree and r.type == "Minor1"])
    minor2 = random.choice([r for r in runes if r.tree == primary_tree and r.type == "Minor2"])
    minor3 = random.choice([r for r in runes if r.tree == primary_tree and r.type == "Minor3"])

    # Gets minors for secondary tree
    secondary_minor1 = random.choice([r for r in runes if r.tree == secondary_tree and r.type != "Keystone"])
    secondary_minor2 = random.choice([r for r in runes if r.tree == secondary_tree and r.type != "Keystone" and r.type != secondary_minor1.type])

    # Gets shards
    shard1 = random.choice([r for r in runes if r.type == "Shard1"])
    shard2 = random.choice([r for r in runes if r.type == "Shard2"])
    shard3 = random.choice([r for r in runes if r.type == "Shard3"])

    return (keystone.name, minor1.name, minor2.name, minor3.name, secondary_minor1.name, secondary_minor2.name, shard1.name, shard2.name, shard3.name)

# Gets champs from text file and adds them to a list
champions = []

with open("champs.txt") as f:
  for line in f:
    champions.append(line.rstrip())

new_runes = randomRunes()

i = 0
print(random.choice([c for c in champions]))
print("##########")
for r in new_runes:
    print(r)
    i += 1
    if i == 4:
        print("##########")
    elif i == 6:
        print("##########")
print("##########")

# Gets 5 items and a pair of boots
boots = ["Berserker's Greaves", "Boots of Swiftness", "Ionian Boots of Lucidity", "Mercury's Treads", "Plated Steelcaps", "Sorcerer's Shoes", "Symbiotic Soles"]
inv = []
inv.append(random.choice(boots))

items = []
with open("items.txt") as f:
  for line in f:
    items.append(line.rstrip())

inv.extend(random.sample(items, 5))
for i in inv:
   print(i)