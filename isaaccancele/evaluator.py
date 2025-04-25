from isaaccancele.ast import *
from isaaccancele.evaluator_objects import Integer, Boolean, TRUE, FALSE, Function
from isaaccancele.Enviroment import Environment

# Entorno global
global_env = Environment()

def eval_node(node, env=global_env):
    if isinstance(node, Program):
        return eval_program(node, env)
    elif isinstance(node, ExpressionStatement):
        return eval_node(node.expression, env)
    elif isinstance(node, LetStatement):
        value = eval_node(node.value, env)
        env.set(node.name.value, value)
        return value
    elif isinstance(node, IntegerLiteral):
        return Integer(node.value)
    elif isinstance(node, PrefixExpression):
        right = eval_node(node.right, env)
        return eval_prefix_expression(node.operator, right)
    elif isinstance(node, InfixExpression):
        left = eval_node(node.left, env)
        right = eval_node(node.right, env)
        return eval_infix_expression(node.operator, left, right)
    elif isinstance(node, IfExpression):
        return eval_if_expression(node, env)
    elif isinstance(node, BlockStatement):
        return eval_block_statement(node, env)
    elif isinstance(node, Identifier):
        return env.get(node.value)
    elif isinstance(node, WhileStatement):
        return eval_while_statement(node, env)
    elif isinstance(node, ForStatement):
        return eval_for_statement(node, env)
    elif isinstance(node, AssignStatement):
        value = eval_node(node.value, env)
        env.set(node.name.value, value)
        return value
    elif isinstance(node, FunctionLiteral):
        return Function(node.parameters, node.body, env)
    elif isinstance(node, CallExpression):
        function = eval_node(node.function, env)
        args = [eval_node(arg, env) for arg in node.arguments]
        return apply_function(function, args)

def eval_program(program: Program, env):
    result = None
    for stmt in program.statements:
        result = eval_node(stmt, env)
        if result is not None:
            print(result.inspect())
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
    elif operator == "!=" :
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

def eval_if_expression(if_expr, env):
    condition = eval_node(if_expr.condition, env)
    if is_truthy(condition):
        return eval_node(if_expr.consequence, env)
    elif if_expr.alternative:
        return eval_node(if_expr.alternative, env)
    return None

def eval_block_statement(block, env):
    result = None
    for stmt in block.statements:
        result = eval_node(stmt, env)
    return result

def is_truthy(obj):
    if obj is None:
        return False
    if isinstance(obj, Boolean):
        return obj.value
    if isinstance(obj, Integer):
        return obj.value != 0
    return True

def eval_while_statement(stmt, env):
    result = None
    while is_truthy(eval_node(stmt.condition, env)):
        result = eval_node(stmt.body, env)
    return result

def eval_for_statement(stmt, env):
    eval_node(stmt.init, env)
    result = None
    while is_truthy(eval_node(stmt.condition, env)):
        result = eval_node(stmt.body, env)
        eval_node(stmt.post, env)
    return result

def apply_function(fn, args):
    if not isinstance(fn, Function):
        raise Exception(f"Cannot call non-function object: {fn.type()}")

    extended_env = Environment(outer=fn.env)

    for param, arg in zip(fn.parameters, args):
        extended_env.set(param.value, arg)

    return eval_node(fn.body, extended_env)