from test import User,Session,engine

user_dict = [
    {
        "username":"ok5",
        "email":"ok5@gmail.com"
    },
    {
        "username":"ok6",
        "email":"ok6@gmail.com"
    },
    {
        "username":"ok7",
        "email":"ok7@gmail.com"
    }
]

local_session = Session(bind=engine)

for u in user_dict:
    new_user = User(username=u['username'],email=u['email'])
    local_session.add(new_user)
    local_session.commit()


# new_user = User(username='diggonto',email="dig@dig.com")

# local_session.add(new_user)
# local_session.commit()