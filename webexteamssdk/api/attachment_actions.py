# -*- coding: utf-8 -*-
"""Webex Teams Messages API wrapper.

Copyright (c) 2016-2019 Cisco and/or its affiliates.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""


from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

from builtins import *

from past.builtins import basestring
from requests_toolbelt import MultipartEncoder

from ..generator_containers import generator_container
from ..restsession import RestSession
from ..utils import (
    check_type, dict_from_items_with_values, is_local_file, is_web_url,
    open_local_file,
)


API_ENDPOINT = 'attachment/actions'
OBJECT_TYPE = 'attachment_action'


class AttachmentActionsAPI(object):
    """Webex Teams Attachment Actions API.

    Wraps the Webex Teams Attachment Actions API and exposes the API as
    native Python methods that return native Python objects.

    """

    def __init__(self, session, object_factory):
        """Init a new AttachmentActionsAPI object with the provided RestSession.

        Args:
            session(RestSession): The RESTful session object to be used for
                API calls to the Webex Teams service.

        Raises:
            TypeError: If the parameter types are incorrect.

        """
        check_type(session, RestSession, optional=False)
        super(AttachmentActionsAPI, self).__init__()
        self._session = session
        self._object_factory = object_factory

    def create(self, type=None, messageId=None, inputs=None,
               **request_parameters):
        """Create an attachment action.

        Args:
            type(attachment action enum): The type of attachment action.
            messageId(basestring): The ID of parent message the attachment
                action is to be performed on.
            inputs(dict): inputs to attachment fields
            **request_parameters: Additional request parameters (provides
                support for parameters that may be added in the future).

        Returns:
            Attachment action: A attachment action object with the details
            of the created attachment action.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.
            ValueError: If the files parameter is a list of length > 1, or if
                the string in the list (the only element in the list) does not
                contain a valid URL or path to a local file.

        """

        check_type(type, basestring, optional=False)
        check_type(messageId, basestring, optional=False)
        check_type(inputs, dict, optional=False)

        post_data = dict_from_items_with_values(
            request_parameters,
            type=type,
            messageId=messageId,
            inputs=inputs
        )

        json_data = self._session.post(API_ENDPOINT, json=post_data)

        # Return a attachment action object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)

    def get(self, attachmentId):
        """Get the details of a attachment action, by ID.

        Args:
            attachmentId(basestring): The ID of the attachment action to be
            retrieved.

        Returns:
            AttachmentAction: A Attachment Action object with the details of
            the requested attachment action.

        Raises:
            TypeError: If the parameter types are incorrect.
            ApiError: If the Webex Teams cloud returns an error.

        """
        check_type(attachmentId, basestring, optional=False)

        # API request
        json_data = self._session.get(API_ENDPOINT + '/' + attachmentId)

        # Return a message object created from the response JSON data
        return self._object_factory(OBJECT_TYPE, json_data)
