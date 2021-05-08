class PackageManager:
    """
    An object that contains the name used by dotstar and the true name of the PM (the one used by the OS, that dotstar
    calls when installing).
    dotstar don't uses the same name as the OS because snap has two mods of installation (sandbox and classic)
    so we have to differentiate them.
    Contains too the command shape, a string with a %s placeholder
    """
    def __init__(
            self,
            dotstar_name: str,
            system_name: str,
            command_shape: str
    ) -> None:
        """
        :param dotstar_name: the name of the PM that dotstar uses
        :param system_name: the name of the PM that the OS uses
        :param command_shape: the shape of the command. Must have a %s placeholder
        """
        self.dotstar_name = dotstar_name
        self.system_name = system_name
        self.command_shape = command_shape
