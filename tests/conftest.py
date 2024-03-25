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
