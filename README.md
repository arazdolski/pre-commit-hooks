# pre-commit-hooks

## Configure pre-commit hooks

Add this to your `.pre-commit-config.yaml`

```
  - repo: https://github.com/arazdolski/pre-commit-hooks
    rev: v1.0.0
    hooks:
      - id: valid-branch-name
        args:
          ["--regex", '[A-Z]+-[0-9]+-.*']
```
