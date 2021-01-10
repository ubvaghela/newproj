# -*- coding: utf-8 -*-
SUCCESS = True
FAIL = False

def getPositiveResponse(message,status_code,data={}):
    response = {}
    response['status'] = SUCCESS
    response['message'] = message
    response['status_code'] = status_code
    response['result'] = data
    return response

def getNagativeResponse(message,status_code,data={}):
    response = {}
    response['status'] =FAIL
    response['message'] = message
    response['status_code'] = status_code
    response['result'] = data
    return response