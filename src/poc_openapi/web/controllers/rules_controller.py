import connexion
import six

from poc_openapi.web.models.rule import Rule  # noqa: E501
from poc_openapi.web.controllers import RulesController_impl
from poc_openapi.web import util


def add_rule(body):  # noqa: E501
    """Add a new rule to opengate

     # noqa: E501

    :param body: Rule object
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    return RulesController_impl.add_rule(body)


def delete_rule(rule_id):  # noqa: E501
    """Deletes a rule

     # noqa: E501

    :param rule_id: Rule id to delete
    :type rule_id: str

    :rtype: None
    """
    return RulesController_impl.delete_rule(rule_id)


def get_all_rules():  # noqa: E501
    """Gets all rules

     # noqa: E501


    :rtype: List[Rule]
    """
    return RulesController_impl.get_all_rules()


def get_rule_by_id(rule_id):  # noqa: E501
    """Find rule by ID

     # noqa: E501

    :param rule_id: ID of rule to return
    :type rule_id: str

    :rtype: Rule
    """
    return RulesController_impl.get_rule_by_id(rule_id)


def update_rule(rule_id, body):  # noqa: E501
    """Updates a rule in the opengate platform

     # noqa: E501

    :param rule_id: ID of rule that needs to be updated
    :type rule_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = Rule.from_dict(connexion.request.get_json())  # noqa: E501
    return RulesController_impl.update_rule(rule_id, body)
