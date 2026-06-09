# Gitingest — Repo Understanding Tool

## Install
```bash
pip install gitingest
```

## Usage
```bash
gitingest https://github.com/owner/repo -o digest.txt
# Or replace 'hub' with 'ingest':
# https://gitingest.com/owner/repo
```

## Python API (batch mode)
```python
from gitingest import ingest
tree, content, stats = ingest(
    "https://github.com/owner/repo",
    max_file_size=30_000,
    exclude_patterns=["*.lock","*.sum","node_modules/*","dist/*","*.min.*"]
)
print(f"Files: {stats['files_analyzed']}")
```

## Token-Efficient Pattern
Don't load full digest. Extract:
- File tree (shows structure at a glance)
- CLAUDE.md / AGENTS.md / README.md (behavior docs)
- Skip: source code files, lock files, generated assets

## Source Repos Already Digested
All 14 source repos were gitingested before building ll-vibekit.
See DISCOVERIES.md for what was found in each.

## Evaluating a New Repo
1. gitingest the repo
2. Read: file tree + key markdown files
3. Answer: what unique patterns does it have?
4. Answer: does it overlap with existing skills/agents?
5. Extract only unique, non-overlapping patterns
6. Add to skills/ with source attribution
