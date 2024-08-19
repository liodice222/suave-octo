#!/bin/bash

case "$1" in
    add)
        username="$2"
        sudo useradd "$username"
        ;;
    modify)
        username="$2"
        shell="$3"
        sudo usermod -s "$shell" "$username"
        ;;
    delete)
        username="$2"
        sudo userdel "$username"
        ;;
    *)
        echo "Usage: $0 {add|modify|delete} username [shell]"
        exit 1
        ;;
esac