import pytest
from main import *


def test_import_line(a_single_import_line):
    extracted = extract_import(a_single_import_line)
    assert extracted == "mylibrary"


def test_from_line(a_single_from_line):
    extracted = extract_from(a_single_from_line)
    assert extracted == "mylibrary"


def test_from_with_multiple_imports(a_multiple_from_import):
    extracted = extract_from(a_multiple_from_import)
    assert extracted == "mylibrary"


def test_from_with_multiple_imports_and_as(a_multiple_from_import_with_as_line):
    extracted = extract_from(a_multiple_from_import_with_as_line)
    assert extracted == "mylibrary"

def test_import_with_as(an_import_with_as):
    extracted = extract_import(an_import_with_as)
    assert extracted == "speech_recognition"



