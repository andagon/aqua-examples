# aqua Agent - Linux Python Selenium Example

## Setup

### Agent

The aqua agent should be running on a x86 Linux. Using an ARM OS might require special steps (Like changing the autoinstall of geckodriver to download an ARM build)

Install python3, python3 venv, pip and poetry (optional, use pipx to install poetry).

This poetry project is configured to create the virtual environment in the project folder to avoid side effects should something on the machine change. The temp folder is cleared by the agent after running the executions automatically.
Reinstalling the environment on each run might be overhead for short running executions.

### Aqua

Create a testcase and add the content of aqua-scripts/01-setup as unix shell script as first step.
This script pulls this repository onto the agent machine and runs poetry install.

Create a second test step with aqua-scripts/02-run. This is the runner that executes the python scripts.

## Development

The project comes with a devcontainer configuration for use in visual studio code.