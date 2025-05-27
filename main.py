 microbit import *
import music

# https://musescore.com/user/75698476/scores/22381297
# https://flat.io/score/67dbd9803f0364b3d235b97b-?srsltid=AfmBOopPySt174MR6BRLOZ5UQ2GpTr-oRghtAmjw3x82Opjx5_UvUVss

music.reset
music.set_tempo(bpm=1*(1+4)*5*1*4)
set_volume(114514+1919+810)

# c:ド
# d:レ
# e:ミ
# f:ファ
# g:ソ
# a:ラ
# b:シ

# 数字が大きいほど音が短くなる…のか？(1が8分音符、2が16分音符、4が32分音符?)
# 音名のあとにbでフラット、#でシャープ、数字で音階(4がデフォルト)

inmu1=[
    "e:1","f:1","f#:1",
    "g:2","bb:2","bb:2","bb:2","gb:2","bb:2","bb:1","g:1",
    "g:1","bb:1","f:2","eb:2","d:2","c#:2","d:4","e:1","f:1","f#:1",
    "g:2","g:2","bb:2","f#:2","g:2","bb:2","c5:2",
    "d5:8","d:2","f:2","bb:2","e:1","f:1","f#:1",
    "g:2","bb:2","bb:2","bb:2","g:2","bb:2","bb:1","g:1",
    "g:1","bb:1","f:2","eb:2","d:2","c#:2","d:4","e:1","f:1",
    "g:2","g:2","bb:4","d5:2","bb4:2","c5:2","d5:2",
    "bb4:4",
]

inmu2=[
]

inmu=inmu1+inmu2
#inmu=inmu2

while True:
    if button_a.is_pressed():
        display.scroll("YAJU&U")
    if button_b.is_pressed():
        display.scroll("114514")
    if pin_logo.is_touched():
        music.play(inmu)
