#!/bin/sh
# Script to install the theme components.

cd "/tmp/" || echo "Error: impossible to access to /tmp/ (wtf)." || exit 1
mkdir "dotstar-theme-components"
cd "dotstar-theme-components" || echo "Error: impossible to access to /tmp/dotstar-theme-components after creating it (wtf)." || exit 1

# Sweet components
wget
# colorsheme
wget
wget "$LINK" || echo "Error: impossible to download the ressource linked ($LINK)." || exit 1
tar -xf "$ARCHIVE_NAME" || echo "Error: impossible to extract the archive ($ARCHIVE_NAME)." || exit 1
rm "$ARCHIVE_NAME" || echo "Error: impossible to delete the now useless archive ($ARCHIVE_NAME)."
