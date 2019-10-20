import requests

class Client(object):

    base_url = 'https://profiles.segment.com/v1/spaces/'

    def __init__(self, namespace, secret):
        self.namespace = namespace
        self.secret = secret

    def get_traits(self, id, value, include=None, verbose=None, limit=None): 
        url = self.base_url + self.namespace + 'collections/users/profiles/' + id + ':' + value + '/traits'
        params = {}
        if include:
            params['include'] = ','.join(include)
        
        if verbose:
            params['verbose'] = 'true'

        if limit:
            params['limit'] = str(limit)

        if len(params) > 0:
            r = requests.get(url, params=params)
        else:
            r = requests.get(url)

        return r.json()

    def get_events(self, id, value, include=None, 
                   exclude=None, start=None, end=None, 
                   limit=None, sort=None):
        url = self.base_url + self.namespace + 'collections/users/profiles/' + id + ':' + value + '/traits'
        params = {}

        if include:
            params['include'] = ','.join(include)
        
        if exclude:
            params['exclude'] = ','.join(exclude)

        if limit:
            params['limit'] = str(limit)

        if sort:
            if sort != 'asc' or sort != 'desc':
                raise
            params['sort'] = sort

    def get_external_ids(self, id, value):
        pass

    def get_metadata(self, id, value):
        pass

    def get_links(self, id, value):
        pass

    