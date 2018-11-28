#! /env/var/sh

find . -type f -name "*bucket*" | xargs -I {} rm {}
