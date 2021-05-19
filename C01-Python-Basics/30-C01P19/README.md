# C01P19 - Stranger forms

Ivan and his friends love going to the cinema (that's pre-pandemic).

But when it comes to picking seats, they don't like the usual & boring "next to each other in one row" placement.

That's why they always pick their seats in a strange way:

- Maria should be above Ivan.
- Georgi should be to the right of Maria.
- Veronika should be above Maria.

And when they are done, they can take really strange forms (at least, strange in the eyes of the cinema owners).

Here's a way they can be placed, using the description above:

```
...*..V.*****..
..*..*MG..*.*..
....*.I...*....
```

Where:

* `.` represents an empty seat.
* `*` represents a reserved seat.
* `I`, `M`, `G` and `V` are the first letters of the respective people.

## The task

Implement the following function:

```python
def stranger_forms(cinema_layout, friends_configuration):
    pass
```

You'll be given 2 arguments:

- The cinema layout
- The configuration our friends want to take.

The function should return a list of **all possible placements**, that satisfy the given form. This is basically a list of possible cinema layouts (structure the layouts the same way as the input)

Possible placement is a configuration where:

* Our friends can book seats in the way they want.
* They are not going outside of the cinema.
* They are not taking any already reserved seats.

The cinema layout will be structured as list of strings:

```python
['..*...*.**',
 '.....**...',
 '*.*...*..*',
 '.**....*.*',
 '...*..*.*.',
 '.***...*..',
 '*......*.*',
 '.....**..*',
 '..*.*.*..*',
 '***.*.**..']
```

Friends configuration will also be given as a list of strings:

```python
["A", "BAA", "FRA", "CAB", "DRC", "EAD", "GLE"]
```

Lets break it down:

* `A` - that's the first letter of the name of someone, who is going to be "central" for the configuration.
* `BAA` - means - person with name `B` will be `Above` the person with name `A`.
* `FRA` - means - person with name `F` will be `Right` of the person with name `A`.
* `CAB` - means - person with name `C` will be `Above` the person with name `B`.
* `DRC` - means - person with name `D` will be `Right` of person with name `C`.
* `EAD` - means - person with name `E` will be `Above` the person with name `D`.
* `GLE` means - person with name `G` will be `Left` of the person with name `E`.

Few things to consider:

* The input will be correct - there won't be 2 people occupying the same place.
* All names are going to be unique.
* There won't be a configuration for someone not being previously introduced.

## Examples

If we take the input from above, here're all the possible configurations:

```
..*GE.*.**
...CD**...
*.*B..*..*
.**AF..*.*
...*..*.*.
.***...*..
*......*.*
.....**..*
..*.*.*..*
***.*.**..
```

```
..*...*.**
.....**...
*.*.GE*..*
.**.CD.*.*
...*B.*.*.
.***AF.*..
*......*.*
.....**..*
..*.*.*..*
***.*.**..
```

```
..*...*.**
.....**...
*.*...*..*
.**.GE.*.*
...*CD*.*.
.***B..*..
*...AF.*.*
.....**..*
..*.*.*..*
***.*.**..
```
