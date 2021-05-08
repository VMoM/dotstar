from applications.package_manager import PackageManager

# Package managers that the application can use.
SUPPORTED_PMS = {
    "pacman": PackageManager("pacman", "pacman", "sudo pacman -Sy %s", True),
    "snap sandbox": PackageManager("snap sandbox", "snap", "sudo snap install %s", True),
    "snap classic": PackageManager("snap classic", "snap", "sudo snap install %s --classic", False)
}
