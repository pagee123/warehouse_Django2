from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib import messages
from .forms import *
import random
from .models import Product
from rest_framework import generics
from .serializers import ProductSerializer, UserSerializer
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required

# Create your views here.

#登入頁面資料處理
def login_view(request):
    if request.method == 'POST':  # 利用post傳遞
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')  # 成功登入後跳轉到首頁或其他頁面
            else:
                messages.error(request, "帳號密碼錯誤")
        else:
            messages.error(request, "驗證碼錯誤")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

def home_view(request):

    user = request.user  # 獲取登入者資訊
    logs = ActivityLog.objects.order_by('-timestamp')[:10]  # 只顯示最近的10條記錄
    return render(request, 'home.html', {'user': user,'logs': logs})

def random_digit_challenge():
    """自定義隨機生成數字的驗證碼"""
    digits = ''.join([str(random.randint(0, 9)) for _ in range(4)])  # 生成6位數字
    return digits, digits  # 返回兩個相同的值，第一個是顯示的驗證碼，第二個是用來檢查的

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()  # 保存新用戶
            login(request, user)  # 註冊後自動登入
            return redirect('home')  # 註冊成功後重定向到首頁或其他頁面
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

def product_list(request):
    query = request.GET.get('q')  # 獲取查詢參數（產品名稱）
    serial = request.GET.get('r')  # 獲取查詢參數（序號）
    product_type = request.GET.get('type')  # 獲取產品類型參數
    page_number = request.GET.get('page')  # 獲取當前頁碼
    # 根據查詢篩選產品
    if query:
        products = Product.objects.filter(product_name__icontains=query)
    elif serial:
        products = Product.objects.filter(serial_number__icontains=serial)
    else:
        products = Product.objects.all()

    # 如果有類型篩選條件，進一步篩選
    if product_type:
        products = products.filter(product_type__id=product_type)

    paginator = Paginator(products, 5)  # 每頁顯示 10 個產品
    page_obj = paginator.get_page(page_number)

    # 傳遞所有產品類型，用於頁面顯示類型篩選標籤
    all_types = ProductType.objects.all() 

    context = {
        'products': page_obj.object_list,
        'is_paginated': paginator.num_pages > 1,
        'page_obj': page_obj,
        'all_types': all_types,  # 所有產品類型
        'selected_type': product_type  # 當前選中的類型
    }
    print(products)
    return render(request, 'product_list.html', context)

def update_quantity(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        action = request.POST.get('action')
        amount = int(request.POST.get('amount'))

        if action == 'add':
            product.add_quantity(amount)
            messages.success(request, f'成功存入 {amount} 個 {product.product_name}.')
            action_description = (f"成功存入 {amount} 個 {product.product_name}.")
        elif action == 'remove':
            if product.remove_quantity(amount):
                messages.success(request, f'成功取出 {amount} 個 {product.product_name}.')
                action_description = (f"成功取出 {amount} 個 {product.product_name}.")
            else:
                messages.add_message(request,messages.ERROR, f'{product.product_name}庫存量不足,庫存為{product.quantity}')
                action_description = (f"{product.product_name}庫存量不足,庫存為{product.quantity}")
                
        user = request.user
        # 創建並保存操作記錄
        ActivityLog.objects.create(user=user, action=action_description)
        return redirect('product_list')  # 重定向到產品列表頁面

    return render(request, 'update_quantity.html', {'product': product})

def error_page(request):
    return render(request,'error.html',locals())

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid():
            # 保存產品
            product = form.save()

            # 創建操作記錄
            user = request.user
            action_description = f"成功建立 {product.product_name}，數量為 {product.quantity}。"
            ActivityLog.objects.create(user=user, action=action_description)

            return redirect('product_list')  # 新增成功後重定向到產品列表
        else:
            print(form.errors)  # 調試時輸出錯誤信息
    else:
        form = ProductForm()

    # 獲取現有的產品類型和供應商
    suppliers = Supplier.objects.all()
    product_types = ProductType.objects.all()
    print(form)

    return render(request, 'add_product.html', {
        'form': form,
        'suppliers': suppliers,
        'product_types': product_types
    })

def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    if request.method == 'POST':
        
        user = request.user
        action_description = (f"成功刪除{product.product_name}")
        # 創建並保存操作記錄
        ActivityLog.objects.create(user=user, action=action_description)
        product.delete()
        return redirect('product_list')  # 刪除成功後重定向到產品列表

    return render(request, 'delete_product.html', {'product': product})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)  # 自動登入用戶
            return redirect('home')  # 註冊成功後重定向到主頁
    else:
        form = SignUpForm()
    
    return render(request, 'signup.html', {'form': form})

# 貨品列表 API
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()  # 取得所有貨品
    serializer_class = ProductSerializer

# 單一貨品 API
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# 使用者列表 API
class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# 單一使用者 API
class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user is not None:
        # 如果驗證成功，返回 Token 或其他訊息
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'message': 'Login successful','username': user.username}, status=status.HTTP_200_OK)
    else:
        return Response({'message': 'Login Failed'}, status=status.HTTP_401_UNAUTHORIZED)
    
@api_view(['GET'])
#@login_required  # 確保只有已登錄用戶可以訪問
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)