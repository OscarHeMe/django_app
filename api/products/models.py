from django.db import models


class Product(models.Model):
    id = models.CharField(primary_key=True, max_length=200)
    name = models.CharField(max_length=55)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()


    @staticmethod
    def create_product(valid_data):
        try:
            product = Product()
            product.id = valid_data.get('id')
            product.name = valid_data.get('name')
            product.value = valid_data.get('value')
            product.discount_value = valid_data.get('discount_value')
            product.stock = valid_data.get('stock')
            return True, product
        except Exception as e:
            error_message = str(e)
            return False, error_message

    def validate(self):
        error_fileds = []
        if len(self.name) < 3:
            error_fileds.append('name')
        if self.value <= 0 or self.value > 99999.9:
            error_fileds.append('value')
        if self.discount_value and self.value < self.discount_value:
            error_fileds.append('discount_value')
        if self.stock <= -1:
            error_fileds.append('stock')
        if error_fileds:
            return False, error_fileds
        return True, error_fileds


    @staticmethod
    def bulk_insert(products):
        valid_products = []
        error_products = []
        for product in products:
            try:
                is_created, product_model = Product.create_product(product)
                if is_created:
                    valid_products.append(product_model)
                    is_valid, error_fileds = product_model.validate()
                    if is_valid:
                        valid_products.append(product_model)
                    else:
                        error_dict = {
                            'product_id': product.get('id'),
                            'errors': error_fileds
                        }
                        error_products.append(error_dict)
                else:
                    error_dict = {
                        'product_id': product.get('id'),
                        'errors': [product_model]
                    }
                    error_products.append(error_dict)
            except Exception as e:
                error_msg = str(e)
                error_dict = {
                    'product_id': product.get('id'),
                    'errors': [error_msg]
                }
                error_products.append(error_dict) 
        for product_model in valid_products:   
            try:
                product_model.save()
            except Exception as e:
                error_msg = str(e)
                error_dict = {
                    'product_id': product_model.id,
                    'errors': [error_msg]
                }
                error_products.append(error_dict)

        if len(error_products) > 0:
            return False, error_products
        return True, error_products


        









