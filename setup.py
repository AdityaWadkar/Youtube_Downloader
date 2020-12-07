import cx_Freeze
executables = [cx_Freeze.Executable("Youtube_downloader.py")]

cx_Freeze.setup(
    name="snake",
    options={"build_exe": {"packages":["pytube","tkinter","threading","time"],
                           "include_files":["icon.png","youtube.ico","youtube.png"]}},
    executables = executables

    )