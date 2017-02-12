# coding=utf-8

from keystoneauth1 import loading
from keystoneauth1 import session
from heatclient import client

class heat():
    # export
    # OS_USERNAME = admin
    # export
    # OS_PASSWORD = b42a6657ab1d4399
    # export
    # OS_AUTH_URL = http: // 192.168
    # .1
    # .200:5000 / v2
    # .0
    # export
    # PS1 = '[\u@\h \W(keystone_admin)]\$ '
    # export
    # OS_TENANT_NAME = admin
    # export
    # OS_REGION_NAME = RegionOne
    def __init__(self, AUTH_URL,USERNAME,PASSWORD,PROJECT_NAME):
        self.AUTH_URL=AUTH_URL
        self.USERNAME=USERNAME
        self.PASSWORD=PASSWORD
        # self.PROJECT_ID=PROJECT_ID
        self.PROJECT_NAME = PROJECT_NAME

    def initClient(self):
        loader = loading.get_plugin_loader('password')
        auth = loader.load_from_options(auth_url=self.AUTH_URL,username=self.USERNAME,password=self.PASSWORD,project_name=self.PROJECT_NAME)
        sess = session.Session(auth=auth)
        heat_client = client.Client('1', session=sess)
        return heat_client

if __name__ == "__main__":
    heat_client = heat("http://192.168.1.200:5000/v2.0","admin","b42a6657ab1d4399","admin").initClient()
    stacks =  heat_client.stacks.list()
    for stack in stacks:
        print stack._info
else:
    print "init heat client"
