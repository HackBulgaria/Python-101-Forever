# C01P15 - Gas stations

We are implementing a smart GPS software.

-   We are taking a long trip from Sofia to Bourgas and we know the distance between the two cities. It is a positive integer and we mark it as `distance`.
-   We know how much our car can ride with a full tank of gas. It is a positive integer in kilometers. We mark it as `tank_size`.
-   We have a list of gas stations. We know the distance between Sofia and the current gas station. `stations = [50, 80, 110, 180, 220, 290]` Notice, the list is sorted!

By using this information we will implement a function that returns the shortest `list` of gas stations that we have to visit in order to travel from Sofia to Bourgas. We allways start with a full `tank_size`!

Something important:

1. If there's a gas station in `50km` and you have `50l`, you cannot reach that gas station. You'll need `51l` in the tank.
1. If you cannot reach the destination, return an empty list.

**Signature**

```python
def gas_stations(distance, tank_size, stations):
    pass
```

**Examples**

```python
gas_stations(320, 90, [50, 80, 140, 180, 220, 290]) == [80, 140, 220, 290]
gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]) == [70, 140, 210, 280, 350]
gas_stations(100, 50, [10, 20, 30, 40, 50, 60, 70, 80, 90, 150]) == [40, 80]
gas_stations(100, 50, [10, 90]) == []
```
