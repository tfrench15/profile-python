import requests

import exceptions

class Client(object):
    """
    Client represents a client to Segment's Profile API.

    ...

    Attributes
    ----------
    base_url : str
        the host of the Profile API.
    namespace : str
        the Personas Space ID 
    secret : str
        the API token used to authenticate requests to the Profile API.

    Methods
    -------
    get_traits(id, value, include=None, verbose=None, limit=None)
        retrieves a Profile's traits
    get_events(id, value, include=None, exclude=None, start=None, end=None, limit=None, sort=None)
        retrieves a Profile's events
    get_external_ids(id, value, include=None, limit=None, verbose=None)
        retrieves a Profile's external IDs.
    get_metadata(id, value, verbose=None)
        retrieves a Profile's metadata.
    get_links(id, value)
        retrives a Profile's links.
    """
    base_url = 'https://profiles.segment.com/v1/spaces/'

    def __init__(self, namespace, secret):
        """
        Parameters
        ----------
        namespace : str
            the Personas Space ID
        secret : str
            the API token for authenticating requests
        """
        self.namespace = namespace
        self.secret = secret

    def get_traits(self, id, value, include=None, verbose=None, limit=None): 
        """get_traits makes requests against the /traits endpoint, returning a profile's traits.
        
        Parameters
        ----------
        id : str
            the id type used in the query, i.e. 'email' or 'user_id'
        value : str
            the value of the id used in the query, i.e. 'user123@domain.com' or 'abc123'
        include : list, optional
            a list of traits to specifically include in the response payload
        limit : int, optional
            a limit on the number of traits to return, must be in the range [1, 100]
        verbose : bool, optional
            flag to return verbose output or not

        Raises
        ------
        LimitError
            if the value passed in for limit is not in the range [1, 100]
        """

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
                   exclude=None, limit=None, sort=None):
        """get_events makes requests against the /events endpoint, returning a profile's events.
        
        Parameters
        ----------
        id : str
            the id type used in the query, i.e. 'email' or 'user_id'
        value : str
            the value of the id used in the query, i.e. 'user123@domain.com' or 'abc123'
        include : list[str], optional
            a list of events to specifically include in the response payload
        exclude : list[str], optional
            a list of events to specifically exclude in the response payload
        limit : int, optional
            a limit on the number of events to return, must be in the range [1, 100]
        verbose : bool, optional
            flag to return verbose output or not
        sort : str, optional
            flag to return events in sorted order
        
        Raises
        ------
        LimitError
            if the value passed in for limit is not in the range [1, 100]
        SortError
            if the value passed in for sort is not equal to 'asc' or 'desc'
        """

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
        """get_external_ids makes requests against the /external_ids endpoint, returning a profile's external IDs.
        
        Parameters
        ----------
        id : str
            the id type used in the query, i.e. 'email' or 'user_id'
        value : str
            the value of the id used in the query, i.e. 'user123@domain.com' or 'abc123'
        include : list, optional
            a list of external_ids to specifically include in the response payload
        limit : int, optional
            a limit on the number of external_ids to return, must be in the range [1, 100]
        verbose : bool, optional
            flag to return verbose output or not
        
        Raises
        ------
        LimitError
            if the value passed in for limit is not in the range [1, 100]
        """

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
        """get_metadata makes requests against the /metadata endpoint, returning a profile's metadata.
        
        Parameters
        ----------
        id : str
            the id type used in the query, i.e. 'email' or 'user_id'
        value : str
            the value of the id used in the query, i.e. 'user123@domain.com' or 'abc123'
        verbose : bool, optional
            flag to return verbose output or not
        """

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/metadata'
        params = {}

        if verbose:
            params['verbose'] = 'true'

        res = requests.get(url, params=params, auth=(self.secret, ''))
        return res.json()

    def get_links(self, id, value):
        """get_links makes requests against the /links endpoint, returning a profile's links.
        
        Parameters
        ----------
        id : str
            the id type used in the query, i.e. 'email' or 'user_id'
        value : str
            the value of the id used in the query, i.e. 'user123@domain.com' or 'abc123'
        """

        url = self.base_url + self.namespace + '/collections/users/profiles/' + id + ':' + value + '/links'

        res = requests.get(url, auth=(self.secret, ''))
        return res.json()

