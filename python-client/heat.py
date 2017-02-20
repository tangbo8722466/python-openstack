# coding=utf-8

from keystoneauth1 import loading
from keystoneauth1 import session
from heatclient import client
from heatclient.client import Client as heatClient
from keystoneclient.v2_0 import client as keyStoneClient
from heatclient.common import template_utils

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
        # loader = loading.get_plugin_loader('password')
        # auth = loader.load_from_options(auth_url=self.AUTH_URL,username=self.USERNAME,password=self.PASSWORD,project_name=self.PROJECT_NAME)
        # sess = session.Session(auth=auth)
        # heat_client = client.Client('1', session=sess)

        #keystone
        keystone = keyStoneClient.Client(username=self.USERNAME, password=self.PASSWORD,
                                         tenant_name=self.PROJECT_NAME, auth_url=self.AUTH_URL)
        auth_token = keystone.auth_ref['token']['id']
        heat_url = ''
        services = keystone.auth_ref['serviceCatalog']
        for service in services:
            if service['name'] == 'heat':
                heat_url = service['endpoints'][0]['publicURL']
        heat_client = heatClient('1', endpoint=heat_url, token=auth_token)
        return heat_client

    def create_stack(self):
        # 创建stack
        path = "/var/tmp/hello_world.yaml"
        tpl_files, template = template_utils.get_template_contents(path)
        create_fields = {
            'stack_name': 'test_stack',
            'disable_rollback': 'false',
            'parameters': '',
            'template': template,
            'files': dict(list(tpl_files.items()))
        }
        heat.stacks.create(**create_fields)
    def delete_stack(self):
        # 删除Stack
        delete_fields = {
            'stack_id': 'test_stack'
        }
        heat.stacks.delete(**delete_fields)

if __name__ == "__main__":
    heat_client = heat("http://192.168.1.200:5000/v2.0","admin","admin","admin").initClient()
    stacks =  heat_client.stacks.list()
    for stack in stacks:
        print stack._info
else:
    print "init heat client"
