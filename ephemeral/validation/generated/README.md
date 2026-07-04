# Generated validation payloads

`payloads.py` contains **450 synthetic Pydantic models** (`GenPayload0000` … `GenPayload0449`) used only for validation stress coverage.

## Purpose

- Exercise Pydantic round-trip serialization across many model shapes without hand-writing hundreds of fixtures.
- Keep `tests/test_validation_generated.py` fast by sampling every third index (not all 450 classes per run).

## Ownership

| Artifact | Role |
|----------|------|
| `payloads.py` | Generated module — do not edit classes by hand |
| `tests/test_validation_generated.py` | Round-trip regression tests |
| `ephemeral/validation/schemas.py` | Real product request/response models |

## Regeneration

There is no checked-in generator script today. To add models, extend `payloads.py` with the same field template (`tag`, `payload`, `score`, `notes`, `items`) and add a sampled test in `test_validation_generated.py`.

## Not used at runtime

These classes are **not** imported by the CLI, Ink bridge, or tools in normal operation. Safe to ignore when navigating the product graph.
