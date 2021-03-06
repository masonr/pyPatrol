import os
from sanic.response import json
from utils import verifyIPv6

def ping6(ip_addr):
	ip_addr = verifyIPv6(ip_addr)
	if ip_addr is None:
		return "error"

	response = os.system("ping6 -c 1 -w2 " + ip_addr + " > /dev/null 2>&1")
	if response == 0:
		status = "online"
	else:
		status = "offline"

	return status

def invoke(request):
	ip_addr = request.json['ip']
	return json({"status": ping6(ip_addr)})