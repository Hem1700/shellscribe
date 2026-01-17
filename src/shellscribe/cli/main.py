from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="shellscribe")
    sub = parser.add_subparsers(dest="command")

    project = sub.add_parser("project")
    project_sub = project.add_subparsers(dest="subcommand")
    project_sub.add_parser("init")

    config = sub.add_parser("config")
    config_sub = config.add_subparsers(dest="subcommand")
    config_sub.add_parser("set")
    config_sub.add_parser("get")

    policy = sub.add_parser("policy")
    policy_sub = policy.add_subparsers(dest="subcommand")
    policy_sub.add_parser("allowlist")

    run = sub.add_parser("run")
    run.add_argument("scenario")

    sub.add_parser("replay")

    report = sub.add_parser("report")
    report.add_argument("run_id")

    plugins = sub.add_parser("plugins")
    plugins.add_argument("action", choices=["list", "enable", "disable"])

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        return 0

    print(f"shellscribe: command '{args.command}' not implemented yet")
    return 0
