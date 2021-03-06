import random
from sprite import Sprite
from stats import Stats
from update import Update

TYPES = [
    "sprites/sheepRight.png",
    "sprites/lightningRight.png",
    "sprites/bluePotion.png",
    "sprites/greenPotion.png",
    "sprites/orangePotion.png",
    "sprites/redPotion.png",
    "sprites/boss1r.png",
    "sprites/boss2r.png",
    "sprites/boss3r.png",
    "sprites/boss4r.png",
    "sprites/ghost1r.png",
    "sprites/ghost2r.png",
    "sprites/ghost3r.png",
    "sprites/ghost4r.png",
    "tiles/depthGrayTile.png",
    "tiles/flatGrayTile.png",
    "tiles/solidGray.png",
    "tiles/simpleGray.png",
    "tiles/stoneTile.png",
    "tiles/metalTile.png",
    "tiles/fallTree1.png",
    "tiles/fallTree2.png",
    "tiles/fallTree3.png",
    "tiles/springTree.png",
    "tiles/grass.png",
    "tiles/redWoodLeftRight.png",
    "tiles/redWoodUpDown.png",
    "tiles/woodLeftRight.png",
    "tiles/woodUpDown.png"
]

SHEEP_SPRITES = [
    "sprites/sheepUp.png",
    "sprites/sheepDown.png",
    "sprites/sheepLeft.png",
    "sprites/sheepRight.png",
    "sprites/sheepUpAttack.png",
    "sprites/sheepDownAttack.png",
    "sprites/sheepLeftAttack.png",
    "sprites/sheepRightAttack.png"
]

GHOST1_SPRITES = [
    "sprites/ghost1l.png",
    "sprites/ghost1r.png",
    "sprites/ghost1l.png",
    "sprites/ghost1r.png"
]

GHOST2_SPRITES = [
    "sprites/ghost2l.png",
    "sprites/ghost2r.png",
    "sprites/ghost2l.png",
    "sprites/ghost2r.png"
]

GHOST3_SPRITES = [
    "sprites/ghost3l.png",
    "sprites/ghost3r.png",
    "sprites/ghost3l.png",
    "sprites/ghost3r.png"
]

GHOST4_SPRITES = [
    "sprites/ghost4l.png",
    "sprites/ghost4r.png",
    "sprites/ghost4l.png",
    "sprites/ghost4r.png"
]   

SHEEP = 0
LIGHTNING = 1
BLUE_POTION = 2
GREEN_POTION = 3
ORANGE_POTION = 4
RED_POTION = 5
BOSS1 = 6
BOSS2 = 7
BOSS3 = 8
BOSS4 = 9
GHOST1 = 10
GHOST2 = 11
GHOST3 = 12
GHOST4 = 13
DEPTH_GRAY_TILE = 14
FLAT_GRAY_TILE = 15
SOLID_GRAY_TILE = 16
SIMPLE_GRAY_TILE = 17
STONE_TILE = 18
METAL_TILE = 19
FALL_TREE1_TILE = 20
FALL_TREE2_TILE = 21
FALL_TREE3_TILE = 22
SPRING_TREE_TILE = 23
GRASS_TILE = 24
REDWOOD_LEFTRIGHT_TILE = 25
REDWOOD_UPDOWN_TILE = 26
WOOD_LEFTRIGHT_TILE = 27
WOOD_UPDOWN_TILE = 28

INDOOR_TYPE = [
    DEPTH_GRAY_TILE,
    FLAT_GRAY_TILE,
    SIMPLE_GRAY_TILE,
    STONE_TILE,
    METAL_TILE,
    REDWOOD_LEFTRIGHT_TILE,
    REDWOOD_UPDOWN_TILE,
    WOOD_LEFTRIGHT_TILE,
    WOOD_UPDOWN_TILE
]

SPRING_TYPE = [
    GRASS_TILE,
    SPRING_TREE_TILE
]

FALL_TYPE = [
    GRASS_TILE,
    FALL_TREE1_TILE,
    FALL_TREE2_TILE,
    FALL_TREE3_TILE
]

TERRAIN = [
    DEPTH_GRAY_TILE,
    FLAT_GRAY_TILE,
    SOLID_GRAY_TILE,
    SIMPLE_GRAY_TILE,
    STONE_TILE,
    METAL_TILE,
    FALL_TREE1_TILE,
    FALL_TREE2_TILE,
    FALL_TREE3_TILE,
    SPRING_TREE_TILE,
    GRASS_TILE,
    REDWOOD_LEFTRIGHT_TILE,
    REDWOOD_UPDOWN_TILE,
    WOOD_LEFTRIGHT_TILE,
    WOOD_UPDOWN_TILE,
]

SOLID_TERRAIN = {
    FALL_TREE1_TILE,
    FALL_TREE2_TILE,
    FALL_TREE3_TILE,
    SOLID_GRAY_TILE,
    SPRING_TREE_TILE,
}

ITEMS = [
    BLUE_POTION,
    GREEN_POTION,
    ORANGE_POTION,
    RED_POTION,
]

LIVING_ENTITIES = [
    GHOST1,
    GHOST2,
    GHOST3,
    GHOST4,
]

BOSS_ENTITIES = [
    BOSS1,
    BOSS2,
    BOSS3,
    BOSS4
]

def is_boss(entity_type):
    for etype in BOSS_ENTITIES:
        if entity_type == etype:
            return True
    return False

def is_solid_terrain(entity_type):
    for etype in SOLID_TERRAIN:
        if entity_type == etype:
            return True
    return False

def is_living(entity_type):
    for etype in LIVING_ENTITIES:
        if entity_type == etype:
            return True
    return False

def is_player(entity_type):
    if entity_type == SHEEP:
        return True
    return False

def is_item(entity_type):
    for etype in ITEMS:
        if entity_type == etype:
            return True
    return False

def is_terrain(entity_type):
    for etype in TERRAIN:
        if entity_type == etype:
            return True
    return False

def generate_terrain_entity(x, y, maptype, floor):
    # generate random map item of a given type
    if random.randint(0,10) == 10:
        if maptype == 0:
            ent_type = FALL_TYPE[random.randint(1,len(FALL_TYPE)-1)]
        elif maptype == 1:
            ent_type = SPRING_TREE_TILE
        else:
            ent_type = SOLID_GRAY_TILE
    else:
        if maptype == 0 or maptype == 1:
            ent_type = GRASS_TILE
        else:
            ent_type = INDOOR_TYPE[floor]

    stats = Stats(x, y)
    solid = False
    if ent_type in SOLID_TERRAIN:
        solid = True
    return Entity(stats, ent_type, solid)

def generate_item_entity(x, y):
    ent_type = ITEMS[random.randint(0, len(ITEMS)-1)]
    stats = Stats(x, y)
    solid = False
    return Entity(stats, ent_type, solid)

def generate_living_entity(x, y):
    ent_type = LIVING_ENTITIES[random.randint(0, len(LIVING_ENTITIES)-1)]
    stats = Stats(x, y)
    solid = True
    return Entity(stats, ent_type, solid)

def generate_player_entity(x, y):
    return Entity(Stats(x, y), SHEEP, True)

class Entity:
    count = 1
    def __init__(self, stats, ent_type, solid, name = "", id_num=None):
        if not id_num:
            self.id_num = Entity.count
            Entity.count += 1
        else:
            self.id_num = id_num
        self.stats = stats
        self.ent_type = ent_type
        if ent_type == SHEEP:
                self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y, 32, 32, False, 3, SHEEP_SPRITES)
        elif ent_type == GHOST1:
            self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y, 32, 32, False, 3, GHOST1_SPRITES)
        elif ent_type == GHOST2:
            self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y, 32, 32, False, 3, GHOST2_SPRITES)
        elif ent_type == GHOST3:
            self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y, 32, 32, False, 3, GHOST3_SPRITES)
        elif ent_type == GHOST4:
            self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y, 32, 32, False, 3, GHOST4_SPRITES)

        else:
            self.sprite = Sprite(TYPES[self.ent_type], stats.x, stats.y)
        self.solid = solid
        self.name = name

    def update(self, viewport):
        self.sprite.update(self.stats, viewport)

    def getUpdate(self):
        return Update(self.id_num, self.ent_type, self.stats, self.name)
