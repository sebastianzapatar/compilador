from anytree import Node, RenderTree
from isaaccancele.ast import Program, LetStatement, Identifier

def visualize_ast(program: Program):
    root = Node("Program")

    for stmt in program.statements:
        if isinstance(stmt, LetStatement):
            stmt_node = Node("LetStatement", parent=root)
            Node(f"name: {stmt.name.value}", parent=stmt_node)
            if isinstance(stmt.value, Identifier):
                Node(f"value: {stmt.value.value}", parent=stmt_node)
            else:
                Node("value: <unknown>", parent=stmt_node)

    for pre, fill, node in RenderTree(root):
        print(f"{pre}{node.name}")