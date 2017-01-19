def request(context, flow):
    method = flow.request.method
    flow.request.headers["method"] = method




