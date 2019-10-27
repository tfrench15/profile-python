import requests

import exceptions

class Client(object):
    """Client represents a client to Segment's Profile API."""
    base_url = 'https://profiles.segment.com/v1/spaces/'

    def __init__(self, namespace, secret):
        self.namespace = namespace
        self.secret = secret

    def get_traits(self, id, value, include=None, verbose=None, limit=None): 
        """get_traits makes requests against the /traits endpoint, returning a profile's traits."""

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/traits'
        params = {}
        if include:
            params['include'] = ','.join(include)
        
        if verbose:
            params['verbose'] = 'true'

        if limit:
            if limit >= 1 and limit <=100:
                params['limit'] = str(limit)
            else:
                raise exceptions.LimitError(limit, 'limit must be between 1 and 100 inclusive')

        res = requests.get(url, params=params, auth=(self.secret, ''))
        return res.json()

    def get_events(self, id, value, include=None, 
                   exclude=None, start=None, end=None, 
                   limit=None, sort=None):
        """get_events makes requests against the /events endpoint, returning a profile's events."""

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/events'
        params = {}

        if include:
            params['include'] = ','.join(include)
        
        if exclude:
            params['exclude'] = ','.join(exclude)

        if limit:
            if limit < 1 or limit > 100:
                raise exceptions.LimitError(limit, 'limit must be between 1 and 100 inclusive')
            else:
                params['limit'] = str(limit)

        if sort:
            if sort != 'asc' or sort != 'desc':
                raise exceptions.SortError(sort, 'sort must be "asc" or "desc"')
            else:
                params['sort'] = sort
                
        res = requests.get(url, params=params, auth=(self.secret, ''))
        return res.json()
        

    def get_external_ids(self, id, value, verbose=None, 
                         include=None, limit=None):
        """get_external_ids makes requests against the /external_ids endpoint, returning a profile's external IDs."""

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/external_ids'
        params = {}

        if include:
            params['include'] = ','.join(include)
        
        if limit:
            if limit < 1 or limit > 100:
                raise exceptions.LimitError(limit, 'limit must be between 1 and 100 inclusive')
            else:
                params['limit'] = str(limit)

        if verbose:
            params['verbose'] = 'true'

        res = requests.get(url, params=params, auth=(self.secret, ''))
        return res.json()

    def get_metadata(self, id, value, verbose=None):
        """get_metadata makes requests against the /metadata endpoint, returning a profile's metadata."""

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/metadata'
        params = {}

        if verbose:
            params['verbose'] = 'true'

        res = requests.get(url, params=params, auth=(self.secret, ''))
        return res.json()

    def get_links(self, id, value):
        """get_links makes requests against the /links endpoint, returning a profile's links."""

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/links'

        res = requests.get(url, auth=(self.secret, ''))
        return res.json()

