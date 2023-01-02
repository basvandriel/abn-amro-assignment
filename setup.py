#!/usr/bin/env python

from pathlib import Path

from extreqs import parse_requirement_files
from setuptools import setup

here_path = Path(__file__).resolve().parent


requirements: tuple[list[str], dict[str, list[str]]] = parse_requirement_files(
    here_path / "requirements.txt",
    optional=here_path / "requirements-dev.txt",
)
install_requires, extras_require = requirements

setup(install_requires=install_requires, extras_require={"dev": extras_require})
