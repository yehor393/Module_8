import collections

Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])


def convert_list(cats):
    cat_dicts = []

    for cat in cats:
        if isinstance(cat, Cat):
            # If the element is already a Cat namedtuple, convert it to a dictionary
            cat_dict = {"nickname": cat.nickname,
                        "age": cat.age,
                        "owner": cat.owner}
            cat_dicts.append(cat_dict)
        elif isinstance(cat, dict):
            # If the element is a dictionary, convert it to a Cat namedtuple
            cat_namedtuple = Cat(**cat)
            cat_dicts.append(cat_namedtuple)

    return cat_dicts


# Example usage
cats_list = [
    Cat("Mick", 5, "Sara"),
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"}
]
converted_cats = convert_list(cats_list)
print(converted_cats)
