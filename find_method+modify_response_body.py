from libmproxy.models import decoded

def start(context, argv):
    f = open('/home/sunny/Desktop/body.txt')
    context.mydata = f.read()
    f.close()
	
def response(context, flow):
    with decoded(flow.response):
	if flow.request.method == "GET":
            flow.response.content = context.mydata

