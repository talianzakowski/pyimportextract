import pytest

@pytest.fixture
def a_single_import_line():
    return "import mylibrary"


@pytest.fixture
def a_single_from_line():
    return "from mylibrary import foo"


@pytest.fixture
def a_multiple_from_import():
    return "from mylibrary import foo, bar, baz"


@pytest.fixture
def a_multiple_from_import_with_as_line():
    return "from mylibrary import foo as off, bar as rab, baz as zab"


@pytest.fixture
def an_import_with_as():
    return "import speech_recognition as src"

    
