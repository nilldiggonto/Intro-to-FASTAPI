from test import User,engine,Session

local_session = Session(bind=engine)

users = local_session.query(User).order_by(User.username).all()

for u in users:
    print(u.username)
    print('---')