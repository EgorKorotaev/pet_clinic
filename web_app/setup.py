#!/usr/bin/env python

from distutils.core import setup

setup(
    name="pet clinic",
    version="0",
    description="",
    author="",
    packages=["pet_clinic"],
    package_dir={"": "src"},
    entry_points={"console_scripts": ["pet_clinic=pet_clinic.app:uvicorn_start"]},
)
