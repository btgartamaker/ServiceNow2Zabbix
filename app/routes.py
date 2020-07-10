from app import app
from flask import request
from urllib.parse import unquote
from pyzabbix.api import ZabbixAPI

@app.route('/')
def home():
    return 'Try one of the paths'
@app.route('/test')
def test():
    eventid = int(unquote(request.args['eventid']).replace("'", ''))
    taskid = request.args['taskid']
    form_string = "Eventid = {} TASK = {}".format(eventid,taskid)
    return form_string
@app.route('/ack')
def ack():
    eventid = int(unquote(request.args['eventid']).replace("'", ''))
    taskid = request.args['taskid']
    #login to zabbix
    zapi = ZabbixAPI(url= app.config['URL'], user= app.config['USER'], password= app.config['PWD'])
    #acknowledge alert
    zapi.do_request('event.acknowledge', { 'eventids': eventid, 'action': 6, 'message': 'ServiceNow has created {} for this alert'.format(taskid) })
    #logut zabbix
    zapi.do_request('user.logout')
    return 'ok'