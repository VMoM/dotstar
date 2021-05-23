#!/bin/sh
# Script to install the theme components.

# GLOBAL VARIABLES
USER_SHARE_PATH="$HOME/.local/share/"
readonly USER_SHARE_PATH

# CREATING /tmp/dotstar-theme-components/
cd "/tmp/" || echo "Error: impossible to access to /tmp/ (wtf). Exiting." || exit 1
MAIN_FOLDER_NAME="dotstar-theme-components"
readonly MAIN_FOLDER_NAME
# if dotstar-theme-components already exists, we delete it
if [ -d "$MAIN_FOLDER_NAME" ]; then
  rm -rf "$MAIN_FOLDER_NAME"
fi
mkdir "$MAIN_FOLDER_NAME"
cd "$MAIN_FOLDER_NAME" || echo "Error: impossible to access to /tmp/$MAIN_FOLDER_NAME after creating it (wtf). Exiting." || exit 1


# SWEET COMPONENTS
# getting Sweet from GitHub
SWEET_ARCHIVE_NAME="Sweet-nova.tar.gz"
SWEET_FOLDER_NAME="Sweet-nova"
readonly SWEET_ARCHIVE_NAME
readonly SWEET_FOLDER_NAME
wget https://github.com/EliverLara/Sweet/archive/nova.tar.gz --output-document="$SWEET_ARCHIVE_NAME" || echo "Error: impossible to get the Sweet theme archive from GitHub. Exiting." || exit 1
# decompressing Sweet
tar -xf "$SWEET_ARCHIVE_NAME" || echo "Error: impossible to extract the Sweet theme archive. Exiting." || exit 1
# removing the archive
rm $SWEET_ARCHIVE_NAME
cd "$SWEET_FOLDER_NAME/kde" || echo "Error: impossible to enter on $SWEET_FOLDER_NAME/kde/. Exiting." || exit 1
# installing aurorae
cp -r "aurorae/Sweet-Dark/" "$USER_SHARE_PATH/aurorae/themes/"
# installing colorsheme
cp "colorschemes/Sweet.colors" "$USER_SHARE_PATH/color-schemes/"
# installing cursors
cp -r "cursors/Sweet-cursors" "$USER_SHARE_PATH/icons/"
# installing sddm
# TODO find where put it


# Layan components
cd "/tmp/$MAIN_FOLDER_NAME/" || echo "Error: impossible to return to /tmp/$MAIN_FOLDER_NAME/. Exiting." || exit 1
# getting Layan from GitHub
LAYAN_ARCHIVE_NAME="Layan-master.tar.gz"
LAYAN_FOLDER_NAME="Layan-kde-master"
readonly LAYAN_ARCHIVE_NAME
readonly LAYAN_FOLDER_NAME
wget https://github.com/vinceliuice/Layan-kde/archive/master.tar.gz --output-document="$LAYAN_ARCHIVE_NAME" || echo "Error: impossible to get the Layan theme archive from GitHub. Exiting." || exit 1
# decompressing Layan
tar -xf "$LAYAN_ARCHIVE_NAME" || echo "Error: impossible to extract the Layan theme archive. Exiting." || exit 1
# removing the archive
rm $LAYAN_ARCHIVE_NAME
cd "$LAYAN_FOLDER_NAME" || echo "Error: impossible to enter on $LAYAN_FOLDER_NAME/. Exiting." || exit 1
# plasma
cp -r "plasma/desktoptheme/Layan/" "$USER_SHARE_PATH/plasma/desktoptheme/"
cp -r "plasma/desktoptheme/icons/" "$USER_SHARE_PATH/plasma/desktoptheme/Layan/"
# wallpaper
cp -r "wallpaper/Layan/" "$USER_SHARE_PATH/wallpapers/"


# Papirus (icons)
cd "/tmp/$MAIN_FOLDER_NAME/" || echo "Error: impossible to return to /tmp/$MAIN_FOLDER_NAME/. Exiting." || exit 1
# getting Papirus from GitHub
PAPIRUS_ARCHIVE_NAME="Papirus-master.tar.gz"
PAPIRUS_FOLDER_NAME="papirus-icon-theme-master"
readonly PAPIRUS_ARCHIVE_NAME
readonly PAPIRUS_FOLDER_NAME
wget https://github.com/PapirusDevelopmentTeam/papirus-icon-theme/archive/master.tar.gz --output-document="$PAPIRUS_ARCHIVE_NAME" || echo "Error: impossible to get the Layan theme archive from GitHub. Exiting." || exit 1
# decompressing Papirus
tar -xf "$PAPIRUS_ARCHIVE_NAME" || echo "Error: impossible to extract the Layan theme archive. Exiting." || exit 1
# removing the archive
rm "$PAPIRUS_ARCHIVE_NAME"
cd "$PAPIRUS_FOLDER_NAME" || echo "Error: impossible to enter on $LAYAN_FOLDER_NAME/. Exiting." || exit 1
# installing icons
cp -r "Papirus/" "$USER_SHARE_PATH/icons/"

exit 0
