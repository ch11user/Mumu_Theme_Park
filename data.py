
# Available attraction categories
ALL_CATEGORIES = ["Shows", "Rides"]

# Available ticket types
TICKET_TYPES = ["Normal", "Express"]

# Theme park attractions
ATTRACTIONS = [

    {
        "name": "Minions Lights Camera Action",
        "category": ["Shows"],
        "description": "Minions movie show",
        "times": [10, 13, 16, 20]
    },

    {
        "name": "Dance for the Magic Beans",
        "category": ["Shows"],
        "description": "Dance performances by the Cat in the Hat and friends",
        "times": [11, 14, 17]
    },

    {
        "name": "Elmo's 4D Action Adventure",
        "category": ["Rides", "Shows"],
        "description": "Find the Cookie Monster with Elmo and friends",
        "times": [10, 13, 16],
        "wait": 45,
        "express_wait": 10
    },

    {
        "name": "Watershow",
        "category": ["Shows"],
        "description": "Waterland show with fireworks",
        "times": [12, 18]
    },

    {
        "name": "Cookie Monster Rollercoaster",
        "category": ["Rides"],
        "description": "Escape with the Cookie Monster",
        "wait": 45,
        "express_wait": 10
    },

    {
        "name": "Water Rapids",
        "category": ["Rides"],
        "description": "Exciting water ride with twists and drops",
        "wait": 30,
        "express_wait": 5
    },

    {
        "name": "Transformers 4D Ride",
        "category": ["Rides"],
        "description": "Exciting 4D ride with Transformers characters",
        "wait": 20,
        "express_wait": 0
    },

    {
        "name": "Nature Valley Buggy Ride",
        "category": ["Rides"],
        "description": "Buggy ride through the Grand Canyon",
        "wait": 50,
        "express_wait": 20
    }

]
