import json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import (
    api_view,
    renderer_classes,
    )
from .models import TextMessages
@csrf_exempt
def index(request):
    return render(request, 'welcome', {})

@csrf_exempt
@api_view(['POST'])
@renderer_classes((JSONRenderer,))
def sendMsg(request):
	text_msg = request.data['msg']
	print text_msg
	try:
		text_msg = TextMessages(text_message= text_msg)
		text_msg.save()
	except Exception, e:
		print e
		return Response({
                "response_status": "failure",
                },status= status.HTTP_500_INTERNAL_SERVER_ERROR)
	return Response({
            "response_status": "success",
            },status= status.HTTP_200_OK)