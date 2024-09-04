name = "dcpomatic"

version = "2.16.91"

authors = [
    "Carl Hetherington",
    "Terrence Meiczinger",
    "Mart Jansink",
    "Ole Laursen",
    "Benjamin Radel",
    "Leo Depoix (@piloegao)",
]

description = """
    Convert video, audio and subtitles into DCP: the standard format required by cinemas across the world.
    """

requires = ["python"]

uuid = "carlh.dcpomatic"

build_command = ""


def commands():
    import os
    install_root = "" # This is installed on windows using an installer.

    match system.platform:
        case "windows":
            install_root = r"C:\\PROGRA~1\\DCP-o-matic 2"
            env.PATH.append(os.path.join(install_root, "bin"))

            # The aliases are not working because of an issue with the space in the path.
            # alias("dcpomatic2", os.path.join(install_root, "bin", "dcpomatic2.exe"))
            # alias("dcpomatic2_batch", os.path.join(install_root, "bin", "dcpomatic2_batch.exe"))
            # alias("dcpomatic2_cli", os.path.join(install_root, "bin", "dcpomatic2_cli.exe"))
            # alias("dcpomatic2_combiner", os.path.join(install_root, "bin", "dcpomatic2_combiner.exe"))
            # alias("dcpomatic2_create", os.path.join(install_root, "bin", "dcpomatic2_create.exe"))
            # alias("dcpomatic2_disk", os.path.join(install_root, "bin", "dcpomatic2_disk.exe"))
            # alias("dcpomatic2_disk_writer", os.path.join(install_root, "bin", "dcpomatic2_disk_writer.exe"))
            # alias("dcpomatic2_editor", os.path.join(install_root, "bin", "dcpomatic2_editor.exe"))
            # alias("dcpomatic2_kdm", os.path.join(install_root, "bin", "dcpomatic2_kdm.exe"))
            # alias("dcpomatic2_kdm_cli", os.path.join(install_root, "bin", "dcpomatic2_kdm_cli.exe"))
            # alias("dcpomatic2_player", os.path.join(install_root, "bin", "dcpomatic2_player.exe"))
            # alias("dcpomatic2_playlist", os.path.join(install_root, "bin", "dcpomatic2_playlist.exe"))
            # alias("dcpomatic2_server", os.path.join(install_root, "bin", "dcpomatic2_server.exe"))
            # alias("dcpomatic2_verify", os.path.join(install_root, "bin", "dcpomatic2_verify.exe"))
        case _:
            pass
