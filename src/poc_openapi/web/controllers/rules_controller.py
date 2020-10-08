import connexion
import six

from poc_openapi.web.models.rule import Rule  # noqa: E501
from poc_openapi.web.models.rules import Rules  # noqa: E501
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


def delete_rule(rule_id):  # noqa: E501
    """Deletes a rule

     # noqa: E501

    :param rule_id: Rule id to delete
    :type rule_id: str

    :rtype: None
    """
    try:
        rules.remove_rule(rule_id)
        response = {}, 200
    except KeyError:
        response = {}, 404

    return response


def get_all_rules():  # noqa: E501
    """Gets all rules

     # noqa: E501


    :rtype: Rules
    """
    allRules = rules.get_all_rules()
    return allRules, 200


def get_rule_by_id(rule_id):  # noqa: E501
    """Find rule by ID

     # noqa: E501

    :param rule_id: ID of rule to return
    :type rule_id: str

    :rtype: Rule
    """
    try:
        rule = rules.get_rule(rule_id)
        response = rule, 200
    except KeyError:
        response = {}, 404
    return response


def update_rule(rule_id, Rule):  # noqa: E501
    """Updates a rule in the opengate platform

     # noqa: E501

    :param rule_id: ID of rule that needs to be updated
    :type rule_id: str
    :param Rule: 
    :type Rule: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        Rule = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
