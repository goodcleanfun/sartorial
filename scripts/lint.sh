#!/usr/bin/env bash

set -e
set -x

#ruff sartorial tests
black sartorial tests --check
