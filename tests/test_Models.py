from sqlalchemy import select

from fast_zero.Models import User


def test_create_user(session):
    user = User(username='passi', email='passi@test.com', password='1234')

    session.add(user)
    session.commit()

    result = session.scalar(select(User).where(User.email == 'passi@test.com'))

    assert result.id == 1
