WILDS Registry
==============

Registry of WILDS repositories.

The registry is in: [registry.json](registry.json)

How it works locally for testing purposes:

```
# create a virtualenv and source it
python -m venv .venv
source .venv/bin/activate

# generate registry
pip install -r requirements.txt
python code.py

# deactivate virtualenv
deactivate
```

How it works on GitHub Actions via the `.github/workflows/build.yml` file:

- Install Python
- Install python libraries
- Run `python code.py`
- Commit changed `registry.json` file to the default branch (`gh-pages`). This updated file is then available at <https://getwilds.org/registry/registry.json>
- Note that the automatic pages-build-deployment action that triggers on a gh-pages branch was turned off in this repo and instead build and deployment is based on the `build.yml` file alone. Go to Settings > Pages > Build and Deployment in the repo to see where this is set
