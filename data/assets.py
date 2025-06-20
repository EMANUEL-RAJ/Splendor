from data.constants import ETHER, WATER, FIRE, AIR, EARTH

elder_mages = [
    {
        "requirements": {ETHER: 3, WATER: 3, FIRE: 3},
        "prestige": 3
    },
    {
        "requirements": {WATER: 4, AIR: 4},
        "prestige": 3
    },
    {
        "requirements": {EARTH: 4, FIRE: 4},
        "prestige": 3
    },
    {
        "requirements": {FIRE: 4, ETHER: 4},
        "prestige": 3
    },
    {
        "requirements": {EARTH: 4, AIR: 4},
        "prestige": 3
    },
    {
        "requirements": {EARTH: 3, FIRE: 3, AIR: 3},
        "prestige": 3
    },
    {
        "requirements": {EARTH: 3, WATER: 3, AIR: 3},
        "prestige": 3
    },
    {
        "requirements": {EARTH: 3, FIRE: 3, ETHER: 3},
        "prestige": 3
    },
    {
        "requirements": {ETHER: 3, WATER: 3, AIR: 3},
        "prestige": 3
    },
    {
        "requirements": {WATER: 4, ETHER: 4},
        "prestige": 3
    }
]

novice_spells = [
    {
        "tier": 1,
        "cost": {WATER: 4},
        "affinity": EARTH,
        "prestige": 1
    },
    {
        "tier": 1,
        "cost": {AIR: 2, FIRE: 2},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 2, ETHER: 1, EARTH: 2},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 3},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 2, WATER: 1, ETHER: 1, EARTH: 1},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, ETHER: 1, FIRE: 2, EARTH: 1},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, EARTH: 2},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 2, ETHER: 2, EARTH: 1},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 2, EARTH: 2},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 1, ETHER: 2, FIRE: 1, EARTH: 1},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 2, ETHER: 1},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 1, ETHER: 1, EARTH: 1},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, ETHER: 2, FIRE: 2},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {ETHER: 3},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 4},
        "affinity": FIRE,
        "prestige": 1
    },
    {
        "tier": 1,
        "cost": {FIRE: 4},
        "affinity": WATER,
        "prestige": 1
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 3, ETHER: 1},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {ETHER: 4},
        "affinity": AIR,
        "prestige": 1
    },
    {
        "tier": 1,
        "cost": {WATER: 1, ETHER: 1, FIRE: 1, EARTH: 1},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 2, WATER: 1},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 3, WATER: 1, EARTH: 1},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, ETHER: 1, FIRE: 1, EARTH: 1},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 1, ETHER: 3, FIRE: 1},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 2, FIRE: 2},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {FIRE: 3},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 1, FIRE: 2, EARTH: 2},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, FIRE: 1, EARTH: 3},
        "affinity": FIRE,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 2, WATER: 2, FIRE: 1},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {ETHER: 2, FIRE: 1},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {WATER: 3},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {FIRE: 2, EARTH: 2},
        "affinity": AIR,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 1, FIRE: 1, EARTH: 2},
        "affinity": ETHER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {ETHER: 1, FIRE: 3, EARTH: 1},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 2, ETHER: 1, FIRE: 1},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 1, ETHER: 1, FIRE: 1},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {EARTH: 3},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {ETHER: 2, EARTH: 2},
        "affinity": WATER,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {AIR: 2, ETHER: 2},
        "affinity": EARTH,
        "prestige": 0
    },
    {
        "tier": 1,
        "cost": {EARTH: 4},
        "affinity": ETHER,
        "prestige": 1
    },
    {
        "tier": 1,
        "cost": {AIR: 1, WATER: 1, FIRE: 1, EARTH: 1},
        "affinity": ETHER,
        "prestige": 0
    },
]