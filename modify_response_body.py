from libmproxy.models import decoded

def start(context, argv):
    f = open('/home/sunny/Desktop/body.txt')
    context.mydata = f.read()
    f.close()
    print(context.mydata)

def response(context, flow):
    with decoded(flow.response):
        flow.response.content = context.mydata #change response body
	
