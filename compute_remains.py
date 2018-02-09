import datetime

now = datetime.datetime.now()
ddl = datetime.datetime(2018, 2, 13, 9)

remain = ddl - now
print("%.2f" % (remain.total_seconds() / 3600))
