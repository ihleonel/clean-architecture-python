# AGENTS.md

## Project Description

Project implementing **Clean Architecture** principles in Python. The code is organized into well-defined layers (domain, application, infrastructure) to achieve separation of concerns, maintainability, and testability.

## Project Structure

```
src/
  commons/          # Shared code (e.g., ValidationError)
  customers/        # Customers module
  routes/           # Routes module
  zones/            # Zones module
tests/
  customers/        # Customer tests
  routes/           # Route tests
  zones/            # Zone tests
```

Each module follows this structure:
- **domain/**: Entities, validations, and repositories (abstract interfaces).
- **application/**: Use cases (creators, updaters).
- **infrastructure/**: Concrete repository implementations.

## Running Tests

The project uses `unittest` (Python standard library, no external dependencies).

### Run all tests

```bash
python3 -m unittest discover -s tests
```

### Run tests for a specific module

```bash
# Customer tests only
python3 -m unittest discover -s tests/customers

# Zone tests only
python3 -m unittest discover -s tests/zones

# Route tests only
python3 -m unittest discover -s tests/routes
```

### Run a specific test file

```bash
python3 -m unittest discover -s tests -p "test_create_customer.py"
```

### Run a specific test case

```bash
python3 -m unittest tests.customers.test_create_customer.TestCreateCustomer.test_should_create_customer
```

## Conventions

- Test files are named with the `test_` prefix.
- Test classes inherit from `unittest.TestCase`.
- Repository mocks are created using `unittest.mock.Mock` in each test's `setUp`.
- The `fakers/` modules inside `tests/` contain fake repository implementations for testing.
- Domain validations raise `ValidationError` (from `src.commons.domain.validation_error`) with an error dictionary.
