import os
import uuid
import pytest
from dundie.core import load
from .constants import PEOPLE_FILE


def setup_module():  # Hooks
    print()
    print("roda antes dos testes desse modulo\n")


def teardown_module():  # Hooks
    print()
    print("roda depois dos testes desse modulo\n")


@pytest.fixture(scope="function", autouse=True)
def create_new_file(tmpdir):
    file_ = tmpdir.join("new_file.txt")
    file_.write("isso é sujeira...")
    yield
    file_.remove()


@pytest.mark.unit
@pytest.mark.high
def test_load(request):
    """Test function load function."""

    request.addfinalizer(lambda: print("✅"))

    filepath = f"arquivo_indesejado-{uuid.uuid4()}.txt"
    request.addfinalizer(
        lambda: os.unlink(filepath) if os.path.exists(filepath) else None
    )

    with open(filepath, "w") as f:
        f.write("Arquivo indesejado")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "J"


@pytest.mark.unit
@pytest.mark.high
def test_load2():
    """Test function load function."""
    with open(f"arquivo_indesejado-{uuid.uuid4()}.txt", "w") as f:
        f.write("Arquivo indesejado")

    assert len(load(PEOPLE_FILE)) == 2
    assert load(PEOPLE_FILE)[0][0] == "J"
