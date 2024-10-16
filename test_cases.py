import unittest
from rule_engine import create_rule, evaluate_rule, combine_rules, modify_rule, ASTNode

class TestRuleEngine(unittest.TestCase):

    def test_create_rule(self):
        rule_string = "age == 30"
        ast_node = create_rule(rule_string)
        
        self.assertIsInstance(ast_node, ASTNode)
        self.assertEqual(ast_node.left, "age")
        self.assertEqual(ast_node.operator, "==")
        self.assertEqual(ast_node.right, 30)

    def test_evaluate_rule(self):
        rule_string = "age == 30"
        ast_node = create_rule(rule_string)

        sample_data = {
            'age': 30,
            'country': 'USA',
            'status': 'active'
        }
        result = ast_node.evaluate(sample_data)
        self.assertTrue(result)

    def test_combine_rules(self):
        rules = ["age == 30", "country == 'USA'"]
        combined = combine_rules(rules)
        self.assertEqual(len(combined), 2)  # Should have two ASTNodes
        self.assertEqual(str(combined[0]), "age == 30")
        self.assertEqual(str(combined[1]), "country == 'USA'")

    def test_modify_rule(self):
        rule_string = "age == 30"
        ast_node = create_rule(rule_string)

        # Modify the operator
        modify_rule(ast_node, new_operator="!=")
        self.assertEqual(ast_node.operator, "!=")

        # Modify the right value
        modify_rule(ast_node, new_right=35)
        self.assertEqual(ast_node.right, 35)

        # Modify both left and right values
        modify_rule(ast_node, new_left="age", new_right="'40'")
        self.assertEqual(ast_node.left, "age")
        self.assertEqual(ast_node.right, "'40'")

        # Test evaluation after modification
        sample_data = {'age': 30}
        result = ast_node.evaluate(sample_data)
        self.assertFalse(result)  # since 30 != 35 should be False

    def test_invalid_rule_format(self):
        with self.assertRaises(ValueError):
            create_rule("age ==")  # Missing right side
        with self.assertRaises(ValueError):
            create_rule("== 30")  # Missing left side
        with self.assertRaises(ValueError):
            create_rule("age 30")  # Invalid operator

if __name__ == "__main__":
    unittest.main()
