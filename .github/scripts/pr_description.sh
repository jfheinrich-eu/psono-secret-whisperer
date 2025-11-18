#!/bin/bash

set -e

ref="${1}"
sha="${2}"

# Get all commits in the PR
commits=$(git log --pretty=format:"%H|%s" origin/${ref}..${sha})

if [[ -z "$commits" ]]; then
    echo "No commits found between origin/${ref} and ${sha}."
    exit 0
fi

# Initialize categories
features=""
fixes=""
docs=""
chore=""
deps=""
other=""

# Process each commit
while IFS='|' read -r hash message; do
    if [[ $message =~ ^feat(\(.+\))?: ]]; then
        features="$features- $message\n"
    elif [[ $message =~ ^fix(\(.+\))?: ]]; then
        fixes="$fixes- $message\n"
    elif [[ $message =~ ^docs(\(.+\))?: ]]; then
        docs="$docs- $message\n"
    elif [[ $message =~ ^chore(\(.+\))?: ]]; then
        chore="$chore- $message\n"
    elif [[ $message =~ ^(build|deps)(\(.+\))?: ]]; then
        deps="$deps- $message\n"
    else
        other="$other- $message\n"
    fi
done <<< "$commits"

# Build changelog
changelog=""

if [[ -n "$features" ]]; then
    changelog="$changelog## 🚀 Features\n$features\n"
fi

if [[ -n "$fixes" ]]; then
    changelog="$changelog## 🐛 Bug Fixes\n$fixes\n"
fi

if [[ -n "$docs" ]]; then
    changelog="$changelog## 📚 Documentation\n$docs\n"
fi

if [[ -n "$deps" ]]; then
    changelog="$changelog## ⬆️ Dependencies\n$deps\n"
fi

if [[ -n "$chore" ]]; then
    changelog="$changelog## 🧹 Chore\n$chore\n"
fi

if [[ -n "$other" ]]; then
    changelog="$changelog## 🔧 Other Changes\n$other\n"
fi

# Set output with proper escaping
{
    echo "changelog<<EOF"
    echo -e "$changelog"
    echo "EOF"
} >> $GITHUB_OUTPUT
