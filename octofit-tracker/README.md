OctoFit Tracker — backend

This folder contains the backend for the OctoFit Tracker project.

Quick start

1. Create and activate the virtual environment (already created in this repo):

```bash
source /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/activate
```

2. Run Django development server (from the repository root or anywhere):

```bash
python /workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/python -m django runserver 0.0.0.0:8000
# or without activating venv:
/workspaces/skills-build-applications-w-copilot-agent-mode/octofit-tracker/backend/venv/bin/python -m django runserver 0.0.0.0:8000
```

Notes
- The virtual environment is located at `octofit-tracker/backend/venv`.
- The Django project was scaffolded into `octofit-tracker/backend/octofit_tracker`.
