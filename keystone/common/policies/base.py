# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

IDENTITY = 'identity:%s'
RULE_ADMIN_REQUIRED = 'rule:admin_required'
RULE_ADMIN_OR_OWNER = 'rule:admin_or_owner'


rules = [
    policy.RuleDefault(
        name='admin_required',
        check_str='role:admin or is_admin:1'),
    policy.RuleDefault(
        name='service_role',
        check_str='role:service'),
    policy.RuleDefault(
        name='service_or_admin',
        check_str='rule:admin_required or rule:service_role'),
    policy.RuleDefault(
        name='owner',
        check_str='user_id:%(user_id)s'),
    policy.RuleDefault(
        name='admin_or_owner',
        check_str='rule:admin_required or rule:owner'),
    policy.RuleDefault(
        name='token_subject',
        check_str='user_id:%(target.token.user_id)s'),
    policy.RuleDefault(
        name='admin_or_token_subject',
        check_str='rule:admin_required or rule:token_subject'),
    policy.RuleDefault(
        name='service_admin_or_token_subject',
        check_str='rule:service_or_admin or rule:token_subject'),
    policy.RuleDefault(
        name='default',
        check_str='rule:admin_required')
]


def list_rules():
    return rules
