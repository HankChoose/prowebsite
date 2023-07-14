from django.shortcuts import render
from django.conf import settings

def index(request):
    '''
    context = {
        'STATIC_ROOT': settings.STATIC_ROOT,
        'STATIC_URL': settings.STATIC_URL,
    }

    
    static_root = settings.STATIC_ROOT
    static_url = settings.STATIC_URL
    '''
    return render(request, 'index.html')
'''
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['POST'])
def register(request):
    # 处理用户注册逻辑
    return Response({'message': 'User registered successfully'})

@api_view(['POST'])
def login(request):
    # 处理用户登录逻辑
    return Response({'message': 'User logged in successfully'})
 '''