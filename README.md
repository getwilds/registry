WILDS Registry
==============

Registry of WILDS repositories.

The registry is in: [registry.json](registry.json)

How it works locally for testing purposes:

```
pip install -r requirements.txt
python code.py
```

How it works on GitHub Actions via the `.github/workflows/build.yml` file:

- Install Python
- Install python libraries
- Run `python code.py`
- Commit changed `registry.json` file to the default branch (`gh-pages`). This updated file is then available at <https://getwilds.org/registry/registry.json>
