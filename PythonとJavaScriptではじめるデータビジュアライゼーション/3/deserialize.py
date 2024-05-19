import datetime
import json

class JSONDateTimeEncoder(json.JSONEncoder):
    def default(self,obj):
        if isinstance(obj,(datetime.date, datetime.datetime)):
            return obj.isoformat()
        else:
            return json.JSONEncoder.default(self,obj)


def dumps(obj):
    return json.dumps(obj, cls=JSONDateTimeEncoder)

now_str = dumps({'times':datetime.datetime.now()}) 

print(now_str)

time_str = '2012/01/01 12:32:11'
dt = datetime.datetime.strptime(time_str,'%Y/%m/%d %H:%M:%S')
print(dt)