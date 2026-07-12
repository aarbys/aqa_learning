from api.generic_api import GenericApi



from models.product import Product
from api.api_result import ApiResult



class ProductApi:
    def __init__(self, generic_api: GenericApi):
        self.generic_api = generic_api
            
    def get_product_by_id(self, product_id: int) -> ApiResult[Product]:
        return self.generic_api.get_by_id(product_id)
    
    def get_all_products(self) -> ApiResult[list[Product]]:
        return self.generic_api.get_all()
    
    def create_product(self, product_data: dict) -> ApiResult[Product]:
        return self.generic_api.create(product_data)
