from jsonpath_rw import parse


class Conditions:

    def __init__(self, body):
        self.body = body

    def field_have_value(self, key, value):
        expr = f"$..{key}"
        jsonpath_expr = parse(expr)
        values = [match.value for match in jsonpath_expr.find(self.body)]

        if value not in values:
            return False
        else:
            return True

    def have_field(self, key):
        expr = f"$..{key}"
        jsonpath_expr = parse(expr)
        values = [match.value for match in jsonpath_expr.find(self.body)]

        if len(values) == 0:
            return False
        else:
            return True

    def get_params_request(self, key):
        expr = f"$..{key}"
        jsonpath_expr = parse(expr)
        values = [match.value for match in jsonpath_expr.find(self.body)]
        return values

    def show_response_body(self):
        return self.body

    def does_str_in_value(self, key, value):
        expr = f"$..{key}"
        jsonpath_expr = parse(expr)
        values = str([match.value for match in jsonpath_expr.find(self.body)])

        if value not in values:
            return False
        else:
            return True
