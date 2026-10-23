#!/usr/bin/env bash
# Automated workspace instantiation script for kryptic-agent core environment
set -e

echo "🤖 Instantiating cybernetic engine architecture..."
mkdir -p modules archived_memories

touch modules/__init__.py
echo "✅ Operational workspace initialized successfully."

chmod +x setup.sh
./setup.sh

python3 main_workspace.py
