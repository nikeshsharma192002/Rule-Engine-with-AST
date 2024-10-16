class ASTNode:
    def __init__(self, left, operator, right):
        self.left = left
        self.operator = operator
        self.right = right

    def __str__(self):
        return f"{self.left} {self.operator} {self.right}"

    def evaluate(self, data):
        left_value = data.get(self.left) if isinstance(self.left, str) else self.left
        
        if isinstance(self.right, str) and self.right.startswith("'") and self.right.endswith("'"):
            right_value = self.right.strip("'")
        else:
            right_value = data.get(self.right) if isinstance(self.right, str) else self.right

        if isinstance(right_value, str):
            return left_value == right_value
        else:
            return eval(f"{left_value} {self.operator} {right_value}")

    def change_operator(self, new_operator):
        """Change the operator of the current node."""
        valid_operators = ["==", "!=", "<", "<=", ">", ">="]
        if new_operator not in valid_operators:
            raise ValueError(f"Invalid operator: {new_operator}")
        self.operator = new_operator

    def change_value(self, new_left=None, new_right=None):
        """Change the left and/or right operand of the node."""
        if new_left is not None:
            self.left = new_left
        if new_right is not None:
            if isinstance(new_right, str) and not (new_right.startswith("'") and new_right.endswith("'")):
                new_right = f"'{new_right}'"  # Enclose string literals in quotes
            self.right = new_right


def create_rule(rule_string):
    parts = rule_string.split()
    
    # Validate rule format: should consist of exactly three parts
    if len(parts) != 3:
        raise ValueError(f"Invalid rule format: {rule_string}")

    left = parts[0]
    operator = parts[1]
    right = parts[2].strip("'\"")

    # Validate operator
    if operator not in ["==", "!=", "<", "<=", ">", ">="]:
        raise ValueError(f"Invalid operator in rule: {operator}")

    # If the right side is not a number, we assume it's a string
    if right.isdigit():
        right = int(right)
    elif right.startswith("'") and right.endswith("'"):
        right = right  # It's a string literal, keep it as is
    else:
        right = f"'{right}'"  # Enclose string literals in quotes

    return ASTNode(left, operator, right)

def parse_expression(expression):
    if " AND " in expression:
        rules = expression.split(" AND ")
        return [create_rule(rule.strip()) for rule in rules]
    else:
        return [create_rule(expression)]


def combine_rules(rules):
    if not rules:
        return []

    combined_rule = " AND ".join(rules)
    return parse_expression(combined_rule)


def evaluate_rule(ast_nodes, data):
    return all(node.evaluate(data) for node in ast_nodes)

def modify_rule(ast_node, new_operator=None, new_left=None, new_right=None):
    """Modify an existing rule represented by an ASTNode."""
    if new_operator:
        ast_node.change_operator(new_operator)
    if new_left or new_right:
        ast_node.change_value(new_left, new_right)
