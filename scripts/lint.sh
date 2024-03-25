#!/usr/bin/env bash

set -e
set -x

#ruff provisional tests
black provisional tests --check
