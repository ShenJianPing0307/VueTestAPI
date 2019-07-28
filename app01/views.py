from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from app01 import models
import json


# Create your views here.

def getAllUser(request):
    queryset=models.UserInfo.objects.values('id','username','password')
    UserList=list(queryset)
    return HttpResponse(json.dumps(UserList,ensure_ascii=False))

def addUser(request):
    retDict={
        'code':1000,
        'state':False,
        'msg':'存储失败'
    }
    userjson=request.body #json数据存储在request.body中
    userdict=json.loads(str(userjson,encoding='utf8'))
    obj=models.UserInfo.objects.create(username=userdict['username'],password=userdict['password'])
    if obj:
        retDict['code']=2000
        retDict['state']=True
        retDict['msg']='存储成功'
        retDict['user']={'id':obj.id,'username':obj.username,'password':obj.password}
    return HttpResponse(json.dumps(retDict,ensure_ascii=False))

def delOneuser(request):
    retDict = {
        'code': 1001,
        'state': False,
        'msg': '删除失败'
    }
    userjson = request.body  # json数据存储在request.body中
    userdict = json.loads(str(userjson, encoding='utf8'))
    obj=models.UserInfo.objects.filter(id=userdict["id"]).first()
    if obj:
        obj.delete()
        retDict['code'] = 2000
        retDict['state'] = True
        retDict['msg'] = '删除成功'
        retDict['userlist'] = list(models.UserInfo.objects.values('id','username','password'))
    return HttpResponse(json.dumps(retDict,ensure_ascii=False))

def editOneuser(request):
    retDict = {
        'code': 1000,
        'state': False,
        'msg': '修改失败'
    }
    userjson = request.body  # json数据存储在request.body中
    userdict = json.loads(str(userjson, encoding='utf8'))
    if userdict["id"]:
        print(userdict["id"])
        models.UserInfo.objects.filter(id=userdict['id']).update(username=userdict['username'], password=userdict['password'])
        retDict['code'] = 1002
        retDict['state'] = True
        retDict['msg'] = '修改成功'
        retDict['userlist'] = list(models.UserInfo.objects.values('id','username','password'))
    return HttpResponse(json.dumps(retDict, ensure_ascii=False))




