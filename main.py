from rule_engine import create_rule, evaluate_rule, modify_rule

def main():
    # Create an initial rule
    rule_string = "age == 30"
    ast_node = create_rule(rule_string)

    print("Original Rule:", ast_node)

    # Modify the rule
    modify_rule(ast_node, new_operator="!=", new_right=35)
    print("Modified Rule:", ast_node)

    # Evaluate the modified rule
    sample_data = {
        'age': 30,
        'country': 'USA',
        'status': 'active'
    }
    result = ast_node.evaluate(sample_data)
    print("Evaluation Result:", result)

if __name__ == "__main__":
    main()
