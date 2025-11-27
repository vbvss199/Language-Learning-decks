"""
Vocabulary Schema Tests
Validates all language JSON files against the vocabulary_schema.json specification.
Run with: python -m pytest -v
"""

import json
from pathlib import Path

import pytest
from jsonschema import Draft7Validator, validate


# Setup paths
TESTS_DIR = Path(__file__).parent
REPO_ROOT = TESTS_DIR.parent
SCHEMA_PATH = TESTS_DIR / "vocabulary_schema.json"


def _vocab_id(path: Path) -> str:
    """Return a stable test id for a vocabulary file."""
    return path.relative_to(REPO_ROOT).as_posix()


VOCAB_FILES = sorted(
    f for f in REPO_ROOT.rglob("*.json") if "tests" not in f.parts
)


@pytest.fixture(scope="module")
def schema():
    """Load and validate the JSON schema."""
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        schema_data = json.load(f)
    
    # Ensure the schema itself is valid
    Draft7Validator.check_schema(schema_data)
    return schema_data


@pytest.fixture(scope="module")
def vocabulary_files():
    """Return all vocabulary JSON files in the repository."""
    return VOCAB_FILES


def test_schema_exists():
    """Test that the schema file exists."""
    assert SCHEMA_PATH.exists(), f"Schema file not found at {SCHEMA_PATH}"


def test_schema_is_valid_json():
    """Test that the schema file contains valid JSON."""
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        json.load(f)  # Should not raise JSONDecodeError


def test_schema_is_valid_json_schema(schema):
    """Test that the schema is a valid JSON Schema."""
    # This is implicitly tested by the schema fixture
    assert schema is not None
    assert "$schema" in schema


def test_vocabulary_files_found(vocabulary_files):
    """Test that we found vocabulary files to validate."""
    assert len(vocabulary_files) > 0, "No vocabulary files found in repository"


@pytest.mark.parametrize("vocab_file", VOCAB_FILES, ids=_vocab_id)
def test_vocabulary_file_valid_json(vocab_file):
    """Test that each vocabulary file contains valid JSON syntax."""
    with open(vocab_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    assert isinstance(data, list), f"{vocab_file.name} should contain a JSON array"
    assert len(data) > 0, f"{vocab_file.name} should not be empty"


@pytest.mark.parametrize("vocab_file", VOCAB_FILES, ids=_vocab_id)
def test_vocabulary_file_schema_compliance(vocab_file, schema):
    """Test that each vocabulary file complies with the schema."""
    with open(vocab_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Validate against schema
    validate(instance=data, schema=schema)