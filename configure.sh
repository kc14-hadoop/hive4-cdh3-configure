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

"${PYTHON3}" "${SCRIPT_DIR}"/configure.py