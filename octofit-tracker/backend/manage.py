#!/usr/bin/env python
"""Wrapper manage.py so VS Code launch config that expects manage.py in backend/ works.
This forwards to octofit_tracker/manage.py.
"""
import os
import runpy

HERE = os.path.dirname(__file__)
TARGET = os.path.join(HERE, "octofit_tracker", "manage.py")
runpy.run_path(TARGET, run_name="__main__")
