import allure
import requests


class LambdatestService:
    BASE_URL = "https://test-backend.lambdatest.com/api/dev-tools/"

    @allure.step("Send a POST request to {endpoint}")
    def _send_request(self, endpoint, input_key, input_str):
        url = self.BASE_URL + endpoint
        allure.attach(url, "Full URL", allure.attachment_type.TEXT)
        return requests.post(url, data={input_key: input_str})

    @allure.step("Send a POST request to convert JSON to XML")
    def json_to_xml(self, input_str: str) -> str:
        response = self._send_request("json-to-xml", input_key="input-str", input_str=input_str)

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response.text, "Output XML", allure.attachment_type.XML)

        return response.text

    @allure.step("Send a POST request to minify XML")
    def minify_xml(self, input_str: str) -> str:
        response = self._send_request("minify-xml", "input-str", input_str).json()["minify_data"]

        allure.attach(input_str, "Input XML", allure.attachment_type.XML)
        allure.attach(response.content, "Minified XML", allure.attachment_type.XML)

        return response

    @allure.step("Send a POST request to Extract Text from JSON")
    def extract_text_from_json(self, input_str: str) -> str:
        response = self._send_request("extract-text-json", "input-str", input_str).json()["data"]

        allure.attach(input_str, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response, "Extracted Text", allure.attachment_type.TEXT)

        return response

    @allure.step("Send a POST request to YAML Validator")
    def yaml_validator(self, input_yaml):
        response = self._send_request("yaml-validator", input_key="yaml-str", input_str=input_yaml)

        allure.attach(input_yaml, "Input yaml", allure.attachment_type.YAML)
        allure.attach(response.content, "Expected result ", allure.attachment_type.TEXT)
        return response

    @allure.step("Send a POST request to JSON to YAML converter")
    def json_to_yaml(self, input_json):
        response = self._send_request("json-to-yaml", input_key="json-str", input_str=input_json)

        allure.attach(input_json, "Input JSON", allure.attachment_type.JSON)
        allure.attach(response.content, "Output YAML", allure.attachment_type.YAML)

        return response

    @allure.step("Send a POST to XML to YAML converter")
    def xml_to_yaml(self, input_xml):
        response = self._send_request("xml-to-yaml", input_key="xml-str", input_str=input_xml)

        allure.attach(input_xml, "Input xml", allure.attachment_type.XML)
        allure.attach(response.json()["data"], "Output YAML", allure.attachment_type.YAML)
        return response

