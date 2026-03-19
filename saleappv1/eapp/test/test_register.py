import hashlib

import pytest

from eapp.dao import add_user
from eapp.models import User
from eapp.test.test_base import test_session, test_app, mock_cloudinary

def test_success(test_app,test_session):
    add_user(username='a'*6, password='1a'*4, name='admin', avatar=None)
    u = User.query.filter(User.username.__eq__('a'*6)).first()

    assert u is not None
    assert u.name == 'admin'
    assert u.password == str(hashlib.md5(("1a"*4).encode('utf-8')).hexdigest())
    assert u.active == True


@pytest.mark.parametrize('password', [
    '1234567', '12345678', 'abcdefgh'
])
def test_invalid_password(password):
    with pytest.raises(ValueError):
        add_user(username='a' * 6, password=password, name='admin', avatar=None)

def test_upload_avatar(test_session, mock_cloudinary):
    add_user(username='a' * 6, password='1a' * 4, name='admin', avatar='abc')
    u = User.query.filter(User.username.__eq__('a' * 6)).first()
    assert u.avatar == 'https://fake_image.png'

def test_existing_username(test_session, mock_cloudinary):
    add_user(username='a' * 6, password='1a' * 4, name='admin', avatar='abc')
    with pytest.raises(ValueError):
        add_user(username='a' * 6, password='1a' * 4, name='admin', avatar='abc')