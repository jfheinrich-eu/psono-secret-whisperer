#!/bin/bash

set -e

checkSecret1="${1}"
checkSecret2="${2}"
checkValue1="ghcr.io"
checkValue2="jfheinrich"
result1="success"
result2="success"

echo "## Output Check Results" >> $GITHUB_STEP_SUMMARY

if [ "$checkSecret1" != "$checkValue1" ]; then
    echo "- ❌ secret1 mismatch: got '$checkSecret1'" >> $GITHUB_STEP_SUMMARY
    result1="fail"
else
    echo "- ✅ secret1 is correct" >> $GITHUB_STEP_SUMMARY
fi

if [ "$checkSecret2" != "$checkValue2" ]; then
    echo "- ❌ secret2 mismatch: got '$checkSecret2'" >> $GITHUB_STEP_SUMMARY
    result2="fail"
else
    echo "- ✅ secret2 is correct" >> $GITHUB_STEP_SUMMARY
fi

# Combine results
if [ "$result1" = "fail" ] || [ "$result2" = "fail" ]; then
    echo "status=fail" >> "$GITHUB_OUTPUT"
else
    echo "status=success" >> "$GITHUB_OUTPUT"
fi
