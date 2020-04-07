import json

from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.forms import model_to_dict
# Create your views here.

# 用户注册
from user.models import ScoreUser


# 客户端上传端号和分数接口
def uploadData(request):

    # 获取客户端号
    clientNumber = request.POST.get('clientNumber','-1')
    # 获取分数
    score = request.POST.get('score',-1)
    if clientNumber != -1 and score != -1:
        # 判断上传的端号是否存在于数据库中，如果存在则直接修改分数，如果不存在则创建
        try:
            # 端号存在，直接修改分数
            obj = ScoreUser.objects.get(clientNumber=clientNumber)
            obj.score = score
            obj.save()
            return JsonResponse({'code':200,'msg':'分数修改成功','score':score})
        except Exception as e:
            # 端号不存在,创建客户端
            ScoreUser.objects.create(clientNumber=clientNumber,score=score)
            return JsonResponse({'code':201,'msg':'分数上传成功','score':score})
    else:
        return JsonResponse({'code':400,'msg':'参数违法'})




# 客户端查询排行榜
def query(request):
    '''

    :param request:
    :return: 1查询所有 2查询指定名次段 3都要将自己的排名放在最后
    '''
    currentObj_mingci = -1
    clientNumber = request.GET.get('clientNumber',None)
    if clientNumber == None:
        return JsonResponse({'code':-1,'msg':'客户端号必传'})
    else:
        try:
            obj = ScoreUser.objects.get(clientNumber=clientNumber)
        except Exception as e:
            return JsonResponse({
                'code': -1,
                'msg': '此用户未上传过自己的分数，不能查询排名'
            })
        begin = request.GET.get('begin', None)
        end = request.GET.get('end', None)

        if begin != None and end != None:
            # 2
            begin = int(begin)
            end = int(end)
            if begin <1 or end>ScoreUser.objects.count():
                return JsonResponse({'msg':'名次范围违法，重新选择名次范围','code':-1})
            queryset = ScoreUser.objects.order_by('-score').values()
            queryset = list(queryset)
            for i in queryset:
                i['mingci'] = queryset.index(i) + 1
                if obj.clientNumber == i['clientNumber']:
                    currentObj_mingci = i['mingci']
            currentObj = {
                'id':obj.id,
                'clientNumber':obj.clientNumber,
                'score':obj.score,
                'mingci':currentObj_mingci
            }

            queryset = queryset[begin-1:end]
            queryset.append(currentObj)
            return JsonResponse(queryset,safe=False)
        else:
            # 1
            queryset = ScoreUser.objects.order_by('-score').values()
            queryset = list(queryset)

            for i in queryset:
                i['mingci'] = queryset.index(i) + 1
                if obj.clientNumber == i['clientNumber']:
                    currentObj_mingci = i['mingci']
            currentObj = {
                'id':obj.id,
                'clientNumber':obj.clientNumber,
                'score':obj.score,
                'mingci':currentObj_mingci
            }
            queryset.append(currentObj)
            return JsonResponse(queryset, safe=False)



