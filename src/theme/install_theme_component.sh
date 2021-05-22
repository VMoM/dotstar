#!/bin/sh
# Script to install a theme component.
# Downloads the link, put the uncompressed archive (.tar.xz) on the colorsheme directory and delete the archive.
LINK=$1
ARCHIVE_NAME=$2
PATH_TO_THEME_COMPONENT=$3
readonly LINK
readonly ARCHIVE_NAME
readonly PATH_TO_THEME_COMPONENT

cd "$PATH_TO_THEME_COMPONENT" || exit
wget "$LINK"
tar -xf "$ARCHIVE_NAME"
rm "$ARCHIVE_NAME"
