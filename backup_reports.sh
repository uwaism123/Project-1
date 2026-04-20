#!/bin/bash

echo "📦 Backing up logs..."

mkdir -p backup
cp -r logs/* backup/

echo "✅ Backup complete → backup/"