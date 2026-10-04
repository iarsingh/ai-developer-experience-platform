from fastapi.testclient import TestClient
from aidevex.main import app

client = TestClient(app)


def test_pass_and_fail():
    good = client.post("/check", json={'docs': True, 'ci': True, 'preview': True}).json()
    assert good["passed"] is True
    assert good["applied"] is False
    bad = client.post("/check", json={'docs': True, 'ci': True}).json()
    assert bad["passed"] is False
    assert "preview" in bad["failed"]
