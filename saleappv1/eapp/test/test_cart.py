from eapp.test.test_base import test_client, test_app

def test_add_to_cart(test_client):
    res = test_client.post("/api/carts", json={
        'id': 1,
        'name': 'abcxyz',
        'price': 100
    })

    assert res.status_code == 200

    data = res.get_json()

    assert data["total_quantity"] == 1
    assert data["total_amount"] == 100


def test_add_increase_item(test_client):
    test_client.post("/api/carts", json={
        'id': 1,
        'name': 'abcxyz',
        'price': 100
    })
    test_client.post("/api/carts", json={
        'id': 1,
        'name': 'abcxyz',
        'price': 100
    })
    res = test_client.post("/api/carts", json={
        'id': 2,
        'name': 'xyzabc',
        'price': 100
    })

    data = res.get_json()

    assert data["total_quantity"] == 3
    assert data["total_amount"] == 300

    with test_client.session_transaction() as ses:
        assert 'cart' in ses
        assert len(ses['cart']) == 2
        assert  ses['cart']['1']['quantity'] == 2


def test_add_existing(test_client):
    with test_client.session_transaction() as ses:
       ses['cart'] = {
           "2": {
               "id": 2,
               "name": "aaaa",
               "price": 500,
               "quantity": 2
           }
       }
    res = test_client.post("/api/carts", json={
       'id': 1,
       'name': 'abcxyz',
       'price': -1000
    })

    res = test_client.post("/api/carts", json={
        'name': 'abcxyz',
        'price': 1000
    })

    res = test_client.post("/api/carts", json={
        'id': 10,
        'price': 1000,
        'tag': 'bca'
    })

    res = test_client.post("/api/carts", json={
        'id': -1,
        'name': 'abcxyz',
        'price': 1000
    })

    data = res.get_json()

    assert data["total_amount"] == 3000
    assert data["total_quantity"] == 6

    with test_client.session_transaction() as ses:
        assert 'cart' in ses
        assert len(ses['cart']) == 5
        assert  ses['cart']['-1']['quantity'] == 1