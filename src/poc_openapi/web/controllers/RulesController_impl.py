import six

from poc_openapi.web.models.rule import Rule  # noqa: E501
from poc_openapi.web import util

from poc_openapi.core import rules

def add_rule(body):  # noqa: E501
    rules.add_rule(body)
    return {}, 201


def delete_rule(rule_id):  # noqa: E501
    try:
        rules.remove_rule(rule_id)
        response = {}, 200
    except KeyError:
        response = {}, 404

    return response


def get_all_rules():  # noqa: E501
    allRules = rules.get_all_rules()
    return allRules, 200


def get_rule_by_id(rule_id):  # noqa: E501
    try:
        rule = rules.get_rule(rule_id)
        response = rule, 200
    except KeyError:
        response = {}, 404
    return response


def update_rule(rule_id, body):  # noqa: E501
    rules.update_rule(rule_id, body)
    return body, 200