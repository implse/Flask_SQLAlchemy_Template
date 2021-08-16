from template_SQLAlchemy import db, Musicien


# Query all the users from User model
quartet = Musicien.query.all()

# Loop through all the users
for musicien in quartet:
    print(musicien)

# Get a user by id
drums = Musicien.query.get(1)
double_bass = Musicien.query.get(2)
alto_saxophone = Musicien.query.get(3)
piano = Musicien.query.get(4)

print(drums)
print(double_bass)
print(alto_saxophone)
print(piano)


