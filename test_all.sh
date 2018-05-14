#! /usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
ORIG="$(pwd)"
set -uo pipefail

cd "$DIR"
python -m unittest
cd "$ORIG"

# to run a subset
# python -m test.test_inclusion.Inclusion
# python -m test.test_inclusion.Inclusion.test_b

