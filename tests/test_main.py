import os
import re

from main import analyze_lua_script, check_obfuscation, calculate_entropy


def test_calculate_entropy() -> None:
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith(".lua"):
            with open(file_name, "r") as file:
                script_content = file.read()
                for match in re.findall(r'["\']([^"\']+)["\']', script_content):
                    if file_name == "test_clean.lua":
                        assert calculate_entropy(match) == 3.5368867237421675
                    elif file_name == "test_clean_loadstring.lua":
                        assert calculate_entropy(match) == 2.822294684942814
                    elif file_name == "backtrack_lines.lua":
                        assert calculate_entropy(match) < 4.0

    assert calculate_entropy(None) == 0.0


def test_check_obfuscation() -> None:
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith(".lua"):
            with open(file_name, "r") as file:
                script_content = file.read()
                if file_name == "test_clean.lua":
                    assert check_obfuscation(script_content) is False
                elif file_name == "test_clean_obfuscated.lua":
                    assert check_obfuscation(script_content) is True
                elif file_name == "test_clean_loadstring.lua":
                    assert check_obfuscation(script_content) is True
                elif file_name == "backtrack_lines.lua":
                    assert check_obfuscation(script_content) is False

    assert (
        check_obfuscation(
            'local data = "aZx3!@#$%^&*()_+=-1234567890qwertyuiop[]{}|;:,.<>?/`~AaBbCcDdEeFfGgHhIiJj"'
        )
        is True
    )

    assert check_obfuscation("".join(["a" for _ in range(1001)])) is True


def test_analyze_lua_script() -> None:
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith(".lua"):
            with open(file_name, "r") as file:
                script_content = file.read()
                if file_name == "test_clean.lua":
                    result = analyze_lua_script(script_content)
                    assert result["status"] == "approved"
                elif file_name == "test_clean_obfuscated.lua":
                    result = analyze_lua_script(script_content)
                    assert result["status"] == "flagged"
                    assert result["reason"] == "Possible infinite loop"
                elif file_name == "test_clean_loadstring.lua":
                    result = analyze_lua_script(script_content)
                    assert result["status"] == "flagged"
                    assert result["reason"] == "Contains loadstring"
                elif file_name == "backtrack_lines.lua":
                    result = analyze_lua_script(script_content)
                    assert result["status"] == "approved"

    result = analyze_lua_script(
        'local data = "aZx3!@#$%^&*()_+=-1234567890qwertyuiop[]{}|;:,.<>?/`~AaBbCcDdEeFfGgHhIiJj"'
    )
    assert result["status"] == "flagged"
    assert result["reason"] == "Possible obfuscation detected"


def test_analyze_lua_script_exception():
    result = analyze_lua_script("error('Hello, world!')")
    assert result["status"] == "flagged"
    assert "Error during execution:" in result["reason"]
