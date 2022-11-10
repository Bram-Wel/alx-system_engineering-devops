#!/usr/bin/env bash
# Run a command as a different user

if [ "$1" ]
then
    sudo -u "$1" 'whoami'
fi
