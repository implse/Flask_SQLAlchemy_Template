from template_SQLAlchemy import db, User


# Query all the users from User model
users = User.query.all()

# Loop through all the users
for user in users:
    print(user.username, user.email)


# Get a user by id
drums = User.query.get(1)
double_bass = User.query.get(2)
alto_saxophone = User.query.get(3)
piano = User.query.get(4)

print(drums)
print(double_bass)
print(alto_saxophone)
print(piano)