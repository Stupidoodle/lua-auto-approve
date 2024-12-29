import os
from fastapi.testclient import TestClient
from main import app, analyze_lua_script

client = TestClient(app)


def test_analyze_script():
    for file_name in os.listdir(os.getcwd()):
        if file_name.endswith(".lua"):
            with open(file_name, "rb") as file:
                script_content = file.read().decode("utf-8")
                response = client.post(
                    "/analyze-script",
                    files={"file": (file_name, file, "text/plain")},
                )
                assert response.status_code == 200
                assert response.json() == analyze_lua_script(script_content)


def test_analyze_script_invalid_file_type():
    response = client.post(
        "/analyze-script",
        files={"file": ("test.txt", b"print('Hello, world!')", "text/plain")},
    )
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Invalid file type. Only .lua files are allowed."
    }
