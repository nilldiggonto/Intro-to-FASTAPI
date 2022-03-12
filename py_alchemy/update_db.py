from test import User,Session,engine

local_session = Session(bind=engine)

user_update = local_session.query(User).filter(User.username=='ok2').first()

user_update.username = 'updateuser'
user_update.emain = 'updateemail@email.com'

local_session.commit()