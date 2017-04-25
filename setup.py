import cx_Freeze

executables = {cx_Freeze.Executable("flappycompleted.py")}

cx_Freeze.setup(
    name = "Flying Birds",
    options ={"build_exe":{"packages":["pygame"],"include_files":["main.jpg","bird1.png","bird2.png","bird3.png","wallpaper1.jpg","wallpaper2.jpg","wallpaper3.jpg"]}},
    description = "It is a game like Flappy birds",
    executables = executables
    )
