BIG_CONSTANT = "YES"


def group_by(xs, grouper):
    groups = {}

    for x in xs:
        group = grouper(x)

        if group not in groups:
            groups[group] = []

        groups[group].append(x)

    return groups


print(group_by([1, 2, 3, 4, 5, 6], lambda x: "even" if x % 2 == 0 else "odd"))
