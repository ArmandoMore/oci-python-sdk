# coding: utf-8
# Copyright (c) 2016, 2019, Oracle and/or its affiliates. All rights reserved.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ApiSpecificationRoute(object):
    """
    A single route that forwards requests to a particular backend and may contain some additional policies.
    """

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "ANY"
    METHODS_ANY = "ANY"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "HEAD"
    METHODS_HEAD = "HEAD"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "GET"
    METHODS_GET = "GET"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "POST"
    METHODS_POST = "POST"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "PUT"
    METHODS_PUT = "PUT"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "PATCH"
    METHODS_PATCH = "PATCH"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "DELETE"
    METHODS_DELETE = "DELETE"

    #: A constant which can be used with the methods property of a ApiSpecificationRoute.
    #: This constant has a value of "OPTIONS"
    METHODS_OPTIONS = "OPTIONS"

    def __init__(self, **kwargs):
        """
        Initializes a new ApiSpecificationRoute object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param path:
            The value to assign to the path property of this ApiSpecificationRoute.
        :type path: str

        :param methods:
            The value to assign to the methods property of this ApiSpecificationRoute.
            Allowed values for items in this list are: "ANY", "HEAD", "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type methods: list[str]

        :param request_policies:
            The value to assign to the request_policies property of this ApiSpecificationRoute.
        :type request_policies: ApiSpecificationRouteRequestPolicies

        :param logging_policies:
            The value to assign to the logging_policies property of this ApiSpecificationRoute.
        :type logging_policies: ApiSpecificationLoggingPolicies

        :param backend:
            The value to assign to the backend property of this ApiSpecificationRoute.
        :type backend: ApiSpecificationRouteBackend

        """
        self.swagger_types = {
            'path': 'str',
            'methods': 'list[str]',
            'request_policies': 'ApiSpecificationRouteRequestPolicies',
            'logging_policies': 'ApiSpecificationLoggingPolicies',
            'backend': 'ApiSpecificationRouteBackend'
        }

        self.attribute_map = {
            'path': 'path',
            'methods': 'methods',
            'request_policies': 'requestPolicies',
            'logging_policies': 'loggingPolicies',
            'backend': 'backend'
        }

        self._path = None
        self._methods = None
        self._request_policies = None
        self._logging_policies = None
        self._backend = None

    @property
    def path(self):
        """
        **[Required]** Gets the path of this ApiSpecificationRoute.
        A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers
        to allow wildcard and parameterized matching.


        :return: The path of this ApiSpecificationRoute.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """
        Sets the path of this ApiSpecificationRoute.
        A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers
        to allow wildcard and parameterized matching.


        :param path: The path of this ApiSpecificationRoute.
        :type: str
        """
        self._path = path

    @property
    def methods(self):
        """
        Gets the methods of this ApiSpecificationRoute.
        A list of allowed methods on this route.

        Allowed values for items in this list are: "ANY", "HEAD", "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The methods of this ApiSpecificationRoute.
        :rtype: list[str]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        """
        Sets the methods of this ApiSpecificationRoute.
        A list of allowed methods on this route.


        :param methods: The methods of this ApiSpecificationRoute.
        :type: list[str]
        """
        allowed_values = ["ANY", "HEAD", "GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"]
        if methods:
            methods[:] = ['UNKNOWN_ENUM_VALUE' if not value_allowed_none_or_none_sentinel(x, allowed_values) else x for x in methods]
        self._methods = methods

    @property
    def request_policies(self):
        """
        Gets the request_policies of this ApiSpecificationRoute.

        :return: The request_policies of this ApiSpecificationRoute.
        :rtype: ApiSpecificationRouteRequestPolicies
        """
        return self._request_policies

    @request_policies.setter
    def request_policies(self, request_policies):
        """
        Sets the request_policies of this ApiSpecificationRoute.

        :param request_policies: The request_policies of this ApiSpecificationRoute.
        :type: ApiSpecificationRouteRequestPolicies
        """
        self._request_policies = request_policies

    @property
    def logging_policies(self):
        """
        Gets the logging_policies of this ApiSpecificationRoute.

        :return: The logging_policies of this ApiSpecificationRoute.
        :rtype: ApiSpecificationLoggingPolicies
        """
        return self._logging_policies

    @logging_policies.setter
    def logging_policies(self, logging_policies):
        """
        Sets the logging_policies of this ApiSpecificationRoute.

        :param logging_policies: The logging_policies of this ApiSpecificationRoute.
        :type: ApiSpecificationLoggingPolicies
        """
        self._logging_policies = logging_policies

    @property
    def backend(self):
        """
        **[Required]** Gets the backend of this ApiSpecificationRoute.

        :return: The backend of this ApiSpecificationRoute.
        :rtype: ApiSpecificationRouteBackend
        """
        return self._backend

    @backend.setter
    def backend(self, backend):
        """
        Sets the backend of this ApiSpecificationRoute.

        :param backend: The backend of this ApiSpecificationRoute.
        :type: ApiSpecificationRouteBackend
        """
        self._backend = backend

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other