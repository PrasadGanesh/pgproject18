#! /usr/bin/env bash

find . -type f -name "*bucket*" | xargs -I {} rm {}
