import pytest
from flask import Flask

from eapp import db
from eapp.models import Product
from eapp.index import register_routes

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["PAGE_SIZE"] = 2
    app.config["TESTING"] = True
    app.secret_key = "vibecode"
    db.init_app(app)
    register_routes(app=app)
    return app

@pytest.fixture
def test_client(test_app):
    return test_app.test_client()


@pytest.fixture
def test_app():
    app = create_app()

    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def test_session(test_app):
    yield db.session
    db.session.rollback()


@pytest.fixture
def sample_products(test_session):
    p1 = Product(name='ip 17', price=10, category_id=1)
    p2 = Product(name='ip 18 promax 10 terabyte', price=20, category_id=2)
    p3 = Product(name='samsung note 100', price=30, category_id=3)
    p4 = Product(name='redmi 17', price=40, category_id=4)
    p5 = Product(name='oppo neo 9', price=100, category_id=3)

    test_session.add_all([p1,p2,p3,p4,p5])
    test_session.commit()
    return [p1,p2,p3,p4,p5]

@pytest.fixture
def mock_cloudinary(monkeypatch):
    def fake_upload(file):
        return {'secure_url': 'https://fake_image.png'}

    monkeypatch.setattr('cloudinary.uploader.upload', fake_upload)