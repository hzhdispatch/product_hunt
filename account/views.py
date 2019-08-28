from django.shortcuts import render,redirect
from django.contrib.auth.models import User #导入django自带的用户模板
from django.contrib import auth
# Create your views here.

def signup(request):
	if request.method == 'GET':#Get是到注册页面去
		return render(request,'signup.html')
	elif request.method == 'POST':#Post是想要注册
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

def login(request):
	if request.method == 'GET':#Get是到登录页面去
		return render(request,'login.html')
	elif request.method == 'POST':#Post是想要登录
		user_name = request.POST['用户名']
		pass_word = request.POST['密码']
		user = auth.authenticate(username=user_name,password=pass_word)#鉴定成功会返回一个用户
		if user is None:
			return render(request,'login.html',{'错误':'用户名或密码错误'})
		else:
			auth.login(request,user)
			return redirect('主页')


def logout(request):#登出不是get，不从服务器获取资源而是想修改服务器的信息/状态，
#但html那边默认是一种get—method，需要用隐藏的form标签
	if request.method == 'POST':#退出就不需要get只要post，一点按钮直接退出就好了
		auth.logout(request)
		return redirect('主页') 