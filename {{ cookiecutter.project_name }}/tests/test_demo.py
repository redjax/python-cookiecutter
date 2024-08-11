from __future__ import annotations

import logging
import os
import platform
import sys
import typing as t

## Add parent directory to path for importing Python project
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pytest import mark

from {{ cookiecutter.project_src }}.__test_demo import demo_test_print

log = logging.getLogger(__name__)


@mark.xfail
@mark.demo
def test_expect_fail() -> t.NoReturn:
    raise Exception("This failure is expected")


@mark.xfail
@mark.demo
@mark.platform
def test_fail_platform_system(detected_system: str) -> t.NoReturn:
    assert detected_system == "Force test failure", ValueError(
        "This failure is expected"
    )


@mark.demo
@mark.platform
def test_print_system(detected_system: str) -> t.NoReturn:
    log.info(f"Detected OS: {detected_system}")
    

@mark.demo
def test_demo_print():
    demo_test_print()