
define ch_Sans = Character("샌즈", color = "#2effee")
define ch_Papyrus = Character("파피루스", color = "#ff9830")
define ch_Minyoung = Character("민영", color = "#81fc92")
define ch_narrator = Character(None)

define narrator = Character(None, kind = nvl) 

image bg_WASans = "bg/maxresdefault.jpg"
image scg_Sans: 
    im.FactorScale("Character/sans/Colored_Undertale_Sans_sprite.png", 0.75)
    yalign 0.7

image scg_Sans shrug:
    im.FactorScale("Character/sans/sans_shrug.png",0.75)
    
image scg_Papyrus:
    im.FactorScale("Character/papyrus/Papyrus.png", 0.75)
    yalign 0.7

define center = Position(xalign = 0.5)
define left = Position(xalign = 0.2)
define right = Position(xalign = 0.8)


label start:
    
    $love_point = 0

    scene bg_WASans with fade
    show scg_Sans

    "싸늘한 기운이 당신을 감싼다."
    "당신은 죄악이 등을 타고 오르는 것을 느꼈다"

    show scg_Sans at left

    ch_Sans "안녕. 꽤 바빴었지, 응?"
    ch_Sans "... 그래, 물어볼 게 하나 있어.
            가장 나쁜 사람이라 할지라도 바뀔 수 있을까...?
            노력만 한다면, 모두가 착한 사람이 될 수 있을까?"
   
    show scg_Sans shrug at center
   
    ch_Sans "헤 헤 헤 헤...
            좋아.
            그럼, 여기 더 괜찮은 질문이 있어.
            끔찍한 시간을 보내고 싶어?"
    
    nvl clear

    show scg_Sans at left with dissolve
    show scg_Papyrus at right with dissolve

    "독"
    "백"
    "두번째"
    
    nvl clear
    
    ch_narrator "뭐 먹을까?"

    menu:
        "한우오마카세":
            ch_Sans "ㄹㅇㅋㅋ"
            $love_point = love_point + 1
        "은행꼬치구이":
            "샌즈, 파피루스"  "어우 그건좀"
            $love_point = love_point - 1
  
    if(love_point > 0):
        jump good_ending
    else:
        jump bad_ending

    ch_Minyoung "오마카세 먹으러 가고싶다."
    ch_Sans "ㄹㅇㅋㅋ"
    ch_Papyrus "ㄹㅇㅋㅋ"

    hide scg_Sans
    hide scg_Papyrus
    with dissolve
    
label good_ending:
     return

label bad_ending:
    
     return
    
    return
