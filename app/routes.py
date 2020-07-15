from app import app
from flask import request
from urllib.parse import unquote
from pyzabbix.api import ZabbixAPI

@app.route('/')
def home():
    return 'Try one of the paths'
@app.route('/api/v1/zab/testackwtask', methods=['GET'])
def testack():
    eventid = int(unquote(request.args['eventid']).replace("'", ''))
    taskid = request.args['taskid']
    action = app.config['ACTION']
    form_string = "Eventid = {} TASK = {} ACTION = {}".format(eventid,taskid, action)
    return form_string
@app.route('/api/v1/zab/ackwtask', methods=['GET'])
def ack():
    eventid = int(unquote(request.args['eventid']).replace("'", ''))
    taskid = request.args['taskid']
    action = app.config['ACTION']
    #login to zabbix
    zapi = ZabbixAPI(url= app.config['URL'], user= app.config['USER'], password= app.config['PWD'])
    #acknowledge alert
    zapi.do_request('event.acknowledge', { 'eventids': eventid, 'action': action, 'message': 'ServiceNow has created {} for this alert'.format(taskid) })
    #logut zabbix
    zapi.do_request('user.logout')
    return 'ok'