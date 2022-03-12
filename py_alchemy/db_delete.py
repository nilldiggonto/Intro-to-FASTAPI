from test import User,Session,engine

local_session = Session(bind=engine)

user_delete = local_session.query(User).filter(User.username== 'ok7').first()

local_session.delete(user_delete)

local_session.commit()