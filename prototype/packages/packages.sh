#!/bin/bash


if command -v python3 &>/dev/null; then
	echo Py3 Installed! #run next checking scripts
else
	echo Please install Py3 before proceeding
fi

if command -v conda &>/dev/null; then
	echo Conda is installed
else
	echo Conda is not installed
fi
