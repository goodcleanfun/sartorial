#!/usr/bin/env bash

set -e
set -x

#ruff dorsal tests
black dorsal tests --check
