# Copyright (c) 2014 VMware, Inc.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from oslo.vmware import service


class Vim(service.Service):
    """Service class that provides access to the VIM API."""

    def __init__(self, protocol='https', host='localhost', port=None,
                 wsdl_url=None):
        """Constructs a VIM service client object.

        :param protocol: http or https
        :param host: server IP address or host name
        :param port: port for connection
        :param wsdl_url: VIM WSDL url
        :raises: VimException, VimFaultException, VimAttributeException,
                 VimSessionOverLoadException, VimConnectionException
        """
        base_url = service.Service.build_url(protocol, host, port)
        self.soap_url = base_url + '/sdk'
        if wsdl_url is None:
            wsdl_url = self.soap_url + '/vimService.wsdl'
        self.wsdl_url = wsdl_url
        super(Vim, self).__init__(self.wsdl_url, self.soap_url)

    def retrieve_service_content(self):
        return self.RetrieveServiceContent('ServiceInstance')
