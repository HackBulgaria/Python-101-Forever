import json


attribute_path = "members[0].name"


def deep_get(example_dict, attribute_path):
    attribute_chain = attribute_path.split('.')

    try:
        current = get_attribute(example_dict, attribute_chain[0])
        for a in attribute_chain[1:]:
            current = get_attribute(current, a)
    except KeyError:
        print("Input not correct!")
        print(-1)
        return

    return current


def get_attribute(structure, attribute):
    if type(attribute) is int:
        return structure[attribute]
    if attribute.endswith(']'):
        index, attribute_name = extract_index_and_attribute(attribute)
        return get_attribute(get_attribute(structure, attribute_name), index)

    return structure[attribute]


def extract_index_and_attribute(attribute):
    index = attribute[-2:-1]
    attribute_name = attribute[:-3]
    return int(index), attribute_name


example_dict = json.loads("""{
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
}""")

example_dict_2 = json.loads("""{
  "items": [
    [[1]],
    [2]
  ]
}""")

print(deep_get(example_dict_2, "items[1][0]"))
