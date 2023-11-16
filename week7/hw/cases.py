import pandas as pd
# Updating the test cases with the calculated expected outputs
test_cases_updated = [
    {"Case No": 1, "Purpose": "Valid weight, delivery, and discount", "Input": "3, 'standard', 'LOYALTY10'", "Output": "", "Expected Output": "13.5"},
    {"Case No": 2, "Purpose": "Valid weight, delivery, and discount", "Input": "10, 'express', 'LOYALTY20'", "Output": "", "Expected Output": "28"},
    {"Case No": 3, "Purpose": "Valid weight, delivery, and free shipping", "Input": "25, 'overnight', 'FREESHIP'", "Output": "", "Expected Output": "0"},
    {"Case No": 4, "Purpose": "Valid weight and delivery, no discount", "Input": "5, 'standard', None", "Output": "", "Expected Output": "15"},
    {"Case No": 5, "Purpose": "Valid weight and delivery, empty discount", "Input": "15, 'express', ''", "Output": "", "Expected Output": "35"},
    {"Case No": 6, "Purpose": "Negative weight", "Input": "-5, 'standard', 'LOYALTY10'", "Output": "", "Expected Output": "None"},
    {"Case No": 7, "Purpose": "Zero weight", "Input": "0, 'express', 'LOYALTY20'", "Output": "", "Expected Output": "None"},
    {"Case No": 8, "Purpose": "Invalid delivery type", "Input": "10, 'fast', 'LOYALTY10'", "Output": "", "Expected Output": "None"},
    {"Case No": 9, "Purpose": "Empty delivery type", "Input": "20, '', 'FREESHIP'", "Output": "", "Expected Output": "None"},
    {"Case No": 10, "Purpose": "None delivery type", "Input": "7, None, 'LOYALTY20'", "Output": "", "Expected Output": "None"},
    {"Case No": 11, "Purpose": "Invalid discount code", "Input": "12, 'standard', 'DISCOUNT50'", "Output": "", "Expected Output": "None"},
    {"Case No": 12, "Purpose": "Invalid discount code", "Input": "18, 'overnight', 'XYZ'", "Output": "", "Expected Output": "None"},
    {"Case No": 13, "Purpose": "Empty discount code", "Input": "5, 'express', ' '", "Output": "", "Expected Output": "None"},
    {"Case No": 14, "Purpose": "Exact 5 kg weight, standard delivery, no discount", "Input": "5, 'standard', None", "Output": "", "Expected Output": "15"},
    {"Case No": 15, "Purpose": "Just over 5 kg, express delivery, no discount", "Input": "5.1, 'express', None", "Output": "", "Expected Output": "35"},
    {"Case No": 16, "Purpose": "Exact 20 kg weight, overnight delivery, no discount", "Input": "20, 'overnight', None", "Output": "", "Expected Output": "75"},
    {"Case No": 17, "Purpose": "Just over 20 kg, standard delivery, no discount", "Input": "20.1, 'standard', None", "Output": "", "Expected Output": "55"},
    {"Case No": 18, "Purpose": "Medium weight, express delivery, LOYALTY10 discount", "Input": "10, 'express', 'LOYALTY10'", "Output": "", "Expected Output": "31.5"},
    {"Case No": 19, "Purpose": "High weight, overnight delivery, LOYALTY20 discount", "Input": "30, 'overnight', 'LOYALTY20'", "Output": "", "Expected Output": "60"},
    {"Case No": 20, "Purpose": "Low weight, standard delivery, FREESHIP discount", "Input": "2, 'standard', 'FREESHIP'", "Output": "", "Expected Output": "0"},
    {"Case No": 21, "Purpose": "High weight, express delivery, empty discount", "Input": "22, 'express', ''", "Output": "", "Expected Output": "65"},
    {"Case No": 22, "Purpose": "Medium weight, standard delivery, non-existent discount", "Input": "15, 'standard', 'NONEXISTENT'", "Output": "", "Expected Output": "None"},
    {"Case No": 23, "Purpose": "Very high weight, overnight delivery, no discount", "Input": "50, 'overnight', None", "Output": "", "Expected Output": "75"}

]

# Convert to DataFrame
df_test_cases_updated = pd.DataFrame(test_cases_updated)

# Save to a CSV file
csv_file_path_updated = 'shipping_cases.csv'
df_test_cases_updated.to_csv(csv_file_path_updated, index=False)

