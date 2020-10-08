import connexion
import six

from poc_openapi.web.models.rule import Rule  # noqa: E501
from poc_openapi.web.models.rules import Rules
from poc_openapi.web import util

from poc_openapi.core import rules


def add_rule(body):  # noqa: E501
    """Add a new rule to opengate

     # noqa: E501

    :param body: Rule object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    rules.add_rule(body)
    return {}, 201


def delete_rule(ruleId, api_key=None):  # noqa: E501
    """Deletes a rule

     # noqa: E501

    :param ruleId: Rule id to delete
    :type ruleId: str
    :param api_key: 
    :type api_key: str

    :rtype: None 
    """
    return 'do some magic!'


def get_rule_by_id(ruleId):  # noqa: E501
    """Find rule by ID

    Returns a single rule # noqa: E501

    :param ruleId: ID of rule to return
    :type ruleId: str

    :rtype: Rule
    """
    try:
        rule = rules.get_rule(ruleId)
        response = rule, 200
    except KeyError:
        response = {}, 404
    return response


def update_rule(ruleId, name=None, javascript=None):  # noqa: E501
    """Updates a rule in the opengate platform

     # noqa: E501

    :param ruleId: ID of rule that needs to be updated
    :type ruleId: str
    :param name: Updated name of the rule
    :type name: str
    :param javascript: Updated javascript of the rule
    :type javascript: str

    :rtype: None
    """
    return 'do some magic!'
