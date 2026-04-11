#!/usr/bin/env bash
set -euo pipefail

REPO_OWNER="${EPHEMERAL_REPO_OWNER:-desenyon}"
REPO_NAME="${EPHEMERAL_REPO_NAME:-ephemeral}"
REPO_URL="https://github.com/${REPO_OWNER}/${REPO_NAME}"
INSTALL_ROOT="${EPHEMERAL_HOME:-$HOME/.ephemeral}"
BIN_DIR="${EPHEMERAL_BIN_DIR:-$HOME/.local/bin}"
REF="${EPHEMERAL_REF:-main}"

if [[ "${REF}" == v* ]]; then
  ARCHIVE_REF="refs/tags/${REF}"
else
  ARCHIVE_REF="refs/heads/${REF}"
fi

ARCHIVE_URL="https://codeload.github.com/${REPO_OWNER}/${REPO_NAME}/tar.gz/${ARCHIVE_REF}"
TMP_DIR="$(mktemp -d)"
APP_DIR="${INSTALL_ROOT}/app"
VENV_DIR="${INSTALL_ROOT}/.venv"

cleanup() {
  rm -rf "${TMP_DIR}"
}

trap cleanup EXIT

require_command() {
  if ! command -v "$1" >/dev/null 2>&1; then
    echo "ephemeral installer: missing required command '$1'" >&2
    exit 1
  fi
}

require_command curl
require_command tar
require_command node
require_command npm

if command -v python3 >/dev/null 2>&1; then
  PYTHON_BIN="python3"
elif command -v python >/dev/null 2>&1; then
  PYTHON_BIN="python"
else
  echo "ephemeral installer: Python 3.11+ is required" >&2
  exit 1
fi

"${PYTHON_BIN}" - <<'PY'
import sys

if sys.version_info < (3, 11):
    raise SystemExit("ephemeral installer: Python 3.11+ is required")
PY

mkdir -p "${INSTALL_ROOT}" "${BIN_DIR}"

echo "Downloading Ephemeral from ${REPO_URL} (${REF})..."
curl -fsSL "${ARCHIVE_URL}" -o "${TMP_DIR}/ephemeral.tar.gz"
tar -xzf "${TMP_DIR}/ephemeral.tar.gz" -C "${TMP_DIR}"

EXTRACTED_DIR="$(find "${TMP_DIR}" -mindepth 1 -maxdepth 1 -type d -name "${REPO_NAME}-*" | head -n 1)"
if [[ -z "${EXTRACTED_DIR}" ]]; then
  echo "ephemeral installer: failed to unpack archive" >&2
  exit 1
fi

rm -rf "${APP_DIR}"
mv "${EXTRACTED_DIR}" "${APP_DIR}"

"${PYTHON_BIN}" -m venv "${VENV_DIR}"
"${VENV_DIR}/bin/python" -m pip install --upgrade pip setuptools wheel
"${VENV_DIR}/bin/pip" install -e "${APP_DIR}"
npm ci --prefix "${APP_DIR}/ephemeral/ink_ui"

ln -sf "${VENV_DIR}/bin/ephemeral" "${BIN_DIR}/ephemeral"
ln -sf "${VENV_DIR}/bin/ephemeral-setup" "${BIN_DIR}/ephemeral-setup"

echo
echo "Ephemeral is installed."
echo "Run: ${BIN_DIR}/ephemeral"
echo

case ":${PATH}:" in
  *":${BIN_DIR}:"*)
    ;;
  *)
    echo "Add ${BIN_DIR} to your PATH to launch it as \`ephemeral\`."
    ;;
esac

