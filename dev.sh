#!/bin/sh

echo "Starting Tailwind CSS watcher 🎨"

tailwindcss -i ./assets/styles/input.css -o ./assets/styles/output.css --watch
