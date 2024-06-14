# from django.contrib import messages
# from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate,login,logout


# def sign_up(request):
#     return render(request, 'sign_up.html')

# def sign_in(request):
#     if request.method=='POST':
#         try:
#             username=request.POST.get('Username')
#             email=request.POST.get('Email')
#             password=request.POST.get('Password')
#             user_data=User.objects.create_user(username=username,email=email,password=password)
#             user_data.save()
#             success_message='Successfully Created User'
#             messages.success(request, success_message)
#             return redirect('index')
#         except Exception as e:
#             error_message='Username Already Exit Try Another'
#             messages.error(request, error_message)
#     return render(request, 'sign_up.html')

# def log_in(request):
#     if request.method=='POST':
#         username=request.POST.get('Username')
#         password=request.POST.get('Password')
#         user_data=authenticate(username=username, password=password)
#         if user_data:
#             login(request, user_data)
#             success_msg='Successfully Logged In'
#             messages.success(request, success_msg)
#             return redirect('index')
#         else:
#             error_message='Invalid Username or Password'
#             messages.error(request, error_message)
#     return render(request, 'sign_up.html')

# def sign_out(request):
#     logout(request)
#     success_msg='Successfully Logged Out'
#     messages.success(request, success_msg)
#     return render(request, 'sign_up.html')