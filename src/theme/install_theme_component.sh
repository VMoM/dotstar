#!/bin/sh
# Script to install a theme component.
# Downloads the link, put the uncompressed archive (.tar.xz) on the colorsheme directory and delete the archive.
LINK=$1
ARCHIVE_NAME=$2
PATH_TO_THEME_COMPONENT=$3
readonly LINK
readonly ARCHIVE_NAME
readonly PATH_TO_THEME_COMPONENT

cd "$PATH_TO_THEME_COMPONENT" || echo "Error: invalid path to the theme component ($PATH_TO_THEME_COMPONENT)." || exit 1
wget "$LINK" || echo "Error: impossible to download the ressource linked ($LINK)." || exit 1
tar -xf "$ARCHIVE_NAME" || echo "Error: impossible to extract the archive ($ARCHIVE_NAME)." || exit 1
rm "$ARCHIVE_NAME" || echo "Error: impossible to delete the now useless archive ($ARCHIVE_NAME)."
