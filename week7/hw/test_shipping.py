from shipping import calculate_shipping_cost  # Replace 'your_module' with the actual module name

# Test Case 1: Valid weight, delivery, and discount
def test_valid_weight_delivery_discount_LOYALTY10():
    assert calculate_shipping_cost(3, 'standard', 'LOYALTY10') == 13.5

# Test Case 2: Valid weight, delivery, and discount
def test_valid_weight_delivery_discount_LOYALTY20():
    assert calculate_shipping_cost(10, 'express', 'LOYALTY20') == 28

# Test Case 3: Valid weight, delivery, and free shipping
def test_valid_weight_delivery_free_shipping():
    assert calculate_shipping_cost(25, 'overnight', 'FREESHIP') == 0

# Test Case 4: Valid weight and delivery, no discount
def test_valid_weight_delivery_no_discount():
    assert calculate_shipping_cost(5, 'standard', 'NONE') == 15

# Test Case 5: Valid weight and delivery, empty discount
def test_valid_weight_delivery_empty_discount():
    assert calculate_shipping_cost(15, 'express', '') == None

# Test Case 6: Negative weight
def test_negative_weight():
    assert calculate_shipping_cost(-5, 'standard', 'LOYALTY10') is None

# Test Case 7: Zero weight
def test_zero_weight():
    assert calculate_shipping_cost(0, 'express', 'LOYALTY20') is None

# Test Case 8: Invalid delivery type
def test_invalid_delivery_type():
    assert calculate_shipping_cost(10, 'fast', 'LOYALTY10') is None

# Test Case 9: Empty delivery type
def test_empty_delivery_type():
    assert calculate_shipping_cost(20, '', 'FREESHIP') is None

# Test Case 10: None delivery type
def test_none_delivery_type():
    assert calculate_shipping_cost(7, None, 'LOYALTY20') is None

# Test Case 11: Invalid discount code
def test_invalid_discount_code_DISCOUNT50():
    assert calculate_shipping_cost(12, 'standard', 'DISCOUNT50') is None

# Test Case 12: Invalid discount code XYZ
def test_invalid_discount_code_XYZ():
    assert calculate_shipping_cost(18, 'overnight', 'XYZ') is None

# Test Case 13: Empty discount code
def test_empty_discount_code():
    assert calculate_shipping_cost(5, 'express', ' ') is None

# Test Case 14: Exact 5 kg weight, standard delivery, no discount
def test_exact_5kg_standard_no_discount():
    assert calculate_shipping_cost(5, 'standard', 'NONE') == 15

# Test Case 15: Just over 5 kg, express delivery, no discount
def test_just_over_5kg_express_no_discount():
    assert calculate_shipping_cost(5.1, 'express', 'NONE') == 35

# Test Case 16: Exact 20 kg weight, overnight delivery, no discount
def test_exact_20kg_overnight_no_discount():
    assert calculate_shipping_cost(20, 'overnight', 'NONE') == 75

# Test Case 17: Just over 20 kg, standard delivery, no discount
def test_just_over_20kg_standard_no_discount():
    assert calculate_shipping_cost(20.1, 'standard', 'NONE') == 55

# Test Case 18: Medium weight, express delivery, LOYALTY10 discount
def test_medium_weight_express_LOYALTY10_discount():
    assert calculate_shipping_cost(10, 'express', 'LOYALTY10') == 31.5

# Test Case 19: High weight, overnight delivery, LOYALTY20 discount
def test_high_weight_overnight_LOYALTY20_discount():
    assert calculate_shipping_cost(30, 'overnight', 'LOYALTY20') == 60

# Test Case 20: Low weight, standard delivery, FREESHIP discount
def test_low_weight_standard_FREESHIP_discount():
    assert calculate_shipping_cost(2, 'standard', 'FREESHIP') == 0

# Test Case 21: High weight, express delivery, empty discount
def test_high_weight_express_empty_discount():
    assert calculate_shipping_cost(22, 'express', '') == None

# Test Case 22: Medium weight, standard delivery, non-existent discount
def test_medium_weight_standard_non_existent_discount():
    assert calculate_shipping_cost(15, 'standard', 'NONEXISTENT') is None

# Test Case 23: Very high weight, overnight delivery, no discount
def test_very_high_weight_overnight_no_discount():
    assert calculate_shipping_cost(50, 'overnight', 'NONE') == 75
