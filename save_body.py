from libmproxy.models import decoded
	
def response(context, flow):
    with decoded(flow.response):
	f = open('/home/sunny/Desktop/body.txt','a')
	if flow.request.content:
            f.write("request : \n")
            f.write(flow.request.content)
            f.write("\n")

        if flow.response.content:
            f.write("response : \n")
            f.write(flow.response.content)
            f.write("\n")
        
        f.write(b"------------------------------------------\n")
