#!/usr/bin/env bash

set -ex
coverage run --source='.' -m pytest "$@"
coverage report