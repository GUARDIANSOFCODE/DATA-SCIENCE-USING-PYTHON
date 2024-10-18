import pytest
from unittest.mock import MagicMock
from order_processor import Inventory, DiscountCalculator, OrderProcessor

# Parameterized test to test multiple scenarios
@pytest.mark.parametrize("item, quantity, price, discount, stock, expected", [
    ("laptop", 2, 1000, 0.1, {"laptop": 10}, {"status": "success", "total_price": 1800}),
    ("laptop", 1, 500, 0.5, {"laptop": 5}, {"status": "success", "total_price": 250}),
    ("phone", 3, 300, 0.2, {"phone": 1}, {"status": "failed", "message": "Item out of stock"}),
    ("tablet", 1, 200, 1.5, {"tablet": 5}, {"status": "failed", "message": "Discount must be between 0 and 1."}),
])
def test_process_order(item, quantity, price, discount, stock, expected):
    # Arrange
    inventory = Inventory(stock)
    discount_calculator = DiscountCalculator()
    order_processor = OrderProcessor(inventory, discount_calculator)

    # Act
    result = order_processor.process_order(item, quantity, price, discount)

    # Assert
    assert result == expected

# Mock external dependencies to isolate the function being tested
def test_process_order_with_mock():
    # Arrange
    mock_inventory = MagicMock()
    mock_inventory.check_stock.return_value = True
    mock_discount_calculator = MagicMock()
    mock_discount_calculator.apply_discount.return_value = 900  # Mock discount

    order_processor = OrderProcessor(mock_inventory, mock_discount_calculator)

    # Act
    result = order_processor.process_order("laptop", 2, 1000, 0.1)

    # Assert
    assert result == {"status": "success", "total_price": 1800}

    # Verify the mocks were called with expected arguments
    mock_inventory.check_stock.assert_called_once_with("laptop", 2)
    mock_discount_calculator.apply_discount.assert_called_once_with(1000, 0.1)
