from eapp.dao import load_products
from eapp.test.test_base import test_app, sample_products


def test_all(sample_products):
    actual_products = load_products()
    assert len(actual_products) == len(sample_products)

def test_find_with_page_size_equal_none(sample_products):
    actual_products = load_products(page=None)
    assert len(actual_products) == len(sample_products)

def test_find_with_page_size_not_none(test_app, sample_products):
    actual_products = load_products(page=-1)
    assert len(actual_products) == test_app.config["PAGE_SIZE"]
    actual_products = load_products(page=1)
    assert len(actual_products) == test_app.config["PAGE_SIZE"]
    actual_products = load_products(page=3)
    assert len(actual_products) == 1
    actual_products = load_products(page=4)
    assert len(actual_products) == 0

def test_find_with_kw(sample_products):
    actual_products = load_products(kw = 'ip 18')
    assert actual_products[0] == sample_products[1]
    actual_products = load_products(kw='')
    assert len(actual_products) == len(sample_products)
    actual_products = load_products(kw='1')
    assert len(actual_products) == 4
    actual_products = load_products(kw=1)
    assert len(actual_products) == 4
    actual_products = load_products(kw='abc')
    assert len(actual_products) == 0

def test_find_with_category_id(sample_products):
    actual_products = load_products(cate_id=None)
    assert len(actual_products) == len(sample_products)
    actual_products = load_products(cate_id=1)
    assert len(actual_products) == 1
    actual_products = load_products(cate_id=3)
    assert len(actual_products) == 2
    actual_products = load_products(cate_id=4)
    assert len(actual_products) == 1
    actual_products = load_products(cate_id=-1)
    assert len(actual_products) == 0
    actual_products = load_products(cate_id=5)
    assert len(actual_products) == 0
    actual_products = load_products(cate_id='abc')
    assert len(actual_products) == 0
    actual_products = load_products(cate_id=False)
    assert len(actual_products) == len(sample_products)
    actual_products = load_products(cate_id=0)
    assert len(actual_products) == len(sample_products)
    actual_products = load_products(cate_id=True)
    assert len(actual_products) == 1
