class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def execute(self, query, variables=None):
        return post(self.endpoint, json=dict(query=query, variables=variables), headers=self.headers).json()

    def add_header(self, name, value):
        self.headers[name] = value
