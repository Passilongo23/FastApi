from sqlalchemy import Select

from fast_zero.Models import User


def test_create_user(session):
    new_user = User(
        username='alice',
        email='test@test.com',
        password='password',
    )
    session.add(new_user)
    session.commit()
    result = session.scalar(Select(User).where(User.email == 'test@test.com'))

    assert result.username == 'alice'
