#!/usr/bin/env bash

set -e
set -x

#ruff corral tests
black corral tests --check
