# Tests Directory

This directory contains schema validation tests for the Language Learning Decks repository.

**Note:** The schema currently accepts all values present in existing JSON files to maintain backward compatibility. This includes some edge cases and suspected inaccuracies, particularly in the `pos` (part of speech) field, which may contain non-standard values like 'aia' or 'violette'.

## Files

### `vocabulary_schema.json`
The formal JSON Schema specification that defines the structure and validation rules for all vocabulary files in this repository.

### `test_vocabulary_schema.py`
Comprehensive pytest test suite that validates all vocabulary JSON files. Tests include:
- JSON syntax validation
- Schema compliance checking against the shared JSON Schema

### `requirements.txt`
Python package dependencies required to run the validation tests.

## Usage

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Tests
```bash
# Run with detailed traceback 
python -m pytest -v --tb=short
```
