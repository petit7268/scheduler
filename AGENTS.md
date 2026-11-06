# AI Agent Guidelines for OSM Project



## Python Version
- Target Python 3.14+ (project uses Python 3.14)
- Use modern Python features available in 3.14+

## Code Style Guidelines

### Type Annotations
- Use modern Python type annotations with built-in types
- Use `list` instead of `List` from typing module
- Use `dict` instead of `Dict` from typing module
- Use `tuple` instead of `Tuple` from typing module
- Use `X | None` instead of `Optional[X]` for nullable types
- Use function parameter and return type annotations
- Add `from __future__ import annotations` at the top of files when using modern type annotations
- Use `typing.Protocol` for structural subtyping when needed

```python
# Good
def process_data(items: list[dict]) -> dict[str, str]:
    return {"result": "processed"}

# Bad
from typing import List, Dict
def process_data(items: List[Dict]) -> Dict[str, str]:
    return {"result": "processed"}
```

### Import Organization
Organize imports in this order:
1. Standard library imports
2. Third-party imports
3. Local imports (from this project)

Separate each group with a blank line.
Sort imports alphabetically within each import group to satisfy Ruff I001 lint rule.
Use absolute imports for project modules: `from src.classes.point import Point`

```python
# Good
import json
import os
import re
from collections import defaultdict

from curl_cffi import requests
from gpxpy.gpx import GPX, GPXWaypoint

from src.function.reverse_geo import get_country_from_gpx_point
```

### Code Formatting
- Follow PEP 8 standards
- Maximum line length: 88 characters (black default)
- Use `black` formatter if configured in pyproject.toml

### Docstrings
- Use triple double quotes `"""` for docstrings
- Use docstrings for all functions
- Include Args and Returns sections for functions with parameters
- Include Raises sections when applicable
- Keep descriptions concise but informative


### Dataclasses
- Use `@dataclass` decorator for simple data containers
- Use `@dataclass(frozen=True)` for immutable data
- Prefer dataclasses over regular classes for data storage
- Use dataclasses for configuration instead of global variables

### Error Handling
- Use specific exception types
- Include helpful error messages
- Use context managers (`with` statements) for resource management
- Do not catch blind `Exception` - use specific exceptions like `requests.RequestException`, `ValueError`, etc.

### File Paths
- Use `pathlib.Path` instead of `os.path` for file path operations
- Path is more readable and object-oriented
- Example: `Path("folder") / "file.txt"` instead of `os.path.join("folder", "file.txt")`
- Use `Path.exists()`, `Path.is_file()`, `Path.is_dir()` for path checks
- Use `Path.mkdir(parents=True, exist_ok=True)` for directory creation

### AI-Specific Guidelines
- When modifying existing code, match the existing style
- Prefer minimal, focused edits
- Add comments only when the logic is complex or non-obvious
- Use meaningful variable and function names
- Avoid magic numbers; use named constants instead


### Git Conventions
- Write clear, descriptive commit messages
- Use imperative mood in commit messages (e.g., "Add feature" not "Added feature")
- Keep commits focused on a single change
- Always `git pull` before starting work on different computers

## Common Patterns

### Configuration Management
- Use dataclasses for configuration instead of global variables
- Group related configuration values in dataclass fields
- Create default configuration instances for convenience
- Pass configuration objects to functions rather than relying on global state
- This improves testability and makes dependencies explicit

```python
# Good
@dataclass
class CaravanConfig:
    graphql_url: str = "https://app.caravanya.com/graphql/"
    output_dir: str = "files/caravanya_data"
    headers: dict = field(default_factory=lambda: {...})



### Error Handling
- Use specific exception handling where possible
- Include error logging for debugging
- Return None or empty results for non-critical failures
- Use context managers for resource management

### File Operations
- Use `pathlib.Path` for cross-platform path handling
- Create directories with `Path.mkdir(parents=True, exist_ok=True)`
- Use UTF-8 encoding for file operations

### Progress Tracking
- Print progress updates for long-running operations
- Use percentage-based progress for batch operations
- Include timestamp information in output files


