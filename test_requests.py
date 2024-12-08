import requests

url = "http://localhost:8001/get_form"

# Тест 1: Данные, которые подходят под шаблон MyForm
data = {
    "user_name": "Вова",
    "lead_email": "test@example.com",
    "order_date": "2020-05-20",
}
r = requests.post(url, data=data)
print("Test 1:", r.json())

# Тест 2: Данные, которые не подходят ни под один шаблон
data = {"random_field": "hello world", "another_field": "+70000000000"}
r = requests.post(url, data=data)
print("Test 2:", r.json())

# Тест 3: Данные для LeadForm
data = {
    "lead_phone": "+71234567890",
    "lead_email": "contact@company.com",
    "extra_field": "some text",
}
r = requests.post(url, data=data)
print("Test 3:", r.json())
