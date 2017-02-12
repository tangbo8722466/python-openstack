from keystoneauth1 import identity
from keystoneauth1 import session
from neutronclient.v2_0 import client

class neutorn():
    def __init__(self, auth_url, username, password, project_name):
        self.auth_url = auth_url
        self.username = username
        self.password = password
        self.project_name = project_name

    def initClient(self):
        # v3
        # username='username'
        # password='password'
        # project_name='demo'
        # project_domain_id='default'
        # user_domain_id='default'
        # auth_url='http://auth.example.com:5000/v3'
        # auth = identity.Password(auth_url=self.auth_url, username=self.username,password=self.password,project_name=self.project_name,project_domain_id=project_domain_id,user_domain_id=user_domain_id)
        # sess = session.Session(auth=auth)
        # neutron_client = client.Client(session=sess)

        #v2
        auth = identity.Password(auth_url=self.auth_url,username = self.username,password = self.password,project_name = self.project_name)
        sess = session.Session(auth=auth)
        neutron_client = client.Client(session=sess)
        return neutron_client

if __name__ == "__main__":
    client = neutorn("http://192.168.1.200:5000/v2.0","admin","b42a6657ab1d4399","admin").initClient()
    network = {'name': 'mynetwork', 'admin_state_up': True}
    client.create_network({'network': network})
    networks = client.list_networks(name='mynetwork')
    print networks
    network_id = networks['networks'][0]['id']
    client.delete_network(network_id)

    networks = client.list_networks()
    print networks