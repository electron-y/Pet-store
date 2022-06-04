from src.conditions_ import Conditions


class AssertableResponse:

    def __init__(self, response):
        self.response = response
        self.condition = Conditions(self.response.json())

    def should_have_status_code(self, status_code):
        assert self.response.status_code == status_code, f'{self.response.status_code} | {status_code}: \n ' \
                                                         f'{self.condition.show_response_body()}'

    def should_have_body_field(self, field_name, field_value=False):
        assert self.condition.have_field(field_name) is True

        if field_value:
            assert self.condition.field_have_value(field_name, field_value) is True

    def does_str_in_value(self, field_name, field_value):
        assert self.condition.does_str_in_value(field_name, field_value)
