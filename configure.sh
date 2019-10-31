#! /usr/bin/env bash

# WRITING SAFE SHELL SCRIPTS
set -e
set -u
set -o pipefail
# set -o verbose

# shopt -s failglob
shopt -s nullglob
shopt -s extglob

READLINK="${READLINK:=readlink}"
PYTHON3="${PYTHON3:=python3}"

SCRIPT_PATH=$("${READLINK}" -f "$0")
SCRIPT_DIR=$(dirname "${SCRIPT_PATH}")

# If you use the eclipse launch configuration for 'configure.sh (macOS)' it will set these environment variables when you have all projects in eclipse
export HIVE_PROJECT_LOC="${HIVE_PROJECT_LOC:?is not set\!}"
export DOWNLOADS_DIR="${DOWNLOADS_DIR:?is not set\!}"

"${PYTHON3}" "${SCRIPT_DIR}"/configure.py