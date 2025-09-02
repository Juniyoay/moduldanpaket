# Juniyo Abdiel Yassar / 243107030067

from game.sound import load, play, pause
from game.image import open, change, close
from game.level import start, load as load_level, over

load.s_load("mesin gerinda.mp3")
play.s_play("mesin gerinda.mp3")
pause.s_pause()

open.i_open("sapi.png")
change.i_change("sapi.png")
close.i_close("sapi.png")

start.l_start(1)
load_level.l_load(1)
over.l_over()