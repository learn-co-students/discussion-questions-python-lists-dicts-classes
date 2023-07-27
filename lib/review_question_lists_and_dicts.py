## QUESTION 1

pokemon = [
    {
        "id": 1,
        "name": "bulbasaur",
        "base_experience": 64,
        "height": 7,
        "is_default": True,
        "order": 1,
        "weight": 69,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "chlorophyll",
                    "url": "http://pokeapi.co/api/v2/ability/34/",
                },
            }
        ],
    },
    {
        "id": 3,
        "name": "venesaur",
        "base_experience": 50,
        "height": 10,
        "is_default": True,
        "order": 1,
        "weight": 90,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "fire",
                    "url": "http://pokeapi.co/api/v2/ability/38/",
                },
            }
        ],
    },
    {
        "id": 2,
        "name": "pikachu",
        "base_experience": 60,
        "height": 4,
        "is_default": True,
        "order": 1,
        "weight": 37,
        "abilities": [
            {
                "is_hidden": True,
                "slot": 3,
                "ability": {
                    "name": "lightning",
                    "url": "http://pokeapi.co/api/v2/ability/30/",
                },
            }
        ],
    },
]

if __name__ == "__main__":
    # How would you get the url for Bulbasaur's ability?
    print(
        [p for p in pokemon if p["name"] == "bulbasaur"][0]["abilities"][0]["ability"][
            "url"
        ]
    )
    # How would you return the first pokemon with base experience over 40?
    print(
        [p for p in pokemon if p["base_experience"] > 40][0]
    )  # list comp working like find
    # How would you return ALL OF THE pokemon with base experience over 40? (Gotta catch em all)
    print(
        [p for p in pokemon if p["base_experience"] > 40]
    )  # list comp working like filter
    # How would you return an array of all of the pokemon's names?
    print([poke["name"] for poke in pokemon])  # list comp working like map
    # How would you determine whether or not the pokemon array contained any pokemon with a weight greater than 60?
    # Whatever method you use should return True if there are any such pokemon, False if not.
    print(len([p for p in pokemon if p["weight"] > 60]) > 0)  # check list method .any()
