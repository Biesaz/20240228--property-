# class Person:
#     def __init__(self, name: str) -> None:
#         self._name = name

#     @property
#     def name(self) -> str:
#         return self._name

#     @name.setter
#     def name(self, new_name: str) -> None:
#         self._name = new_name

#     @name.deleter
#     def name(self):
#         del self._name


# class PersonOne(Person):
#     def __init__(self, name: str) -> None:
#         super().__init__(name)

#     @property
#     def name(self):
#         return super().name


# # person_1 = Person(name="Saulius")

# # print(person_1.name)

# # del person_1.name

# # person_1.name = "Mindaugas"

# # print(person_1.name)

# person_2 = PersonOne(name="Vilius")

# print(person_2.name)

# person_2.name = "Mykolas"

######################
# offtopik
#
# print("""1
# 2
# 3
# 4
# 5
# """)
######################