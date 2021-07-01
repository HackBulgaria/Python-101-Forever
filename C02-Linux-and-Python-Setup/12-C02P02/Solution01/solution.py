import json


example = """{
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "properties": {
      "foo": "bar"
  },
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": [
        "Radiation resistance",
        "Turning tiny",
        "Radiation blast"
      ]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
    {
      "name": "Eternal Flame",
      "age": 1000000,
      "secretIdentity": "Unknown",
      "powers": [
        "Immortality",
        "Heat Immunity",
        "Inferno",
        "Teleportation",
        "Interdimensional travel"
      ]
    }
  ]
}"""

example_2 = """{
  "items": [
    [[1], 3],
    [2]
  ]
}"""


def get_attribute(structure, attribute_name):
    if type(attribute_name) is int:
        return structure[attribute_name]

    if attribute_name.endswith(']'):
        attribute, index = get_attribute_and_index(attribute_name)
        return get_attribute(get_attribute(structure, attribute), index)

    return structure[attribute_name]


def get_attribute_and_index(attribute_name):
    # we should handle indexes greater than 9
    attribute = attribute_name[:-3]
    index = int(attribute_name[-2:-1])

    return attribute, index


def deep_get(structure, path):
    attribute_chain = path.split('.')

    try:
        current = get_attribute(structure, attribute_chain[0])
        for a in attribute_chain[1:]:
            current = get_attribute(current, a)
    except (IndexError, KeyError):
        print('Input not valid!')
        return -1

    return current


def gson(json_file, path):
    return deep_get(json.loads(json_file), path)


print(gson(example_2, 'items[0][1]'))
