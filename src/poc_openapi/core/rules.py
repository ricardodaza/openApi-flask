import json
import os.path
import uuid


def get_all_rules():
    rules = read_from_file()
    rules_in_store = []
    for k, v in rules.items():
        current_rule = {"identifier": k, **v}
        rules_in_store.append(current_rule)

    return rules


def remove_rule(id):
    rules = read_from_file()
    del rules[id]
    write_to_file(rules)


def update_rule(id, rule):
    rules = read_from_file()
    rules[id] = rule
    write_to_file(rules)


def add_rule(rule):
    rules = read_from_file()
    new_id = str(uuid.uuid1())
    rules[new_id] = {"identifier": str(new_id), "name": rule.name, "organization": rule.organization, "channel": rule.channel, "javascript": rule.javascript}
    write_to_file(rules)


def get_rule(id):
    rules = read_from_file()
    rule = rules[id]
    return rule


def write_to_file(content):
    with open(os.path.abspath("src/poc_openapi/core/rules.json"), "w") as rules:
        rules.write(json.dumps(content))


def read_from_file():
    with open(os.path.abspath("src/poc_openapi/core/rules.json"), "r") as rules:
        return json.loads(rules.read())