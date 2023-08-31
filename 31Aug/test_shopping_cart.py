from unittest.mock import Mock
from item_database import ItemDatabase
from shpping_cart import ShoppingCart
import pytest

@pytest.fixture
def cart():
    return ShoppingCart(3)

@pytest.fixture
def price_map():
    return {
    "apple":5.0,
    "mango":8.0,
    "banana":3.0,
    "orange":4.50
}

def test_can_add_item_to_cart(cart):
    cart.add("apple")
    # checking if its added
    assert cart.size() > 0

def test_when_item_added_then_cart_contains_item(cart):
    cart.add("banana")
    assert 'banana' in cart.get_items()

# test if the code fails
def test_when_add_more_than_max_items_should_fails(cart):
    cart.add("mango")
    cart.add("apple")
    cart.add("banana")
    # adding fourth item
    with pytest.raises(OverflowError):
        cart.add("orange")

def test_get_total_prices(cart,price_map):
    cart.add("mango")
    cart.add("apple")
    item_Databse = ItemDatabase()

    def mock_get_item(item:str):
        return price_map[item]
    
    item_Databse.get = Mock(side_effect=mock_get_item)

    assert cart.get_total_price(item_Databse) == 13 