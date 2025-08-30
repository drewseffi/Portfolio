class Rune:
    def __init__(self, name: str, tree: str, type: str):
        self.name = name
        self.tree = tree
        self.type = type

runes = [
    # Precision
    Rune("Press the Attack", "Precision", "Keystone"),
    Rune("Lethal Tempo", "Precision", "Keystone"),
    Rune("Fleet Footwork", "Precision", "Keystone"),
    Rune("Conqueror", "Precision", "Keystone"),

    Rune("Absorb Life", "Precision", "Minor1"),
    Rune("Triumph", "Precision", "Minor1"),
    Rune("Presence of Mind", "Precision", "Minor1"),

    Rune("Legend: Alacrity", "Precision", "Minor2"),
    Rune("Legend: Haste", "Precision", "Minor2"),
    Rune("Legend: Bloodline", "Precision", "Minor2"),

    Rune("Coup de Grace", "Precision", "Minor3"),
    Rune("Cut Down", "Precision", "Minor3"),
    Rune("Last Stand", "Precision", "Minor3"),

    # Domination
    Rune("Electrocute", "Domination", "Keystone"),
    Rune("Dark Harvest", "Domination", "Keystone"),
    Rune("Hail of Blades", "Domination", "Keystone"),

    Rune("Cheap Shot", "Domination", "Minor1"),
    Rune("Taste of Blood", "Domination", "Minor1"),
    Rune("Sudden Impact", "Domination", "Minor1"),

    Rune("Sixth Sense", "Domination", "Minor2"),
    Rune("Gisly Mementos", "Domination", "Minor2"),
    Rune("Deep Ward", "Domination", "Minor2"),

    Rune("Treasure Hunter", "Domination", "Minor3"),
    Rune("Relentless Hunter", "Domination", "Minor3"),
    Rune("Ultimate Hunter", "Domination", "Minor3"),

    # Sorcery
    Rune("Summon Aery", "Sorcery", "Keystone"),
    Rune("Arcane Comet", "Sorcery", "Keystone"),
    Rune("Phase Rush", "Sorcery", "Keystone"),

    Rune("Axiom Arcanist", "Sorcery", "Minor1"),
    Rune("Manaflow Band", "Sorcery", "Minor1"),
    Rune("Nimbus Cloak", "Sorcery", "Minor1"),

    Rune("Transcendence", "Sorcery", "Minor2"),
    Rune("Celerity", "Sorcery", "Minor2"),
    Rune("Absolute Focus", "Sorcery", "Minor2"),

    Rune("Scorch", "Sorcery", "Minor3"),
    Rune("Water Walking", "Sorcery", "Minor3"),
    Rune("Gathering Storm", "Sorcery", "Minor3"),

    # Resolve
    Rune("Grasp of the Undying", "Resolve", "Keystone"),
    Rune("Aftershock", "Resolve", "Keystone"),
    Rune("Guardian", "Resolve", "Keystone"),

    Rune("Demolish", "Resolve", "Minor1"),
    Rune("Font of Life", "Resolve", "Minor1"),
    Rune("Shield Bash", "Resolve", "Minor1"),

    Rune("Conditioning", "Resolve", "Minor2"),
    Rune("Second Wind", "Resolve", "Minor2"),
    Rune("Bone Plating", "Resolve", "Minor2"),

    Rune("Overgrowth", "Resolve", "Minor3"),
    Rune("Revitalise", "Resolve", "Minor3"),
    Rune("Conditioning", "Resolve", "Minor3"),

    # Inspiration
    Rune("Glacial Augment", "Inspiration", "Keystone"),
    Rune("Unsealed Spellbook", "Inspiration", "Keystone"),
    Rune("First Strike", "Inspiration", "Keystone"),

    Rune("Hextech Flashtraption", "Inspiration", "Minor1"),
    Rune("Magical Footwear", "Inspiration", "Minor1"),
    Rune("Cash Back", "Inspiration", "Minor1"),

    Rune("Triple Tonic", "Inspiration", "Minor2"),
    Rune("Timewarp Tonic", "Inspiration", "Minor2"),
    Rune("Biscuit Delivery", "Inspiration", "Minor2"),

    Rune("Cosmic Insight", "Inspiration", "Minor3"),
    Rune("Approach Velocity", "Inspiration", "Minor3"),
    Rune("Jack of all Trades", "Inspiration", "Minor3"),

    # Shards
    Rune("Adaptive Shard", "All", "Shard1"),
    Rune("Attack Speed Shard", "All", "Shard1"),
    Rune("Ability Haste Shard", "All", "Shard1"),

    Rune("Adaptive Shard", "All", "Shard2"),
    Rune("Move Speed Shard", "All", "Shard2"),
    Rune("Health Scaling Shard", "All", "Shard2"),

    Rune("Health Shard", "All", "Shard3"),
    Rune("Tenacity and Slow Resist Shard", "All", "Shard3"),
    Rune("Health Scaling Shard", "All", "Shard3"),
]