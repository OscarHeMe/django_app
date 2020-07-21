# django_app
Django API

# Contracts

## Get products

```
curl --location --request GET 'http://127.0.0.1:8000/products'
```

## Insert products

```
curl --location --request POST 'http://127.0.0.1:8000/products/bulk_insert' \
--header 'Content-Type: application/json' \
--data-raw '{
    "products": [
        {
            "id": "23",
            "name": "Test Product",
            "value": 50.5,
            "discount_value": 5.5,
            "stock": 0
        },
        {
            "id": "24",
            "name": "Test Prod 2",
            "value": 90.5,
            "discount_value": 45.5,
            "stock": 2
        }
    ]
}'
```