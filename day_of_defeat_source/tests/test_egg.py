#!/usr/bin/env python3
"""Structural contract tests for the Day of Defeat: Source egg."""

from __future__ import annotations

import json
import os
import re
import subprocess
import unittest
from pathlib import Path


EGG_DIR = Path(__file__).resolve().parents[1]
EGG_PATH = EGG_DIR / "egg-day-of-defeat--source.json"


def decode_json_object(value: str, field: str) -> dict:
    """Decode a Panel JSON-in-JSON field and require an object."""
    decoded = json.loads(value)
    if not isinstance(decoded, dict):
        raise ValueError(f"{field} must decode to an object")
    return decoded


class DecodeJsonObjectTests(unittest.TestCase):
    def test_decodes_panel_json_object(self) -> None:
        self.assertEqual(
            decode_json_object('{"done": "ready"}', "config.startup"),
            {"done": "ready"},
        )

    def test_rejects_non_object_panel_json(self) -> None:
        with self.assertRaisesRegex(ValueError, "config.files must decode to an object"):
            decode_json_object("[]", "config.files")

    def test_structural_test_script_is_executable(self) -> None:
        self.assertTrue(os.access(Path(__file__), os.X_OK))


class EggContractTests(unittest.TestCase):
    def test_has_ptdl_v2_identity(self) -> None:
        self.assertTrue(EGG_PATH.is_file(), f"missing egg export: {EGG_PATH}")
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))

        self.assertEqual(
            egg["_comment"],
            "DO NOT EDIT: FILE GENERATED AUTOMATICALLY BY PTERODACTYL PANEL - PTERODACTYL.IO",
        )
        self.assertEqual(egg["meta"], {"version": "PTDL_v2", "update_url": None})
        self.assertEqual(egg["name"], "Day of Defeat: Source")
        self.assertEqual(egg["author"], "support@pterodactyl.io")
        self.assertIn("Day of Defeat: Source", egg["description"])
        self.assertEqual(egg["features"], ["steam_disk_space"])
        self.assertIsInstance(egg["exported_at"], str)
        self.assertEqual(egg["file_denylist"], [])

    def test_uses_stock_source_image_and_direct_startup(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        expected_image = "ghcr.io/ptero-eggs/games:source"
        expected_startup = (
            "./srcds_run -game {{SRCDS_GAME}} -console -strictportbind "
            "-ip 0.0.0.0 -port {{SERVER_PORT}} +map {{SRCDS_MAP}} "
            "+servercfgfile server.cfg -maxplayers {{MAX_PLAYERS}} -nohltv -norestart"
        )

        self.assertEqual(egg.get("docker_images"), {expected_image: expected_image})
        self.assertEqual(egg.get("startup"), expected_startup)
        self.assertNotIn("{{STARTUP}}", egg.get("startup", ""))
        self.assertNotIn(".sh", egg.get("startup", ""))
        placeholders = set(re.findall(r"{{([A-Z0-9_]+)}}", egg.get("startup", "")))
        declared = {variable["env_variable"] for variable in egg.get("variables", [])}
        self.assertEqual(
            placeholders,
            {"SRCDS_GAME", "SERVER_PORT", "SRCDS_MAP", "MAX_PLAYERS"},
        )
        self.assertEqual(placeholders - {"SERVER_PORT"}, placeholders & declared)

    def test_decodes_panel_config_and_targets_dod_server_cfg(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        config = egg.get("config", {})

        self.assertEqual(set(config), {"files", "startup", "logs", "stop"})
        files = decode_json_object(config["files"], "config.files")
        startup = decode_json_object(config["startup"], "config.startup")
        logs = decode_json_object(config["logs"], "config.logs")
        self.assertEqual(
            files,
            {
                "dod/cfg/server.cfg": {
                    "parser": "file",
                    "find": {
                        "hostname": 'hostname "{{env.HOSTNAME}}"',
                        "sv_password": 'sv_password "{{env.SERVER_PASSWORD}}"',
                        "rcon_password": 'rcon_password "{{env.RCON_PASSWORD}}"',
                    },
                }
            },
        )
        self.assertEqual(startup, {"done": "Connection to Steam servers successful."})
        self.assertEqual(logs, {})
        self.assertEqual(config["stop"], "quit")

    def test_installer_is_anonymous_stock_and_fail_closed(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        installation = egg.get("scripts", {}).get("installation", {})

        self.assertEqual(
            installation.get("container"), "ghcr.io/ptero-eggs/installers:debian"
        )
        self.assertEqual(installation.get("entrypoint"), "bash")
        script = installation.get("script", "")
        syntax = subprocess.run(
            ["bash", "-n"],
            input=script.replace("\r\n", "\n"),
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(syntax.returncode, 0, syntax.stderr)
        self.assertIn("set -euo pipefail", script)
        self.assertIn("--retry 5 --retry-all-errors", script)
        self.assertIn(
            "tar --extract --gzip --file steamcmd.tar.gz --directory /mnt/server/steamcmd --no-same-owner",
            script,
        )
        self.assertIn(
            '+@sSteamCmdForcePlatformType linux +login anonymous +app_update "${SRCDS_APPID}" validate +quit',
            script,
        )
        self.assertIn("test -x /mnt/server/srcds_run", script)
        self.assertIn("test -x /mnt/server/srcds_linux", script)
        self.assertIn("test -f /mnt/server/dod/gameinfo.txt", script)
        self.assertIn("/mnt/server/dod/cfg/server.cfg", script)
        self.assertNotIn("apt ", script)

    def test_variables_have_safe_fixed_defaults_and_panel_rules(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        variables = {
            variable["env_variable"]: variable for variable in egg.get("variables", [])
        }
        expected = {
            "HOSTNAME": (
                "A Pterodactyl Hosted Day of Defeat: Source Server",
                r"required|string|max:64|not_regex:/[\x22\x5C\x0D\x0A]/",
                True,
                True,
            ),
            "SRCDS_MAP": (
                "dod_anzio",
                r"required|string|max:64|regex:/\A[A-Za-z0-9_-]+\z/",
                True,
                True,
            ),
            "MAX_PLAYERS": ("32", "required|integer|between:1,32", True, True),
            "SERVER_PASSWORD": (
                "",
                r"nullable|string|max:32|not_regex:/[\x22\x5C\x0D\x0A]/",
                True,
                True,
            ),
            "RCON_PASSWORD": (
                "",
                r"nullable|string|max:32|not_regex:/[\x22\x5C\x0D\x0A]/",
                True,
                True,
            ),
            "AUTO_UPDATE": ("1", "required|boolean", True, True),
            "SRCDS_APPID": ("232290", "required|string|in:232290", False, False),
            "SRCDS_GAME": ("dod", "required|string|in:dod", False, False),
        }

        self.assertEqual(set(variables), set(expected))
        self.assertNotIn("SERVER_PORT", variables)
        for env_name, (default, rules, viewable, editable) in expected.items():
            with self.subTest(env_name=env_name):
                variable = variables[env_name]
                self.assertEqual(variable["default_value"], default)
                self.assertEqual(variable["rules"], rules)
                self.assertEqual(variable["user_viewable"], viewable)
                self.assertEqual(variable["user_editable"], editable)
                self.assertEqual(variable["field_type"], "text")
                self.assertTrue(variable["name"].strip())
                self.assertTrue(variable["description"].strip())

    def test_quoted_server_cfg_values_reject_command_delimiters(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        variables = {
            variable["env_variable"]: variable for variable in egg.get("variables", [])
        }
        valid_values = {
            "HOSTNAME": (
                variables["HOSTNAME"]["default_value"],
                "Friendly DoD:S; Server",
            ),
            "SERVER_PASSWORD": (
                variables["SERVER_PASSWORD"]["default_value"],
                "ordinary;pass-123",
            ),
            "RCON_PASSWORD": (
                variables["RCON_PASSWORD"]["default_value"],
                "Rcon;pass_123",
            ),
        }
        unsafe_values = ('"', "\\", "\r", "\n", 'safe"; quit')

        for env_name, allowed in valid_values.items():
            with self.subTest(env_name=env_name):
                rule = next(
                    (
                        item
                        for item in variables[env_name]["rules"].split("|")
                        if item.startswith("not_regex:")
                    ),
                    None,
                )
                self.assertIsNotNone(
                    rule,
                    f"{env_name} must reject Source quoted-command delimiters",
                )
                assert rule is not None
                expression = rule.removeprefix("not_regex:")
                delimiter = expression[0]
                self.assertEqual(expression[-1], delimiter)
                pattern = expression[1:-1]
                for value in allowed:
                    self.assertIsNone(re.search(pattern, value), value)
                for value in unsafe_values:
                    self.assertIsNotNone(re.search(pattern, value), repr(value))

    def test_startup_map_rule_rejects_shell_metacharacters(self) -> None:
        egg = json.loads(EGG_PATH.read_text(encoding="utf-8"))
        variables = {
            variable["env_variable"]: variable for variable in egg.get("variables", [])
        }
        rules = variables["SRCDS_MAP"]["rules"]
        regex_rule = next(
            (rule for rule in rules.split("|") if rule.startswith("regex:")), None
        )

        self.assertIsNotNone(regex_rule, "SRCDS_MAP must have an allowlist regex")
        assert regex_rule is not None
        pattern = regex_rule.removeprefix("regex:")
        self.assertTrue(pattern.startswith(r"/\A") and pattern.endswith(r"\z/"))
        python_pattern = pattern.removeprefix(r"/\A").removesuffix(r"\z/")
        for valid_map in ("dod_anzio", "dod_avalanche", "custom-map_2"):
            with self.subTest(valid_map=valid_map):
                self.assertIsNotNone(re.fullmatch(python_pattern, valid_map))
        for unsafe_map in (
            "$(touch /home/container/pwned)",
            "dod_anzio;id",
            "dod_anzio && id",
            "dod_anzio foo",
            "dod_anzio\nid",
            "dod_anzio\n",
            "dod_anzio\r",
        ):
            with self.subTest(unsafe_map=unsafe_map):
                self.assertIsNone(re.fullmatch(python_pattern, unsafe_map))

    def test_readme_documents_install_config_and_single_allocation(self) -> None:
        readme_path = EGG_DIR / "README.md"
        self.assertTrue(readme_path.is_file(), f"missing egg README: {readme_path}")
        readme = readme_path.read_text(encoding="utf-8")
        root_readme = (EGG_DIR.parent / "README.md").read_text(encoding="utf-8")
        root_entry = "#### [Day of Defeat: Source](./day_of_defeat_source)"

        self.assertIn("Steam App ID `232290`", readme)
        self.assertIn("anonymous SteamCMD", readme)
        self.assertIn("`dod/cfg/server.cfg`", readme)
        self.assertIn("game traffic and A2S queries", readme)
        self.assertIn("one Pterodactyl allocation", readme)
        self.assertIn("SourceTV is disabled", readme)
        self.assertEqual(root_readme.count(root_entry), 1)
        self.assertLess(root_readme.index(root_entry), root_readme.index("#### [DayZ]"))


if __name__ == "__main__":
    unittest.main(verbosity=2)
