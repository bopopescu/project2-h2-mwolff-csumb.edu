# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Library for working with Firebase Test Lab service endpoints."""

from googlecloudsdk.api_lib.test import exceptions
from googlecloudsdk.core import log
from googlecloudsdk.core import properties


def ValidateTestServiceEndpoints():
  """Ensure that test-service endpoints are compatible with each other.

  A staging/test ToolResults API endpoint will not work correctly with a
  production Testing API endpoint, and vice versa. This check is only relevant
  for internal development.

  Raises:
    IncompatibleApiEndpointsError if the endpoints are not compatible.
  """
  testing_url = properties.VALUES.api_endpoint_overrides.testing.Get()
  toolresults_url = properties.VALUES.api_endpoint_overrides.toolresults.Get()
  log.info('Test Service endpoint: [{0}]'.format(testing_url))
  log.info('Tool Results endpoint: [{0}]'.format(toolresults_url))
  if ((toolresults_url is None or 'apis.com/toolresults' in toolresults_url)
      != (testing_url is None or 'testing.googleapis' in testing_url)):
    raise exceptions.IncompatibleApiEndpointsError(
        testing_url, toolresults_url)
