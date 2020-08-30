"""
Title: Use and pin Black 20
Date: 2020-08-30
"""
import argparse
from pathlib import Path
from subprocess import run

from all_repos import autofix_lib
from all_repos.grep import repos_matching


def find_repos(config):
    return repos_matching(config, ("black", "--", "requirements.txt"))


def run_command(command: list):
    result = run(command)
    result.check_returncode()


def apply_fix():
    requirements_txt = Path("requirements.txt")

    lines = requirements_txt.read_text().splitlines()
    for index, line in enumerate(lines):
        if line.startswith("black"):
            lines[index] = "black==20.8b1"

    requirements_txt.write_text("\n".join(lines) + "\n")

    run_command(["scripts/install"])
    run_command(["scripts/lint"])


def main(argv=None):
    parser = argparse.ArgumentParser()
    autofix_lib.add_fixer_args(parser)
    args = parser.parse_args(argv)

    repos, config, commit, autofix_settings = autofix_lib.from_cli(
        args,
        find_repos=find_repos,
        msg="Use and pin Black 20",
        branch_name="black20",
    )

    autofix_lib.fix(
        repos,
        apply_fix=apply_fix,
        config=config,
        commit=commit,
        autofix_settings=autofix_settings,
    )


if __name__ == "__main__":
    exit(main())
