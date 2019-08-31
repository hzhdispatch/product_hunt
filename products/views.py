from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required#导入装饰器
from .models import Product
from django.utils import timezone 
from django.contrib.auth.models import User 

# Create your views here.


def product_list(request):
	return render(request, 'product_list.html')

@login_required#只有用户登录才能获取到发布页面
def publish(request):
	if request.method == 'GET':
		return render(request, 'publish.html')
	elif request.method == 'POST':
		title = request.POST['标题']
		intro = request.POST['介绍']
		url = request.POST['APP链接']
		try:
			icon = request.FILES['APP图标']
			image = request.FILES['大图']#图片要用files方式
		except Exception as err:
			return render(request,'publish.html',{'错误':'请上传图片'})
		product = Product()
		product.title = title
		product.intro = intro
		product.url = url
		product.icon = icon
		product.image = image
		product.pub_date = timezone.datetime.now()
		product.hunter = request.user #使用request中的user需要导入from django.contrib.auth.models import User 
		product.save()
		return redirect('主页')	

		return render(request, 'publish.html')