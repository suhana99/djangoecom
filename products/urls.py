from django.urls import path
# from .views import test
# from .import test 
from .views import *

urlpatterns = [
#     path('demo/',test),
#     path('me/', me),
    path('',index),
    path('addproduct/',post_product),
    path('updateproduct/<int:product_id>',update_product),
    path('deleteproduct/<int:product_id>',delete_product),
    path('addcategory/',post_category),
    path('categories/',show_category),
    path('updatecategory/<int:category_id>',update_category),
    path('deletecategory/<int:category_id>',delete_category),
]