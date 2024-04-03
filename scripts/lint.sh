#!/usr/bin/env bash

set -e
set -x

ruff check sartorial tests --fix
black sartorial tests --check
