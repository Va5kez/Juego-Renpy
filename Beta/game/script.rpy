# Imagenes de personajes importados desde de http://tokudaya.net/
# Musica https://www.youtube.com/channel/UC_aEa8K-EOJ3D6gOs7HcyNg
# Se usa la variable image para definir cada una de las imagenes que se van a usar en el juego como los personajes y el background.
# Para poner un background, despues de la variable image, hay que poner bg y despues el nombre con el que vamos a llamar al background cada ves que lo necesitamos
image bg pasillo = "pasillo.jpg"
image bg bedroom = "bedroom.jpg"
image bg escuela = "escuela.jpg"
image bg aula = "aula.jpg"
image bg black = "black.jpg"
image bg back = "back.jpg"
image bg locker1 = "locker1.jpg"

image Leah crying = "Leah_crying.png"
image Leah mad = "Leah_mad.png"
image Leah normal = "Leah_normal.png"
image Leah sad = "Leah_sad.png"
image Leah shy = "Leah_shy.png"
image Leah smiling = "Leah_smiling.png"
image Leah surprised = "Leah_suprised.png"
image Leah worried = "Leah_worried.png"

image Jack normal = "Jack_normal.png"
image Jack serious = "Jack_serious.png"
image Jack shy = "Jack_shy.png"
image Jack smiling1 = "Jack_smiling1.png"
image Jack smiling2 = "Jack_smiling2.png"
image Jack surprised = "Jack_surprised.png"
image Jack thnking = "Jack_thinking.png"
image Jack worried = "Jack_worried.png"

image Julie crying = "Julie_crying.pmg"
image Julie mad = "Julie_mad.png"
image Julie normal = "Julie_normal.png"
image Julie shy = "Julie_shy.png"
image Julie smiling = "Julie_smiling.png"
image Julie surprised = "Julie_surprised.png"
image Julie undifferent = "Julie_undifferent.png"
image Julie worried = "Julie_worried.png"

image Rias Sensei happy = "RiasSensei_happy.png"
image Rias Sensei mad = "RiasSensei_mad.png"
image Rias Sensei normal = "RiasSensei_normal.png"
image Rias Sensei sad = "RiasSensei_sad.png"
image Rias Sensei smiling = "RiasSensei_smiling.png"
image Rias Sensei surprised = "RiasSensei_surprised.png"
image Rias Sensei thinking = "RiasSensei_thinking.png"
image Rias Sensei dissapointed = "RiasSensei_dissapointed.png"

image Roman mad = "Roman_mad.png"
image Roman normal = "Roman_normal.png"
image Roman serious = "Roman_serious.png"
image Roman smiling = "Roman_smiling.png"
image Roman surprised = "Roman_surprised.png"
image Roman worried = "Roman_worried.png"

image Emily mad = "Emily_mad.png"
image Emily normal = "Emily_normal.png"
image Emily shy = "Emily_shy.png"
image Emily smiling = "Emily_smiling.png"
image Emily surprised = "Emily_surprised.png"
image Emily worried = "Emily_worried.png"

# Declare characters used by this game.
define j = Character('Jack', color="#c8ffc8")
define r = Character('Rias Sensei', color="#c8ffc8")
define m = Character('Me', color="#c8c8ff")
define e = Character('Emily', color="#c8ffc8")
define ju = Character('Julie', color="#c8ffc8")
define l = Character('Leah', color="#c8ffc8")
define ro = Character('Roman Sensei', color="#c8ffc8")

# El juego comienza a partir de este punto
label start:
    $ bl_game = False
    
    play music "Dropouts.ogg"
    
    scene bg bedroom
    with fade
    
    "Oh god!, I will be late in the first day of class..."
    "Aff, is that hard for a new transferred student to be on time?..."
    "At the end that doesn't matter....."
    "I must hurry up, or I will be late for the first class..."
    
    scene bg escuela
    with fade
    
    m "I can't beleive it!" 
    m "Luckly, I manage to arrive on time..."
    
    show Rias Sensei mad
    with dissolve
    
    r "You are almost late young boy..."
    m "Sorry Sensei, I fall asleep..."
    m "I'm still not used to the time zone in here..."
    
    show Rias Sensei thinking
    r "You need to wake up earlier, or else you would get in trouble for coming late to school."
    m "Yeah, I know."
    m "It won't happen again...."
    
    show Rias Sensei happy
    r "I'm glad to here that..."
    r "Well, now go to your classroom..." 
    r "The classes are about to start..."
    m "Yes, Sensei..."
    
    hide Rias Sensei normal
    with dissolve
    " After that, I hurried up to get into my classroom..."
    
    scene bg aula
    with fade
    
    show Jack smiling1
    with dissolve
    
    j "Hi! You are the new transferred student right?"
    j "I´ll be your classmate from now on."
    
    show Jack smiling2
    j "By the way, my name is Jack, nice to meet you..."
    
    menu:
        
        "Nice to meet you too!":
            
            jump nice
        
        "Sorry, i'm not interested in been your friend":
            jump sorry
    
label nice:

    show Jack smiling1
    with dissolve
    m "Nice to meet you too!"
    m "My name is Mark..."
    m "Hope to get along with you from now on..."
    j "Of course..."
    hide Jack smiling1
    with dissolve
    
    show Emily normal
    e "Good moring Jack, here's your lunch..."
    hide Emily normal
    with dissolve
    
    show Jack smiling2
    j "Thanks babe, your lunchs are always tasty."
    
    show Jack normal
    j "By the way Emily, this is my new friend Mark..."
    j "He is a transferred student from U.S."
    hide Jack normal
    with dissolve
    
    show Emily smiling
    with dissolve
    e "Nice to meet you Mark. I'm Jack's girlfriend..."
    
    show Emily normal
    m "Nice to meet you too Emily..."
    hide Emily normal
    with dissolve
    
    show Julie mad
    with dissolve
    ju "Come on guys, sit down already please. Roman Sensei is coming to the classroom"
    hide Julie mad
    
    show Jack normal
    with dissolve
    j "Ok Julie, just calm down. It's not big deal."
    hide Jack normal
    
    show Julie mad
    with dissolve
    ju "Like always Jack, just giving troubles."
    ju "Can you be responsible for just once..."
    ju "At least in this new school year?..."
    hide Julie mad
    with dissolve
    
    show Emily mad
    with dissolve
    e "Come on Julie, you don't have to be like that with us..."
    hide Emily mad
    
    show Julie undifferent
    with dissolve
    ju "Ok, sorry guys. But you know the rules."
    ju "Roman sensei is just at the door, I better hurry and sit down."
    hide Julie undifferent
    with dissolve
    
    show Jack smiling1
    with dissolve
    j "She's always like that... Never changes..."
    m "Who's her?..."
    show Jack normal
    with dissolve
    j "Her name is Julie..."
    j "She is the Student council president..."
    j "Thats why she always acts so strict, you know, following the rules..."
    
    scene bg back
    with fade
    
    show Roman normal
    with dissolve
    ro "Good morning students..."
    "Good morning Sensei..."
    ro"Well students, class has started, so everyone get your history books..."
    hide Roman normal
    with dissolve
    "And so the day passed like any other..."
    
    show bg pasillo
    with fade
    m " Now that the school day is over, I can go home to relax a little bit..."
    " But suddenly Jack and Emily appears..."
    
    show Jack smiling1 at left
    with dissolve
    show Emily normal at right
    with dissolve
    j "Hey Mark, do you have free time right now?"
    e " We are going to the shopping mall..."
    e "We wonder if you want to come with us...?"
    
    menu:
        
        "Yeah, of course, just let me grab my stuff from the classroom...":
            
            jump yeah
            
        "Sorry I can't today. I have some stuff to do...":
        
            jump no
            
label yeah:
    
    m "Yeah, of course, just let me grab my stuff from the classroom..."
    j "We will be waiting for you at the entrance..."
    m "Ok, I will be there in a second..."
    hide Jack smiling 1
    with dissolve
    hide Emily normal
    with dissolve
    
    show bg locker1
    with fade
    
    m "I kept them waiting a lot..."
    m "I better run or they will go without me"
    
    "Suddenly a girl crossed in front of me while I was running... and we collide."
    m "Are you alright?"
    show Leah worried
    with dissolve
    l "Yeah I'm Ok... I guess..."
    m "Please forgive me, I didn't pay attention while I was running..."
    show Leah normal
    l "Don't worry, I'm fine..."
    m "Ok"
    m "By the way, my name is Mark, nice to meet you."
    l "I'm Leah, nice to meet you Mark..."
    l "I'm in the 1-B class..."
    m "I'm from class 2-A..."
    m "Well I have to go now, see you tomorrow then Leah..."
    l "Ok Mark, see you tomorrow too..."
    hide Leah normal
    
    scene bg bedroom
    with fade
    m "Oh, this was a very long and exhausting day..."
    m "It was really fun to hang out today with Jack and Emily "
    m "Besides, I meet this pretty girl Leah"
    m "Today was an awesome day..."
    m "I can't imaging how tomorrow will be..."
   
    scene bg black
    with fade
    "   You had a nice and normal highschool student life after that day"
    "   You made a lot of new friends..."
    "   Had some great and unique experience with your friends..."
    "   Good Ending...."
    
    return
    
label no:
    
    m " Sorry I cant today. I have some stuff to do.."
    j " Ok, dont worry Mark"
    j "It will be for next time..."
    e " See you tomorrow then Mark, bye..."
    m " Bye guys, see you tomorrow then."
    
    hide Jack smiling 1
    with dissolve
    hide Emily normal
    with dissolve
    
    m "Now I will head back home..."
    
    scene bg bedroom
    with fade
    m "Oh, this was a very long and exhausting day..."
    m "I can't imaging how tomorrow will be..."
    
    scene bg black
    with fade
    "   You had a nice and normal highschool student life after that day"
    "   You made a lot of new friends..."
    "   Had some great and unique experience with your friends..."
    "   Good Ending...."
    return
    
label sorry:
    
    m "Sorry, i'm not interested in been your friend."
    
    show Jack surprised
    with fade
    j "Well..... I was trying to be friendly, you know..."
    m "I didn't ask you to do that for me."
       
    show Jack serious
    j "Ok, whatever man..."
    j "I don't have a problem with that."
    
    hide Jack serious
    with dissolve
    
    "Jack walks away...."
    show bg black
    with fade
    
    "Everyone on the classroom saw your arrogant attitude towards Jack."
    "Because of that you couldn't make any friends in your classroom."
    
    "Bad Ending..."
    
    return
