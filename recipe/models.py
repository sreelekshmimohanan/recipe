from django.db import models


class tbl_login(models.Model):
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    user_type=models.CharField(max_length=150)
    
class customer_reg(models.Model):
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    street=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)

class staff_reg(models.Model):
    fname=models.CharField(max_length=150)
    lname=models.CharField(max_length=150)
    district=models.CharField(max_length=150)
    street=models.CharField(max_length=150)
    phone=models.CharField(max_length=150)
    gender=models.CharField(max_length=150)
    dob=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    status=models.CharField(max_length=150)


class category(models.Model):
    category_name=models.CharField(max_length=150)

class subcategory(models.Model):
    subcat_name=models.CharField(max_length=150)
    category=models.ForeignKey(category, on_delete=models.CASCADE)


class product_category(models.Model):
    category_name=models.CharField(max_length=150)

class tbl_product(models.Model):
    customer=models.ForeignKey(customer_reg, on_delete=models.CASCADE)
    cat_id=models.CharField(max_length=150)
    item_name=models.CharField(max_length=150)
    item_desc=models.CharField(max_length=150)
    item_price=models.DecimalField(max_digits=10, decimal_places=2)
    item_status=models.CharField(max_length=150)
    item_stock = models.DecimalField(max_digits=10, decimal_places=2)
    item_image=models.FileField(max_length=150)

class cart_master(models.Model):
    customert_id=models.CharField(max_length=150)
    cart_tot_amt=models.DecimalField(max_digits=10, decimal_places=2)
    cart_status=models.CharField(max_length=150)

class cart_child(models.Model):
    cart_master_id=models.CharField(max_length=150)
    item_id=models.CharField(max_length=150)
    cart_qty=models.PositiveIntegerField()
    cart_price=models.DecimalField(max_digits=10, decimal_places=2)

class card(models.Model):
    customer = models.ForeignKey(customer_reg, on_delete=models.CASCADE)
    card_holder = models.CharField(max_length=150)
    card_no = models.CharField(max_length=150)
    exp_date = models.CharField(max_length=150)
    cvv = models.CharField(max_length=150)

class tbl_payment(models.Model):
    cart_master_id = models.CharField(max_length=150)
    card_id = models.CharField(max_length=150)
    pay_date = models.DateField(auto_now_add=True)  # Automatically adds the current date and time
    status = models.CharField(max_length=150)

class tbl_courier(models.Model):
    staff_id=models.CharField(max_length=150)
    co_name=models.CharField(max_length=150)
    co_city=models.CharField(max_length=150)
    co_dist=models.CharField(max_length=150)
    co_pin=models.CharField(max_length=150)
    co_street=models.CharField(max_length=150)
    co_phone=models.CharField(max_length=150)
    email=models.CharField(max_length=150)
    password=models.CharField(max_length=150)
    co_status=models.CharField(max_length=150)

class tbl_cassign(models.Model):
    courier_id=models.CharField(max_length=150)
    cassign_date=models.CharField(max_length=150)
    cart_master_id=models.CharField(max_length=150)
    status=models.CharField(max_length=150)

class tbl_delivery(models.Model):
    cassign_id=models.CharField(max_length=150)
    del_date=models.CharField(max_length=150)
    cart_master_id=models.CharField(max_length=150)

class tbl_item(models.Model):
    category=models.ForeignKey(category, on_delete=models.CASCADE)
    subcategory=models.ForeignKey(subcategory, on_delete=models.CASCADE)
    item_desc=models.CharField(max_length=500)
    item_name=models.CharField(max_length=150)
    item_status=models.CharField(max_length=150)
    recipe_status=models.CharField(max_length=150)
    item_image=models.FileField(max_length=150)

class tbl_recipes(models.Model):
    item=models.ForeignKey(tbl_item, on_delete=models.CASCADE)
    recipe_desc=models.CharField(max_length=1000)
    recipe_name=models.CharField(max_length=150)
    pre_time=models.CharField(max_length=150)
    cook_time=models.CharField(max_length=150)

class tbl_ingrediantcalc(models.Model):
    item=models.ForeignKey(tbl_item, on_delete=models.CASCADE)
    ing_unit=models.DecimalField(max_digits=10, decimal_places=2)
    ingrediant=models.CharField(max_length=150)