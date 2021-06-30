# C02P02 - gson

Implement a Python script called `gson.py` that reads 2 arguments:

- Path to a JSON file.
- Path inside the JSON file, which can describe properties & array indices.

The program should output:

- To stdout, the value given from the path. In case the program fails, it should exit with a non-zero status.
- To stderr, if the file is not a proper JSON or the path cannot be found in the JSON.

## Examples

Lets say we have the following `example.json` file:

```
$ cat example.json
```

which outputs ([taken from here](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON))

```json
{
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
}
```

Now, if we have our `gson.py` in the same directory, we should be able to run the following:

```
$ python gson.py example.json "members[0].name"
```

which outputs:

```
Molecule Man
```

Basically, the second argument describes a path in the JSON file.

Here are some more examples:

```
$ python gson.py example.json "members[0].powers[1]"
Turning tiny
```

```
$ python gson.py example.json "squadName"
Super hero squad
```

```
$ python gson.py example.json "properties"
{
    "foo": "bar"
}
```

```
$ python gson.py example.json "properties.foo"
bar
```

```
$ python gson.py example.json "shano.property"
Error: Property not found

$ echo $? 
1
```

We can even have more weird JSON formats:

```json
{
  "items": [
    [1],
    [2]
  ]
}
```

```
$ python gson.py weird.json "items[0]"
[1]

$ python gson.py weird.json "items[0][0]"
1
```

## Hints

- We are effectively trying to mimick <https://lodash.com/docs/4.17.15#get> or <https://pypi.org/project/python-benedict/>.
- Use <https://docs.python.org/3/library/json.html> to read & parse the JSON file.
- Use `sys.argv` to read the arguments.
