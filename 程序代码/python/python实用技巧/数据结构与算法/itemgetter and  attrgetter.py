from operator import attrgetter,itemgetter
from pprint import pprint

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return 'User({})'.format(self.user_id)
users = [User(23), User(3), User(99)]

# itemgetter(key) 相当于 lambda x:x[key]
pprint(sorted(rows,key=itemgetter("lname")))
# attrgetter(key) 相当于  lambda x:x.getter(key)
print(sorted(users, key=attrgetter("user_id")))