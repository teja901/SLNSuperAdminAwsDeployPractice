
from django.shortcuts import render


class AuthenticationMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response


    def __call__(self, request):
        print(request.path) 
        print("Im Middleware")
        if request.path.startswith('/superadmin/app1/api/'):
            return self.get_response(request)

        if request.path.startswith("/superadmin/app1/Login") and  not request.session.get('LoginAccess') and request.method!='POST':
            print('Login Page From if block')
            request.session['indexPage']=True
            return render(request,'Login.html')
        elif request.path.startswith("/superadmin/") and not request.session.get('LoginAccess') and not request.path.startswith("/superadmin/app1/Login"):
            print("Login Page From elif block")
            if request.session.get('indexPage'):
                del request.session['indexPage']
            request.session['responseUrl']=request.build_absolute_uri()
            return render(request,'Login.html')
        else:
            return self.get_response(request)
            
            