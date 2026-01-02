from django.http import HttpResponse,HttpResponseRedirect,HttpResponseNotAllowed
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from urllib.parse import urlencode
from .models import *
from django.db.models import Q
from django.db.models import Sum
from decimal import Decimal

def first(request):
    return render(request,'index.html')

def index(request):
    return render(request,'index.html')

def cus_register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        district=request.POST.get('district')
        street=request.POST.get('street')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if tbl_login.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'cus_register.html', {'msg': 'Email already exists. Please use a different email.'})
       
        cus=customer_reg(fname=fname,lname=lname,district=district,street=street,phone=phone,gender=gender,dob=dob,email=email,password=password)
        cus.save()
        cus1= tbl_login(email=email,password=password,user_type='customer')
        cus1.save()
        return render(request,"index.html", {'message':'Succesfully Registered'})
    else:
        return render(request,"cus_register.html")
    
def login(request):
    return render(request,'login.html')

def addlogin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == 'admin@gmail.com' and password =='admin':
        request.session['logintdetail'] = email
        request.session['admin'] = 'admin'
        return redirect(dash)
    elif customer_reg.objects.filter(email=email, password=password).exists():
        userdetails = customer_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['cuid'] = userdetails.id
            request.session['cuname'] = userdetails.fname
            request.session['cuemail'] = email

            return redirect(index)
        
    elif staff_reg.objects.filter(email=email,password=password,status='Active').exists():
        userdetails=staff_reg.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['sid'] = userdetails.id
            request.session['sname'] = userdetails.fname
            request.session['semail'] = email

            return redirect(dash)
        
    elif tbl_courier.objects.filter(email=email,password=password).exists():
        userdetails=tbl_courier.objects.get(email=request.POST['email'], password=password)
        if userdetails.password == request.POST['password']:
            request.session['coid'] = userdetails.id
            request.session['coname'] = userdetails.co_name
            request.session['coemail'] = email

            return redirect(dash)
   
    else:
        return render(request, 'login.html', {'message':'Invalid Email or Password'})
    
def logout(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return redirect(first)

#Admin
def dash(request):
    return render(request,'admin/index.html')

def staff_register(request):
    if request.method=="POST":
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        district=request.POST.get('district')
        street=request.POST.get('street')
        phone=request.POST.get('phone')
        gender=request.POST.get('gender')
        dob=request.POST.get('dob')
        email=request.POST.get('email')
        password=request.POST.get('password')
        if tbl_login.objects.filter(email=email).exists():
                 # Email already exists, display an alert message
            return render(request, 'admin/addstaff.html', {'msg': 'Email already exists. Please use a different email.'})

       
        cus=staff_reg(fname=fname,lname=lname,district=district,street=street,phone=phone,gender=gender,dob=dob,email=email,password=password,status='Active')
        cus.save()
        cus1= tbl_login(email=email,password=password,user_type='staff')
        cus1.save()
        return render(request,"admin/index.html", {'message':'Succesfully Registered'})
    else:
        return render(request,"admin/addstaff.html")
    
def view_staff(request):
    staff=staff_reg.objects.all()
    return render(request,'admin/viewstaff.html',{'result':staff})


def removestaff(request,id):
    recipe_detail = get_object_or_404(staff_reg, id=id)
    recipe_detail.status = 'Deactive'
    recipe_detail.save()
    return redirect(view_staff)
def activestaff(request,id):
    recipe_detail = get_object_or_404(staff_reg, id=id)
    recipe_detail.status = 'Active'
    recipe_detail.save()
    return redirect(view_staff)

def view_cus(request):
    staff=customer_reg.objects.all()
    return render(request,'admin/viewcustomer.html',{'result':staff})


def removecustomer(request,id):
    staff=customer_reg.objects.get(id=id)
    staff.delete()
    return redirect(view_cus)

def add_category(request):
    if request.method=="POST":
        category_name=request.POST.get('category_name')
        
        cus=category(category_name=category_name)
        cus.save()
        cat=category.objects.all()
        return render(request,"admin/addcategory.html", {'msg':'Succesfully Added','result':cat})
    else:
        cat=category.objects.all()
        return render(request,"admin/addcategory.html",{'result':cat})
    
def add_subcategory(request):   
    if request.method=="POST":
        subcat_name=request.POST.get('subcat_name')
        cat_id=request.POST.get('cat_id')
        
        cus=subcategory(subcat_name=subcat_name,category_id=cat_id)
        cus.save()
        cat=category.objects.all()
    return render(request,"admin/index.html", {'message':'Succesfully Added','result':cat})

def view_category(request):
    categories=category.objects.all()
    return render(request,'admin/view_category.html',{'categories':categories})

def remove_category(request, category_id):
    categoryy = get_object_or_404(category, pk=category_id) 
    # Delete associated subcategories
    subcategory.objects.filter(category=categoryy).delete()
    # Delete the category
    categoryy.delete()
    return redirect(view_category) 


def add_category_products(request):
    if request.method=="POST":
        category_name=request.POST.get('category_name')
        
        cus=product_category(category_name=category_name)
        cus.save()
        return redirect(view_product_category)
    else:
        return render(request,"admin/add_category_products.html")

def view_product_category(request):
    categories=product_category.objects.all()
    return render(request,'admin/view_product_category.html',{'categories':categories})
def remove_pro_category(request, category_id):
    categoryy = get_object_or_404(product_category, pk=category_id) 
    categoryy.delete()
    return redirect(view_product_category) 


def courier_manage(request):
    if request.method=="POST":
        co_name=request.POST.get('co_name')
        co_city=request.POST.get('co_city')
        co_dist=request.POST.get('co_dist')
        co_pin=request.POST.get('co_pin')
        co_street=request.POST.get('co_street')
        co_phone=request.POST.get('co_phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        staff_id = request.session.get('sid', 'admin')
        if customer_reg.objects.filter(email=email).exists() or staff_reg.objects.filter(email=email).exists() or tbl_courier.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'admin/add_courier.html', {'msg': 'Email already exists. Please use a different email.'})

        cus=tbl_courier(staff_id=staff_id,co_name=co_name,co_city=co_city,co_dist=co_dist,co_pin=co_pin,co_street=co_street,co_phone=co_phone,email=email,password=password,co_status='Active')
        cus.save()
        cus1= tbl_login(email=email,password=password,user_type='courier')
        cus1.save()
        cat=tbl_courier.objects.all()
        return render(request,"admin/courier.html", {'msg':'Succesfully Added','result':cat})
    else:
        cat=tbl_courier.objects.all()
        return render(request,"admin/courier.html",{'result':cat})
    
def add_courier(request):
    return render(request,'admin/add_courier.html')

def edit_courier(request,id):
    if request.method=="POST":
        co_name=request.POST.get('co_name')
        co_city=request.POST.get('co_city')
        co_dist=request.POST.get('co_dist')
        co_pin=request.POST.get('co_pin')
        co_street=request.POST.get('co_street')
        co_phone=request.POST.get('co_phone')
        email=request.POST.get('email')
        password=request.POST.get('password')
        co_status=request.POST.get('co_status')
        staff_id = request.session.get('sid', 'admin')
        if customer_reg.objects.filter(email=email).exists() or staff_reg.objects.filter(email=email).exists():
            # Email already exists, display an alert message
            return render(request, 'admin/add_courier.html', {'msg': 'Email already exists. Please use a different email.'})

        cus=tbl_courier(staff_id=staff_id,co_name=co_name,co_city=co_city,co_dist=co_dist,co_pin=co_pin,co_street=co_street,co_phone=co_phone,email=email,password=password,co_status=co_status,id=id)
        cus.save()
        return redirect(courier_manage)
    else:
        cou=tbl_courier.objects.get(id=id)
        return render(request,'admin/edit_courier.html',{'result':cou})
    
def remove_courier(request,id):
    co_detail = get_object_or_404(tbl_courier, id=id)
    co_detail.delete()
    return redirect(courier_manage)



def admin_sales_view(request):
    # Fetch all payment details
    payment_details = tbl_payment.objects.all()

    # Initialize a dictionary to store the results grouped by cart_master_id
    result_dict = defaultdict(list)

    # Iterate through each payment detail
    for payment in payment_details:
        # Retrieve cart master for the payment
        cart_master_obj = cart_master.objects.filter(id=payment.cart_master_id).first()

        if cart_master_obj:
            # Extract user_id and item_ids
            user_id = cart_master_obj.customert_id
            cart_child_items = cart_child.objects.filter(cart_master_id=payment.cart_master_id)
            item_ids = [item.item_id for item in cart_child_items]

            # Fetch user details from customer_reg table
            user_details = customer_reg.objects.filter(id=user_id).first()

            # Calculate number of items and amount paid
            number_of_items = cart_child_items.count()
            amount_paid = cart_master_obj.cart_tot_amt
            pay_status = payment.status
            pay_date = payment.pay_date
            # Append user and item details along with number of items and amount paid to the result dictionary
            result_dict[cart_master_obj.id].append({'user_details': user_details,
                                                     'number_of_items': number_of_items,
                                                     'amount_paid': amount_paid,
                                                     'pay_status':pay_status,
                                                     'pay_date':pay_date})

    # Convert the dictionary to a list of grouped results
    result = [{'cart_master_id': cart_master_id, 'details': details}
              for cart_master_id, details in result_dict.items()]

    return render(request, 'admin/admin_sales_view.html', {'result': result})

def delivery_detail_admin(request, id):
    # Fetch delivery details
    delivery_details = tbl_delivery.objects.filter(cart_master_id=id)

    # Initialize an empty list to store the result
    result = []

    # Iterate through each delivery detail
    for delivery in delivery_details:
        # Retrieve the courier assign details based on cassign_id
        cassign_details = tbl_cassign.objects.filter(id=delivery.cassign_id).first()

        # Retrieve the courier company details based on courier_id
        courier_details = tbl_courier.objects.filter(id=cassign_details.courier_id).first()

        # Append the company name, phone, email, assign date, delivery date, and status to the result list
        result.append({
            'company_name': courier_details.co_name,
            'company_phone': courier_details.co_phone,
            'company_email': courier_details.email,
            'courier_assign_date': cassign_details.cassign_date,
            'delivery_date': delivery.del_date,
            'delivery_status': cassign_details.status
        })

    return render(request, 'admin/delivery_detail_admin.html', {'result': result})

def view_hom_pro(request):
    items=tbl_product.objects.all()
    categories=category.objects.all()
    for i in items:
        for j in categories:
            if i.cat_id == str(j.id):
                i.cat_id=j.category_name
    return render(request,'admin/view_hom_pro.html',{'items':items})

def removepro(request,id):
    staff=tbl_product.objects.get(id=id)
    staff.delete()
    return redirect(view_hom_pro)
def deactivepro(request,id):
    recipe_detail = get_object_or_404(tbl_product, id=id)
    recipe_detail.item_status = 'Deactive'
    recipe_detail.save()
    return redirect(view_hom_pro)

def activepro(request,id):
    recipe_detail = get_object_or_404(tbl_product, id=id)
    recipe_detail.item_status = 'Available'
    recipe_detail.save()
    return redirect(view_hom_pro)

def add_items(request):
    sub_categories=subcategory.objects.all()
    categories=category.objects.all()
    return render(request,"admin/item_add.html",{'sub_categories':sub_categories,'categories':categories})

def add_items_insert(request):
    if request.method == "POST":
        item_name = request.POST.get('item_name')
        cat_id = request.POST.get('cat_id')
        subcat_id = request.POST.get('subcat_id')
        item_desc = request.POST.get('item_desc')
        myfile = request.FILES['image']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)

        # Retrieve category and subcategory instances
        cat_instance = category.objects.get(id=cat_id)
        subcat_instance = subcategory.objects.get(id=subcat_id)

        # Create tbl_item instance with category and subcategory instances
        new_item = tbl_item(category=cat_instance, subcategory=subcat_instance,
                            item_name=item_name, item_desc=item_desc,
                            item_status='Available',recipe_status='pending',item_image=filename)
        new_item.save()
        
        return render(request, "admin/index.html", {'message': 'Successfully Added'})
    
def view_items_admin(request):
    items=tbl_item.objects.all()

    return render(request,'admin/view_items.html',{'items':items})


def edititem(request,id):
    items=tbl_item.objects.get(id=id)
    return render(request,'admin/edititem.html',{'result':items})
def addedititem(request,id):
    if request.method=="POST":
        item_name = request.POST.get('item_name')
        cat_id = request.POST.get('cat_id')
        subcat_id = request.POST.get('subcat_id')
        item_desc = request.POST.get('item_desc')
        image = request.POST.get('image')
        item_status = request.POST.get('item_status')
        recipe_status = request.POST.get('recipe_status')


        # Retrieve category and subcategory instances
        cat_instance = category.objects.get(id=cat_id)
        subcat_instance = subcategory.objects.get(id=subcat_id)

        # Create tbl_item instance with category and subcategory instances
        new_item = tbl_item(category=cat_instance, subcategory=subcat_instance,
                            item_name=item_name, item_desc=item_desc,
                            item_status=item_status,recipe_status=recipe_status,item_image=image,id=id)
        new_item.save()
        return redirect(view_items_admin)
    
def removeitem(request,id):
    staff=tbl_item.objects.get(id=id)
    staff.delete()
    return redirect(view_items_admin)
#staff
def staff_profile(request):
    staff=staff_reg.objects.get(id=request.session['sid'] )
    return render(request,'admin/staff_profile.html',{'result':staff})

def addrecipe(request,id):
    items=tbl_item.objects.get(id=id)
    return render(request,'admin/addrecipe.html',{'result':items})

def add_recipe_insert(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        pre_time = request.POST.get('pre_time')
        cook_time = request.POST.get('cook_time')

        item_instance = tbl_item.objects.get(id=item_id)

        new_item = tbl_recipes(item=item_instance, recipe_name=recipe_name,
                            recipe_desc=recipe_desc, pre_time=pre_time,
                            cook_time=cook_time)
        new_item.save()
        recipe_detail = get_object_or_404(tbl_item, id=item_id)
        recipe_detail.recipe_status = 'added'
        recipe_detail.save()
        return render(request, "admin/index.html", {'message': 'Successfully Added'})


def viewrecipe(request,id):
    items=tbl_recipes.objects.get(item=id)
    return render(request,'admin/viewrecipe.html',{'result':items})

def editrecipe(request,id):
    items=tbl_recipes.objects.get(id=id)
    return render(request,'admin/editrecipe.html',{'result':items})
def edit_recipe_insert(request,id):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        recipe_name = request.POST.get('recipe_name')
        recipe_desc = request.POST.get('recipe_desc')
        pre_time = request.POST.get('pre_time')
        cook_time = request.POST.get('cook_time')

        item_instance = tbl_item.objects.get(id=item_id)

        new_item = tbl_recipes(item=item_instance, recipe_name=recipe_name,
                            recipe_desc=recipe_desc, pre_time=pre_time,
                            cook_time=cook_time,id=id)
        new_item.save()
        recipe_detail = get_object_or_404(tbl_item, id=item_id)
        recipe_detail.recipe_status = 'added'
        recipe_detail.save()
        return redirect(reverse('viewrecipe', kwargs={'id': item_id}))



def addingred(request,id):
    items=tbl_item.objects.get(id=id)
    return render(request,'admin/addingred.html',{'result':items})

def add_ing_insert(request):
    if request.method == "POST":
        item_id = request.POST.get('item_id')
        ingrediant = request.POST.get('ingrediant')
        ing_unit = request.POST.get('ing_unit')


        item_instance = tbl_item.objects.get(id=item_id)

        new_item = tbl_ingrediantcalc(item=item_instance, ingrediant=ingrediant,
                            ing_unit=ing_unit,)
        new_item.save()
        return redirect(view_items_admin)
from collections import defaultdict

def courier_assign(request):
    # Fetch all payment details
    payment_details = tbl_payment.objects.filter(status='paid')

    # Initialize a dictionary to store the results grouped by cart_master_id
    result_dict = defaultdict(list)

    # Iterate through each payment detail
    for payment in payment_details:
        # Retrieve cart master for the payment
        cart_master_obj = cart_master.objects.filter(id=payment.cart_master_id).first()

        if cart_master_obj:
            # Extract user_id and item_ids
            user_id = cart_master_obj.customert_id
            cart_child_items = cart_child.objects.filter(cart_master_id=payment.cart_master_id)
            item_ids = [item.item_id for item in cart_child_items]

            # Fetch user details from customer_reg table
            user_details = customer_reg.objects.filter(id=user_id).first()

            # Calculate number of items and amount paid
            number_of_items = cart_child_items.count()
            amount_paid = cart_master_obj.cart_tot_amt

            # Append user and item details along with number of items and amount paid to the result dictionary
            result_dict[cart_master_obj.id].append({'user_details': user_details,
                                                     'number_of_items': number_of_items,
                                                     'amount_paid': amount_paid})

    # Convert the dictionary to a list of grouped results
    result = [{'cart_master_id': cart_master_id, 'details': details}
              for cart_master_id, details in result_dict.items()]

    return render(request, 'admin/view_cassign.html', {'result': result})

def assign_courier(request,id):
    if request.method=="POST":
        courier_id=request.POST.get('courier_id')
        cassign_date=request.POST.get('cassign_date')
        ins=tbl_cassign(courier_id=courier_id,cassign_date=cassign_date,cart_master_id=id,status='pending')
        ins.save()
        cart_detail = get_object_or_404(tbl_payment, cart_master_id=id)
        cart_detail.status = 'Assigned'
        cart_detail.save()
        return render(request, 'admin/index.html', {'message': 'Assigned Successfully'})
    else:
        c_company=tbl_courier.objects.all()
        cart=cart_master.objects.get(id=id)
        return render(request,'admin/assign_courier.html',{'result':c_company,'cart':cart})




#Customer
def cus_profile(request):
    staff=customer_reg.objects.get(id=request.session['cuid'] )
    return render(request,'cus_profile.html',{'result':staff})

def add_my_products(request):
    if request.method=="POST":
        customer_id = request.session['cuid']
        customer_instance = customer_reg.objects.get(id=customer_id)
        product_categoryy=request.POST.get('cat_id')
        prod_name=request.POST.get('prod_name')
        prod_desc=request.POST.get('prod_desc')
        prod_qnty=request.POST.get('prod_qnty')
        prod_price=request.POST.get('prod_price')
        myfile=request.FILES['prod_image']
        fs= FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        cus=tbl_product(customer=customer_instance,cat_id=product_categoryy,item_name=prod_name,item_image=filename,item_desc=prod_desc,item_stock=prod_qnty,item_status='Available',item_price=prod_price)
        cus.save()
        customer_id = request.session['cuid']
        staff=tbl_product.objects.filter(customer=customer_id)
        return render(request,"view_my_pro.html", {'message':'Succesfully Added','result':staff})
    else:   
        cate=product_category.objects.all()
        return render(request,"add_my_products.html",{'result':cate})
    
def view_my_pro(request):
    customer_id = request.session['cuid']
    staff=tbl_product.objects.filter(customer=customer_id)
    return render(request,'view_my_pro.html',{'result':staff})

def editpro(request,id):
    staff=tbl_product.objects.get(id=id)
    return render(request,'edit_my_pro.html',{'result':staff})

def addeditpro(request,id):
    if request.method == "POST":
        customer_id = request.session['cuid']
        customer_instance = customer_reg.objects.get(id=customer_id)
        product_categoryy = request.POST.get('cat_id')
        prod_name = request.POST.get('prod_name')
        prod_desc = request.POST.get('prod_desc')
        prod_qnty = request.POST.get('prod_qnty')
        prod_price = request.POST.get('prod_price')
        item_image = request.POST.get('item_image')
        item_status = request.POST.get('item_status')

        cus = tbl_product(customer=customer_instance, cat_id=product_categoryy, item_name=prod_name, item_image=item_image,
                          item_desc=prod_desc, item_stock=prod_qnty, item_status=item_status, item_price=prod_price, id=id)
        cus.save()

        return redirect(view_my_pro)
    
def delete_my_pro(request,id):
    categoryy = get_object_or_404(tbl_product, pk=id) 
    categoryy.delete()
    return redirect(view_my_pro) 

def view_products(request):
    items=tbl_product.objects.filter(item_status='Available')
    for item in items:
        item.item_stock = float(item.item_stock)
    return render(request,'products.html',{'result':items})


def search3(request):
    if request.method == "POST":
        title = request.POST.get('title')
        # Filter tbl_product based on item name, category name, and subcategory name
        crp = tbl_product.objects.filter(
            Q(item_name__icontains=title) | 
            Q(cat_id__icontains=title)  # Assuming cat_id represents the category ID or name
        )
        return render(request, 'products.html', {'result': crp})
    else:
        # If no search query is provided, redirect to the view_products page
        return redirect(view_products)

def add_cards(request):
    if request.method == "POST":
        customer_id = request.session['cuid']
        customer_instance = customer_reg.objects.get(id=customer_id)
        card_holder = request.POST.get('card_holder')
        card_no = request.POST.get('card_no')
        exp_date = request.POST.get('exp_date')
        cvv = request.POST.get('cvv')
        
        ins = card(customer=customer_instance, card_holder=card_holder, card_no=card_no, exp_date=exp_date, cvv=cvv)
        ins.save()
        return render(request, 'index.html', {'message': 'Successfully Added'})
    else:
        return render(request, 'add_cards.html')

def view_cards(request):
    card_dtl=card.objects.filter(customer=request.session['cuid'])
    return render(request,'view_cards.html',{'result':card_dtl})


def add_to_cart(request, id):
    if request.method == "POST" or request.method == "GET":
        customer_id = request.session.get('cuid')
        if not customer_id:
            return HttpResponse("Invalid customer ID")

        item_id = id
        item_details = tbl_product.objects.get(id=item_id)
        item_price = float(item_details.item_price)

        # Check if there is an existing cart_master for the customer
        existing_cart_master = cart_master.objects.filter(customert_id=customer_id,cart_status='Active').first()

        if existing_cart_master:
            # If a cart_master exists, get the current cart_tot_amt
            current_cart_tot_amt = float(existing_cart_master.cart_tot_amt)

            # Update the total amount in the cart_master
            existing_cart_master.cart_tot_amt = str(current_cart_tot_amt + item_price)
            existing_cart_master.save()



            # Add the item to the cart_child table with the existing master id
            cart_child_item = cart_child(cart_master_id=existing_cart_master.id, item_id=item_id,
                                         cart_qty=1, cart_price=item_price)
            cart_child_item.save()
        else:
            # If no cart_master exists, create a new cart_master and add the item to cart_child
            new_cart_master = cart_master(customert_id=customer_id, cart_tot_amt=str(item_price),cart_status='Active')
            new_cart_master.save()



            cart_child_item = cart_child(cart_master_id=new_cart_master.id, item_id=item_id,
                                         cart_qty=1, cart_price=item_price)
            cart_child_item.save()

        return redirect(viewcart)

    return HttpResponse("Invalid request method")

    
def viewcart(request):
    customer_id = request.session.get('cuid')
    try:
        cart_master_obj = cart_master.objects.get(customert_id=customer_id,cart_status='Active')
    except cart_master.DoesNotExist:
        # If cart_master object doesn't exist, the cart is empty
        return render(request, 'empty_cart.html')

    master_id = cart_master_obj.id
    cart_child_items = cart_child.objects.filter(cart_master_id=master_id)
    total_products = cart_child_items.count()
    request.session['carttotalitem'] = total_products
    
    # Fetch corresponding item details for each cart item
    cart_items_with_details = []
    for cart_item in cart_child_items:
        item_details = tbl_product.objects.get(id=cart_item.item_id)

        try:
            # Convert quantities and prices to floats
            qty = float(cart_item.cart_qty)
            price = float(item_details.item_price)

            # Calculate total price and round to two decimal places
            total_price = round(qty * price, 2)
        except ValueError:
            total_price = 0  # Set a default value in case of conversion errors

        cart_items_with_details.append({
            'cart_item': cart_item,
            'item_details': item_details,
            'total_price': total_price,
        })

    return render(request, 'cart.html', {'cart_items_with_details': cart_items_with_details, 'cart_master_obj': cart_master_obj})

def update_qnty(request, id):
    if request.method == "POST":
        updt_qnty = int(request.POST.get('updt_qnty'))
        cart_detail = cart_child.objects.get(id=id)

        # Get item details from items_tbl
               # Get item details from items_tbl
        item_detail = tbl_product.objects.get(id=cart_detail.item_id)



        # Update quantity in cart_child
        cart_detail.cart_qty = updt_qnty
        cart_detail.cart_price = updt_qnty * item_detail.item_price
        cart_detail.save()



        # Recalculate total price in cart_master
        cart_master_id = cart_detail.cart_master_id
        cart_child_instances = cart_child.objects.filter(cart_master_id=cart_master_id)
        total_amount = sum(child.cart_price for child in cart_child_instances)

        # Update cart_tot_amt in cart_master
        cart_master_detail = cart_master.objects.get(id=cart_master_id)
        cart_master_detail.cart_tot_amt = total_amount
        cart_master_detail.save()

        return redirect(viewcart)  # Assuming 'viewcart' is the correct URL name

    return render(request, 'index.html')


def remove_cart_item(request, id):
    # Get cart item details
    cart_detail = get_object_or_404(cart_child, id=id)
    cart_master_obj = cart_master.objects.get(id=cart_detail.cart_master_id)
    item_details = tbl_product.objects.get(id=cart_detail.item_id)

    # Remove item from cart_child
    cart_detail.delete()


    # Reduce cart_price from total_price in cart_master
    cart_master_obj.cart_tot_amt -= cart_detail.cart_price
    cart_master_obj.save()

    # Check if there are any remaining items for the same master ID
    remaining_items = cart_child.objects.filter(cart_master_id=cart_master_obj.id).exists()
    if not remaining_items:
        # If no remaining items, delete corresponding entry in cart_master table
        cart_master_obj.delete()

    # Redirect to viewcart page
    return redirect(viewcart)

def checkout(request,id):
    crd_mstr=cart_master.objects.get(id=id)
    user_details=customer_reg.objects.get(id=crd_mstr.customert_id)
    card_dtl=card.objects.filter(customer=request.session['cuid'])
    return render(request,'checkout.html',{'result':crd_mstr,'result1':user_details,'card_dtl':card_dtl})

from django.db import transaction

def add_payment(request, id):
    if request.method == 'POST':
        card_id = request.POST.get('card_id')
        cvv = request.POST.get('cvv')
        cart_master_id = id
        card_dtl=card.objects.get(id=card_id) 
        if cvv == card_dtl.cvv:
            try:
                with transaction.atomic():
                    # Save payment details
                    ins = tbl_payment.objects.create(cart_master_id=cart_master_id, card_id=card_id, status='paid')

                    # Mark cart as 'Deactive'
                    cart_detail = get_object_or_404(cart_master, id=id)
                    cart_detail.cart_status = 'Deactive'
                    cart_detail.save()

                    # Reduce item stock quantities
                    cart_items = cart_child.objects.filter(cart_master_id=cart_master_id)
                    for cart_item in cart_items:
                        # Get item details
                        item = tbl_product.objects.get(id=cart_item.item_id)

                        # Deduct purchased quantity from item stock
                        item.item_stock -= cart_item.cart_qty
                        item.save()

            except Exception as e:
                # Handle any exceptions and rollback the transaction
                print("Error occurred:", str(e))
                return HttpResponse("An error occurred during payment processing.")

            # Refresh the cart total in session
            customer_id = request.session.get('cuid')
            cart_master_obj = cart_master.objects.filter(customert_id=customer_id, cart_status='Active').first()
            total_products = cart_master_obj.cart_child_set.count() if cart_master_obj else 0
            request.session['carttotalitem'] = total_products

            return render(request, 'index.html', {'message': 'Your Payment was Successful'})
        else:
            return render(request, 'index.html', {'message': 'Your Payment was not Successful.You Entered a wrong cvv'})
        

def my_purchases(request):
    try:
        # Fetch cart details for the current user where cart_status = Deactive
        cart_dtls = cart_master.objects.filter(customert_id=request.session['cuid'], cart_status='Deactive')

        # Initialize lists to store purchase details
        purchase_details = []

        # Iterate through each cart detail
        for cart_dtl in cart_dtls:
            # Fetch payment details based on the cart master
            pay_tbl = tbl_payment.objects.filter(cart_master_id=cart_dtl.id).first()

            # Fetch delivery details based on the cart master
            delivery_details = tbl_delivery.objects.filter(cart_master_id=cart_dtl.id).first()

            # Fetch items purchased based on the cart master
            cart_items = cart_child.objects.filter(cart_master_id=cart_dtl.id)

            # Calculate total items and total amount
            total_items = cart_items.count()
            total_amount = cart_dtl.cart_tot_amt

            # Prepare a list to store item names
            item_names = []

            # Retrieve item names based on item IDs
            for cart_item in cart_items:
                item = tbl_product.objects.get(id=cart_item.item_id)
                item_names.append(item.item_name)

            # Prepare a dictionary with purchase details for this cart
            purchase_detail = {
                'cart_dtl': cart_dtl.id,
                'item_names': item_names,
                'total_items': total_items,
                'total_amount': total_amount,
                'purchase_date': pay_tbl.pay_date if pay_tbl else None,
                'delivery_date': delivery_details.del_date if delivery_details else None
            }

            # Append the purchase detail to the list
            purchase_details.append(purchase_detail)

        # Prepare context data to pass to the template
        context = {
            'purchase_details': purchase_details
        }

        return render(request, 'my_purchases.html', context)
    except Exception as e:
        # Handle exceptions, such as if the user's cart or payment details are not found
        print(e)  # Print the error for debugging purposes
        return render(request, '404.html')
    

def view_bill(request, cart_master_id):
    try:
        # Fetch cart details based on the cart master ID
        cart_dtl = cart_master.objects.get(id=cart_master_id)

        # Fetch payment details based on the cart master
        pay_tbl = tbl_payment.objects.filter(cart_master_id=cart_dtl.id).first()

        # Fetch delivery details based on the cart master
        delivery_details = tbl_delivery.objects.filter(cart_master_id=cart_dtl.id).first()

        # Fetch items purchased based on the cart master
        cart_items = cart_child.objects.filter(cart_master_id=cart_dtl.id)

        # Prepare a list to store item details
        item_details = []

        # Retrieve item details based on item IDs
        for cart_item in cart_items:
            item = tbl_product.objects.get(id=cart_item.item_id)
            item_detail = {
                'p_id': item.id,
                'p_name': item.item_name
            }
            item_details.append(item_detail)

        # Calculate total items and total amount
        total_items = cart_items.count()
        total_amount = cart_dtl.cart_tot_amt

        # Fetch user/customer details based on the information stored in the cart_master
        user_details = customer_reg.objects.get(id=cart_dtl.customert_id)

        # Prepare context data to pass to the template
        context = {
            'result': {
                'date': pay_tbl.pay_date if pay_tbl else None,
                'item_details': item_details,
                'p_amount': total_amount
            },
            'user': {
                'name': f"{user_details.fname} {user_details.lname}",
                'phone': user_details.phone,
                'place': f"{user_details.district}, {user_details.street}"
            }
        }

        return render(request, 'invoice.html', context)
    except cart_master.DoesNotExist:
        return render(request, '404.html')
    except Exception as e:
        # Handle other exceptions
        print(e)  # Print the error for debugging purposes
        return render(request, '404.html')



def view_recipes(request):
    items=tbl_item.objects.all()
    return render(request,'view_recipes.html',{'result':items})
def search(request):
    if request.method == "POST":
        title = request.POST.get('title')
        # Filter items_tbl based on item name, brand, category, and subcategory
        crp = tbl_item.objects.filter(
            Q(item_name__icontains=title) | 
            Q(category__category_name__iexact=title) |
            Q(subcategory__subcat_name__icontains=title)
        )
        return render(request, 'view_recipes.html', {'result': crp})
    else:
        # Display all items with status 'Available' if no search query is provided
        return redirect(view_recipes)
    
def search2(request):
    if request.method == "POST":
        title = request.POST.get('title')
        # Filter items_tbl based on selected option (category name)
        crp = tbl_item.objects.filter(
            Q(category__category_name__iexact=title)
        )
        return render(request, 'view_recipes.html', {'result': crp})
    else:
        return redirect(view_recipes)
    
def view_item_recipes(request, id):
    items = tbl_recipes.objects.get(item=id)
    itm = get_object_or_404(tbl_item, id=id)
    ingredients = tbl_ingrediantcalc.objects.filter(item=itm)

    # Format ingredients in the view
    formatted_ingredients = []
    for ingredient in ingredients:
        ing_unit = '{:.2f}'.format(ingredient.ing_unit).rstrip('0').rstrip('.')
        formatted_ingredients.append({'ing_unit': ing_unit, 'ingrediant': ingredient.ingrediant})

    return render(request, 'view_item_recipes.html', {'result': items, 'itm': itm, 'ingredients': formatted_ingredients})

def calculation(request):
    if request.method == 'POST':
        serve_num = int(request.POST.get('serve_num'))
        item_id = int(request.POST.get('item_id'))
        itm = get_object_or_404(tbl_item, id=item_id)
        result = tbl_recipes.objects.get(item=itm)  # Fetching tbl_recipes features
        ingredients = tbl_ingrediantcalc.objects.filter(item=itm)
        
        # Calculate ingredient units based on serve_num
        calculated_ingredients = []
        for ingredient in ingredients:
            calculated_unit = float(ingredient.ing_unit) * serve_num
            ing_unit = '{:.2f}'.format(calculated_unit).rstrip('0').rstrip('.')
            calculated_ingredients.append({'ing_unit': ing_unit, 'ingrediant': ingredient.ingrediant})

        return render(request, 'calculated.html', {'result': result, 'itm': itm, 'ingredients': calculated_ingredients,'serve_num':serve_num})
    return render(request, 'calculated.html')



#Courier 
    
def courier_view_company(request):
    # Fetch all assignments for the courier
    assignments = tbl_cassign.objects.filter(courier_id=request.session['coid'])

    # Initialize an empty list to store the result
    result = []

    # Iterate through each assignment
    for assign in assignments:
        # Retrieve the payment details for the current assignment
        payment_details = tbl_payment.objects.filter(cart_master_id=assign.cart_master_id)

        # Initialize a list to store the details for each payment
        payment_details_list = []

        # Iterate through each payment detail
        for payment in payment_details:
            # Retrieve cart master for the payment
            cart_master_obj = cart_master.objects.filter(id=payment.cart_master_id).first()

            if cart_master_obj:
                # Extract user_id and item_ids
                user_id = cart_master_obj.customert_id
                cart_child_items = cart_child.objects.filter(cart_master_id=payment.cart_master_id)
                item_ids = [item.item_id for item in cart_child_items]

                # Fetch user details from customer_reg table
                user_details = customer_reg.objects.filter(id=user_id).first()

                # Calculate number of items and amount paid
                number_of_items = cart_child_items.count()
                amount_paid = cart_master_obj.cart_tot_amt

                # Append user and item details along with number of items and amount paid to the payment_details_list
                payment_details_list.append({'user_details': user_details,
                                              'number_of_items': number_of_items,
                                              'amount_paid': amount_paid})

        # Append the payment details list along with the assign details to the result list
        result.append({'assignment_details': assign, 'payment_details': payment_details_list})

    return render(request, 'admin/courier_assign.html', {'result': result})

def accept_courier(request,id):
    cart_detail = get_object_or_404(tbl_cassign, id=id)
    cart_detail.status = 'Accepted'
    cart_detail.save()
    return redirect(courier_view_company)

def reject_courier(request,id):
    cart_detail = get_object_or_404(tbl_cassign, id=id)
    cart_detail.status = 'rejected'
    cart_detail.save()
    cart_master_id=cart_detail.cart_master_id
    paymt_detail=get_object_or_404(tbl_payment,cart_master_id=cart_master_id)
    paymt_detail.status = 'paid'
    paymt_detail.save()
    return redirect(courier_view_company)

def delivery_update_company(request,id):
    assign_table=tbl_cassign.objects.get(id=id)
    return render(request,'admin/delivery_update_company.html',{'result':assign_table})

def add_delivery_update_company(request):
    del_date = request.POST.get('del_date')
    cart_master_id = request.POST.get('cart_master_id')
    cassign_id = request.POST.get('cassign_id')
         
    ins = tbl_delivery(cassign_id=cassign_id, cart_master_id=cart_master_id, del_date=del_date)
    ins.save()
    cart_detail = get_object_or_404(tbl_cassign, cart_master_id=cart_master_id,status='Accepted')
    cart_detail.status = 'delivered'
    cart_detail.save()
    return render(request, 'admin/index.html', {'msg': 'Updated Successfully'})

def view_delivery_details(request):
    # Fetch all assignments with status 'delivered' for the courier
    assignments = tbl_cassign.objects.filter(courier_id=request.session['coid'], status='delivered')

    # Initialize an empty list to store the result
    result = []

    # Iterate through each delivery assignment
    for assign in assignments:
        # Retrieve the delivery details for the current assignment
        delivery_details = tbl_delivery.objects.filter(cassign_id=assign.id)

        # Initialize a list to store the details for each delivery
        delivery_details_list = []

        # Iterate through each delivery detail
        for delivery in delivery_details:
            # Retrieve cart master for the delivery
            cart_master_obj = cart_master.objects.filter(id=delivery.cart_master_id).first()

            if cart_master_obj:
                # Extract user_id and item_ids
                user_id = cart_master_obj.customert_id
                cart_child_items = cart_child.objects.filter(cart_master_id=delivery.cart_master_id)
                item_ids = [item.item_id for item in cart_child_items]

                # Fetch user details from customer_reg table
                user_details = customer_reg.objects.filter(id=user_id).first()

                # Calculate number of items and amount paid
                number_of_items = cart_child_items.count()
                amount_paid = cart_master_obj.cart_tot_amt
                cassign_date = assign.cassign_date
                # Append user and item details along with number of items and amount paid to the delivery_details_list
                delivery_details_list.append({'user_details': user_details,
                                               'number_of_items': number_of_items,
                                               'amount_paid': amount_paid,
                                               'del_date': delivery.del_date,
                                               'cassign_date': cassign_date})

        # Append the delivery details list along with the assign details to the result list
        result.append({'assignment_details': assign, 'delivery_details': delivery_details_list})

    return render(request, 'admin/view_delivery_details.html', {'result': result})