from django.db import models


class Product(models.Model):
    id = models.CharField(primary_key=True)
    name = models.CharField(max_length=55)
    value = models.FloatField()
    discount_value = models.FloatField()
    stock = models.IntegerField()


    @staticmethod
    def create_product(valid_data):
        try:
            Product.id = valid_data.get('id')
            Product.stock = valid_data.get('stock')
            Product.value = valid_data.get('value')
            Product.discount_value = valid_data.get('discount_value')
            Product.stock = valid_data.get('stock')
            return True, Product
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









