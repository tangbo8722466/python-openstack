from keystoneauth1 import loading
from keystoneauth1 import session
from keystoneauth1.identity import v3
from novaclient import client

class nova():
    def __init__(self, version, auth_url, username, password, project_name):
        self.version = version
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project_name = project_name


    def initClient(self):
        #version 6.0.0
        # loader = loading.get_plugin_loader('password')
        # auth = loader.load_from_options(auth_url=self.auth_url, username=self.username,password=self.password,project_id=self.project_id)
        # sess = session.Session(auth=auth)
        # nova_client = client.Client(self.version, session=sess)

        #version 7.1.0
        auth = v3.Password(auth_url=self.auth_url,
        username = self.username,
        password = self.password,
        project_name = self.project_name,
        user_domain_id = 'default',
        project_domain_id = 'default')
        sess = session.Session(auth=auth)
        nova_client = client.Client(self.version, session=sess)
        return nova_client

if __name__ == "__main__":
    client = nova("2.1","http://192.168.1.200:5000/v3","admin","admin","admin").initClient()
    servers = client.servers.list()
    for server in servers:
        print server._info
    print client.servers.find(id="0e965833-b514-47e4-8186-dc1f788e5853")