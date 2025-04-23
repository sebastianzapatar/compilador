# evaluator.py

from isaaccancele.ast import *
from isaaccancele.evaluator_objects import Integer, Boolean, TRUE, FALSE

# Entorno global para almacenar variables
environment = {}

def eval_node(node):
    if isinstance(node, Program):
        return eval_program(node)
    elif isinstance(node, ExpressionStatement):
        return eval_node(node.expression)
       
    elif isinstance(node, LetStatement):
        # Evaluar la expresión y almacenar en el entorno
        value = eval_node(node.value)
        environment[node.name.value] = value
        return value
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    elif isinstance(node, PrefixExpression):
        right = eval_node(node.right)
        return eval_prefix_expression(node.operator, right)
    elif isinstance(node, InfixExpression):
        left = eval_node(node.left)
        right = eval_node(node.right)
        return eval_infix_expression(node.operator, left, right)
    elif isinstance(node, Identifier):
        # Acceder a variables previamente definidas
        return environment.get(node.value, None)

def eval_program(program: Program):
    result = None
    for stmt in program.statements:
        result = eval_node(stmt)
    return result

def eval_prefix_expression(operator: str, right):
    if operator == "!":
        return eval_bang_operator(right)
    elif operator == "-":
        if right.type() == "INTEGER":
            return Integer(-right.value)
    return None

def eval_bang_operator(obj):
    if obj is TRUE:
        return FALSE
    elif obj is FALSE:
        return TRUE
    elif isinstance(obj, Integer) and obj.value == 0:
        return TRUE
    else:
        return FALSE

def eval_infix_expression(operator: str, left, right):
    if left.type() == "INTEGER" and right.type() == "INTEGER":
        return eval_integer_infix(operator, left, right)
    elif operator == "==":
        return TRUE if left.value == right.value else FALSE
    elif operator == "!=":
        return TRUE if left.value != right.value else FALSE
    return None

def eval_integer_infix(operator: str, left: Integer, right: Integer):
    if operator == "+":
        return Integer(left.value + right.value)
    elif operator == "-":
        return Integer(left.value - right.value)
    elif operator == "*":
        return Integer(left.value * right.value)
    elif operator == "/":
        return Integer(left.value // right.value)
    elif operator == "<":
        return TRUE if left.value < right.value else FALSE
    elif operator == ">":
        return TRUE if left.value > right.value else FALSE
    elif operator == "<=":
        return TRUE if left.value <= right.value else FALSE
    elif operator == ">=":
        return TRUE if left.value >= right.value else FALSE
    elif operator == "==":
        return TRUE if left.value == right.value else FALSE
    elif operator == "!=":
        return TRUE if left.value != right.value else FALSE
    return None
