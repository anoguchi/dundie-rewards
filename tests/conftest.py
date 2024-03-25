import pytest

MARKER = """\
unit: mark a test as a unit test
integration: mark a test as an integration test
high: High priority test
medium: Medium priority test
low: Low priority test
"""


def pytest_configure(config):
    for line in MARKER.split("\n"):
        if line.strip():
            config.addinivalue_line("markers", line)


@pytest.fixture(autouse=True)
def go_to_tmpdir(request):  # Injeção de dependência
    tmpdir = request.getfixturevalue("tmpdir")
    with tmpdir.as_cwd():
        yield  # Protocolo de generators
