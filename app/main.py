class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for i in people:
        new_person = Person(i["name"], i["age"])
        instances.append(new_person)

    for item in people:
        person = Person.people[item["name"]]

        if item.get("wife"):
            wife_name = item["wife"]
            person.wife = Person.people[wife_name]
        if item.get("husband"):
            husband_name = item["husband"]
            person.husband = Person.people[husband_name]

    return instances
