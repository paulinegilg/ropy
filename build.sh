#!/bin/sh

echo "Beep-beep... Starting build... 🤖"

echo "Cleaning previous build 🧹"

if [ -d "./build" ]; then
  rm -r ./build
fi

echo "Creating new build 🪄"

mkdir ./build

echo "Minifying CSS 🐤"

tailwindcss -i ./assets/styles/output.css -o ./build/style.css --minify

echo "Parse contents ⚗️"

python3 main.py

echo "Build is complete! 🎉"
