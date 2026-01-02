"""recipe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
#from django.conf.urls import url
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.first),
    path('index',views.index),

    path('cus_register',views.cus_register),
    path('login/',views.login),
    path('login/addlogin',views.addlogin),
    path('logout/',views.logout),
    path('dash',views.dash),

    path('staff_register',views.staff_register),
    path('view_staff',views.view_staff),
    path('removestaff/<int:id>',views.removestaff),
    path('view_cus',views.view_cus),
    path('removecustomer/<int:id>',views.removecustomer),

    path('staff_profile',views.staff_profile),
    path('cus_profile',views.cus_profile),
    path('add_category',views.add_category),
    path('add_subcategory',views.add_subcategory),
    path('view_category',views.view_category),
    path('remove_category/<int:category_id>/', views.remove_category, name='remove_category'),
    path('remove_pro_category/<int:category_id>/', views.remove_pro_category, name='remove_pro_category'),

    path('add_category_products',views.add_category_products),
    path('view_product_category',views.view_product_category),
    path('add_my_products',views.add_my_products),
    path('view_my_pro',views.view_my_pro),

    path('delete_my_pro/<int:id>',views.delete_my_pro),
    path('editpro/<int:id>',views.editpro),
    path('editpro/addeditpro/<int:id>',views.addeditpro),

    path('view_products',views.view_products),
    path('viewcart',views.viewcart),
    path('add_to_cart/<int:id>/',views.add_to_cart),
    path('update_qnty/<int:id>',views.update_qnty),
    path('remove_cart_item/<int:id>',views.remove_cart_item),

    path('add_cards',views.add_cards),
    path('view_cards',views.view_cards),
    path('checkout/<int:id>',views.checkout),
    path('checkout/add_payment/<int:id>',views.add_payment),

    path('courier_manage',views.courier_manage),
    path('add_courier',views.add_courier),
    path('edit_courier/<int:id>',views.edit_courier),
    path('edit_courier/edit_courier/<int:id>',views.edit_courier),
    path('remove_courier/<int:id>',views.remove_courier),
    path('courier_assign',views.courier_assign),
    path('assign_courier/<int:id>',views.assign_courier),



    path('courier_view_company',views.courier_view_company),
    path('accept_courier/<int:id>',views.accept_courier),
    path('reject_courier/<int:id>',views.reject_courier),
    path('removepro/<int:id>',views.removepro),
    path('delivery_update_company/<int:id>',views.delivery_update_company),   
    path('delivery_update_company/add_delivery_update_company',views.add_delivery_update_company),
    path('view_delivery_details',views.view_delivery_details),
    path('admin_sales_view',views.admin_sales_view),
    path('delivery_detail_admin/<int:id>',views.delivery_detail_admin),
    path('edititem/<int:id>',views.edititem),
    path('edititem/addedititem/<int:id>',views.addedititem),
    path('my_purchases',views.my_purchases),
    path('add_items',views.add_items),
    path('add_items_insert',views.add_items_insert),
    path('view_hom_pro',views.view_hom_pro),
    path('view_items_admin',views.view_items_admin),

    path('removeitem/<int:id>',views.removeitem),

    path('addrecipe/<int:id>',views.addrecipe),
    path('addrecipe/add_recipe_insert',views.add_recipe_insert),

    path('viewrecipe/<int:id>',views.viewrecipe, name='viewrecipe'),
    path('editrecipe/<int:id>',views.editrecipe),
    path('editrecipe/edit_recipe_insert/<int:id>',views.edit_recipe_insert),

    path('addingred/<int:id>',views.addingred),
    path('addingred/add_ing_insert',views.add_ing_insert),
    path('view_recipes',views.view_recipes),
    path('calculation',views.calculation),    
    path('search',views.search),    
    path('search2',views.search2),    
    path('search3',views.search3),    

    path('view_item_recipes/<int:id>',views.view_item_recipes),
    path('deactivepro/<int:id>',views.deactivepro),
    path('activepro/<int:id>',views.activepro),
    path('activestaff/<int:id>',views.activestaff),

    path('view_bill/<int:cart_master_id>/', views.view_bill),


    path('admin/', admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
