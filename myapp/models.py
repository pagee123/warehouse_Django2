import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # 使用內建的User模型
from django.conf import settings

# Create your models here.

class Supplier(models.Model):
    name = models.CharField(max_length=100)  # 廠商名稱
    contact_info = models.TextField(blank=True, null=True)  # 廠商聯絡資訊（選填）

    def __str__(self):
        return self.name
    
class ProductType(models.Model):
    name = models.CharField(max_length=100)  # 類型名稱

    def __str__(self):
        return self.name

class Product(models.Model):
    serial_number = models.AutoField(primary_key=True)  # 流水號，會自動遞增
    barcode = models.CharField(max_length=50, unique=True) 
    product_name = models.CharField(max_length=100)  # 貨品名稱
    arrival_date = models.DateField(default=timezone.now)  # 進貨日期，預設為當前日期
    quantity = models.PositiveIntegerField()  # 貨品數量，必須為正整數
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)  # 與類型關聯
    description = models.TextField(blank=True, null=True)  # 敘述，允許為空
    supplier = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)  # 與廠商關聯

    def __str__(self):
        return self.product_name
    
    # 增加存入和取出的簡單方法
    def add_quantity(self, amount):
        self.quantity += amount
        self.save()

    def remove_quantity(self, amount):
        if self.quantity >= amount:
            self.quantity -= amount
            self.save()
            return True
        else:
            return False  # 如果數量不足以取出，返回 False
    def delete(self, *args, **kwargs):
        # 刪除所有與該產品關聯的圖片
        for image in self.images.all():
            image.delete()  # 這將同時刪除文件
        super().delete(*args, **kwargs)
        
class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='images', on_delete=models.CASCADE)  # 與 Product 關聯
    image = models.ImageField(upload_to='images/')  # 圖片上傳路徑

    def __str__(self):
        return f"Image for {self.product.product_name}"
    
    def delete(self, *args, **kwargs):
        # 檢查文件是否存在
        if self.image:
            image_path = os.path.join(settings.MEDIA_ROOT, self.image.path)
            # 刪除文件
            if os.path.isfile(image_path):
                os.remove(image_path)
        # 刪除資料庫記錄
        super().delete(*args, **kwargs)

class ActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=255)  # 動作描述
    timestamp = models.DateTimeField(auto_now_add=True)  # 記錄時間

    def __str__(self):
        return f"{self.user.username} 在 {self.timestamp.strftime('%Y-%m-%d %H:%M')} : {self.action}"