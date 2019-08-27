from django.shortcuts import render,redirect
from django.contrib.auth.models import User #导入django自带的用户模板

# Create your views here.

def signup(request):
	if request.method == 'GET':
		return render(request,'signup.html')
	elif request.method == 'POST':
		user_name = request.POST['用户名']#post请求可以从POST字典中获取其包含的内容
		password1 = request.POST['密码']
		password2 = request.POST['确认密码']
		try:
			User.objects.get(username = user_name)#通过User模板查找数据库中是否有数据
			return render(request,'signup.html',{'用户名错误':'该用户名已存在'})
		except User.DoesNotExist:
			if password1 == password2:
				User.objects.create_user(username = user_name, password=password1)#通过模板创建新用户
				return redirect('主页')
			else:
				return render(request,'signup.html',{'密码错误':'两次输入的密码不一致！'})

			
		
