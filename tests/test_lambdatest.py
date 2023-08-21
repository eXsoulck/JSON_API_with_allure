import allure
import pytest

from utils.file_utils import read_data_file


@allure.suite("Conventers tests")
@allure.title("JSON to XML conversion")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_xml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_xml = read_data_file(f"xml/{file_name}.xml")

    with allure.step("Convert JSON to XML via API"):
        actual_xml = lambdatest_service.json_to_xml(input_json)

    with allure.step("Compare expected and actual XML"):
        assert actual_xml == expected_xml


@allure.suite("Text extraction")
@allure.title("Extract text from JSON")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-text")
@allure.link("https://jira.com/TEST-1234")
@allure.description("""
    This test case verifies that the API endpoint "Extract Text from JSON" works correctly.
    Steps:
    1. Prepare test data.
    2. Extract text from JSON via API.
    3. Compare expected and actual text.
""")
@pytest.mark.xfail(reason="Don't know how to get rid of space in isActive  line")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_extract_text_from_json(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        expected_text = read_data_file(f"txt/{file_name}.txt")

    with allure.step("Extract text from JSON via API"):
        actual_text = lambdatest_service.extract_text_from_json(input_json)

    with allure.step("Compare expected and actual text"):
        assert actual_text == expected_text


@allure.suite("Conventers tests")
@allure.title("Yaml validator")
@allure.link("https://www.lambdatest.com/free-online-tools/yaml-validator")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_yaml_validator(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_yaml = read_data_file(f"yaml/{file_name}.yml")

    with allure.step("Send post request to yaml-validator"):
        request = lambdatest_service.yaml_validator(input_yaml)

    with allure.step("Checking if yaml is valid"):
        assert request.json()["message"] == "Valid YAML"


@allure.suite("Conventers tests")
@allure.title("JSON to YAML converter")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_json_to_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_json = read_data_file(f"json/{file_name}.json")
        output_yaml = read_data_file(f"yaml/{file_name}.yml")
        str_output = str(output_yaml)

    with allure.step("Send post request to json to yaml"):
        request = lambdatest_service.json_to_yaml(input_json).json()["data"]

    with allure.step("Compare generated yaml file"):
        assert str(request) == str_output


@allure.suite("Conventers tests")
@allure.title("XML to YAML converter")
@allure.link("https://www.lambdatest.com/free-online-tools/json-to-yaml")
@pytest.mark.parametrize("file_name", ["1", "2"])
def test_xml_yaml(lambdatest_service, file_name):
    with allure.step("Prepare test data"):
        input_xml = read_data_file(f"xml/{file_name}.xml")
        output_yaml = read_data_file(f"yaml/{file_name}.yml")
        expected_text = lambdatest_service.extract_text_from_json(output_yaml)

    with allure.step("Send POST request to xml to yaml converter , extract text from "):
        response = lambdatest_service.xml_to_yaml(input_xml).json()["data"]

    with allure.step("Compare results"):
        actual_text = lambdatest_service.extract_text_from_json(response)

        assert actual_text == expected_text

# HOME TASK
# Add tests for the following API endpoints (3 of them):
# https://www.lambdatest.com/free-online-tools/yaml-validator
# https://www.lambdatest.com/free-online-tools/json-to-yaml
# https://www.lambdatest.com/free-online-tools/xml-to-yaml
# https://www.lambdatest.com/free-online-tools/yaml-to-json
