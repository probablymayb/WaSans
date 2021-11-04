# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ch_Sans = Character("샌즈", color = "#2effee")
define ch_Minyoung = Character("민영", color = "#81fc92")

define narrator = Character(None, kind = nvl) 

image bg_WASans = "bg/maxresdefault.jpg"
image scg_Sans: 
    im.FactorScale("Character/sans/Colored_Undertale_Sans_sprite.png", 0.75)
    yalign 0.7

define center = Position(xalign = 0.5, yalign = 0.7)
define left = Position(xalign = 0, yalign = 0.7)
define right = Position(xalign = 1, yalign = 0.7)


label start:
    scene bg_WASans
    show scg_Sans

    "싸늘한 기운이 당신을 감싼다."
    "당신은 죄악이 등을 타고 오르는 것을 느꼈다"

    show scg_Sans at left
    
    ch_Sans "안녕. 꽤 바빴었지, 응?
                ... 그래, 물어볼 게 하나 있어.
                가장 나쁜 사람이라 할지라도 바뀔 수 있을까...?
                노력만 한다면, 모두가 착한 사람이 될 수 있을까?"
   
    show scg_Sans at center
   
    ch_Sans "헤 헤 헤 헤...
            좋아.
            그럼, 여기 더 괜찮은 질문이 있어.
            끔찍한 시간을 보내고 싶어?"
    
    nvl clear
   
    show scg_Sans at right

    "독"
    "백"
    "두번째"

    ch_Minyoung "오마카세 먹으러 가고싶다."



    
    return
