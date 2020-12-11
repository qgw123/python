from django.shortcuts import render,HttpResponse,redirect
from django.views import View   #CBV
import os

# Create your views here.
USER_DICT = {
    '1':{'name':'root', 'email':'root@163.com'},
    '2':{'name':'qwer', 'email':'qwer@163.com'},
    '3':{'name':'asdf', 'email':'asdf@163.com'},
    '4':{'name':'zxcv', 'email':'zxcv@163.com'},
    '5':{'name':'oplk', 'email':'oplk@163.com'},
}

def index(request, nid, uid):
    print(request.path_info)

    from django.urls import reverse
    v = reverse('index', args=(40,60,))
    print(v)

    return render(request , 'index.html' ,{'user_dict': USER_DICT})

# def detail(request, *args, **kwargs):
def  detail(request, nid):
    # return HttpResponse(nid)
    # print(nid, uid)
    # nid = request.GET.get('nid')
    detail_info = USER_DICT[nid]
    return render(request, 'detail.html', {'detail_info':detail_info})


# def login(request):
#     if request.method == 'GET':
#         return  render(request, 'login.html')
#     elif request.method == "POST":
#         username = request.POST.get('username')
#         passwrod = request.POST.get('pwd')
#         if username == 'qgw' and passwrod == 'qgw':
#             return redirect('/index/')
#         else:
#             return render(request, 'login.html')
#     else:
#         return redirect("/index/")
def login(request):
    if request.method == 'GET':
        return  render(request, 'login.html')
    elif request.method == "POST":
        #radio
        # v = request.POST.get('gender')
        # print(v)

        #checkbox
        v = request.POST.getlist('favor')
        print(v)

        #file
        # f = request.POST.get('file')  获取文件名
        # print(f)
        obj = request.FILES.get('file') #获取上传的文件
        print(obj, type(obj),obj.name)

        file_path = os.path.join('uploads',obj.name)
        f = open(file_path,mode='wb')
        for i  in  obj.chunks():
            f.write(i)
        f.close()
        return render(request, 'login.html')
    else:
        return redirect("/index/")

class Home(View):

    def dispatch(self, request, *args, **kwargs):   #先调用
        # 调用父类的dispatch
        print('before')
        result = super(Home,self).dispatch(request , *args, **kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return  render(request, 'home.html')

    def post(self,request):
        print(request.method)
        return  render(request, 'home.html')

