
define snegov = Character('Снегов', color="#003ea2")

define aperturova = Character('Апертурова', color="#f201ff")

define student = Character('Я', color="#00baaa")

define audio.jazz = "music/jazz.mp3"

define audio.street = "music/part.wav"

label startChapter4:
<<<<<<< Updated upstream
=======
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА IV “ЭКОЛОГИЯ”"    
>>>>>>> Stashed changes

    play music street

    scene street with dissolve

<<<<<<< Updated upstream
    "Новый день, а впереди неизвестность."
    "Неизвестность заключается в новом предмете."
    "Вообще он называется “Нормирование качества и методы обращения с материалами информационных систем”"
    "Однако все зовут его Экологией."
    "Также разведданные говорят о том что у нас сразу два преподавателя на этом предмете."
    "Нечего думать. На паре всё станет ясно."
=======
    "{cps=45}{i}Новый день, а впереди неизвестность."
    "{cps=45}{i}Неизвестность заключается в новом предмете."
    "{cps=45}{i}Вообще он называется “Нормирование качества и методы обращения с материалами информационных систем”."
    "{cps=45}{i}Однако все зовут его Экологией."
    "{cps=45}{i}Также разведданные говорят о том что у нас сразу два преподавателя на этом предмете."
    "{cps=45}{i}Нечего думать. На паре всё станет ясно."
>>>>>>> Stashed changes


    scene ecolab2 with fade

    show aperturova:
        xpos 0.3
    with dissolve
    show snegov:
        xpos -0.3
    with dissolve

    play music jazz

<<<<<<< Updated upstream
    snegov "Я пожалуй начну."

    snegov "Моё имя Сергей Спиридонович Снегов. Профессор. Химик."
    snegov "Вы здесь для того, чтобы изучить науку синтезирования различных веществ. Очень точную и тонкую науку."
    snegov "Глупое глядение в монитор к этой науке не имеет никакого отношения, и потому многие из вас с трудом поверят, что мой предмет является важной составляющей учебного плана."
    snegov "Я постараюсь научить вас, как околдовать разум и обмануть чувства. Я расскажу вам, как разлить по бутылкам спирт, как заваривать эпоксидную смолу и даже как закупорить аргон."
    "Часть про спирт явно заинтересовала студентов."

    aperturova "Вы уже закончили, Сергей Спиридонович?"
    aperturova "Прошу простить моего коллегу. Он совсем не понимает сути данной дисциплины."
    aperturova "Забудьте всё, что он вам сказал. Я начну сначала. Так, как правильно."
    aperturova "Добро пожаловать в компьютеризированный экспериментальный центр при лаборатории исследования природы."
    aperturova "Меня зовут Ирина Георгиевна Апертурова. Как наиболее квалифицированный специалист в этом помещении, я рекомендую не прибегать к помощи всяких зельеваров."
    snegov "Всякие, как вы выразились, зельевары, умеют преподавать дисциплину, в отличие от прочих инвалидов умственного труда."
    aperturova "Я пожалуй пропущу мимо ушей вашу грубость и продолжу выполнять свою работу."
    aperturova "В этом научном комплексе мы будем проводить различные эксперименты."
    aperturova "Экспериментальный центр гарантирует абсолютную безопасность условий каждого испытания."
    aperturova "А в опасных условиях экспериментальный центр предоставляет помощь в виде полезных советов"
    aperturova "В целях соблюдения безопасности проведения утвержденных программой опытов просим вас не уничтожать оборудование первостепенной важности."



    aperturova "Первое испытание: Тест на определение жёсткости воды."
    aperturova "Всё необходимое оборудование лежит перед вами."

    snegov "Ой, а вы, я вижу, совсем для умственно отсталых рассказываете."
    snegov "Студенты итак прекрасно видят приборы и, уверен, понимают что это за устройства."
    snegov "Лучше сразу переходит к рецепту успеха сегодняшнего предприятия."
    snegov "Рецепт следующий: в коническую колбу пипеткой поместить 50 кубических сантиметров воды, с помощью пипетки добавить 5 миллилитров буферного раствора. Далее следует добавить индикатор эриохрома черного Т.. Жидкость должна окраситься в сиреневый цвет."
    snegov "Самая интересная часть - это титрование. Нужно взять вторую пипетку и начать постепенно добавлять раствор трилона Б, пока цвет жидкости не сменится на синий потеряв красные тона. Спешить не следует, раствор меняет цвет только через несколько секунд. У некоторых особо торопливых жидкость не синеет, а чернеет. Количество капель нужно подсчитать и выяснить объём затраченного раствора трилона Б. Двадцать капель - один миллилитр."
    snegov "В итоге взяв эту цифру можно выяснить жёсткость воды."
    aperturova "Перед началом тестирования хотим вам напомнить, что хотя основным принципом экспериментального центра является обучение в игровой форме, мы не гарантируем отсутствие увечий и травм."
    aperturova "Можете приступать."
=======
    snegov "{cps=45}Я пожалуй начну."

    snegov "{cps=45}Моё имя Сергей Спиридонович Снегов. Профессор. Химик."
    snegov "{cps=45}Вы здесь для того, чтобы изучить науку синтезирования различных веществ. Очень точную и тонкую науку."
    snegov "{cps=45}Глупое глядение в монитор к этой науке не имеет никакого отношения, и потому многие из вас с трудом поверят, что мой предмет является важной составляющей учебного плана."
    snegov "{cps=45}Я постараюсь научить вас, как околдовать разум и обмануть чувства. Я расскажу вам, как разлить по бутылкам спирт, как заваривать эпоксидную смолу и даже как закупорить аргон."
    "{cps=45}{i}Часть про спирт явно заинтересовала студентов."

    aperturova "{cps=45}Вы уже закончили, Сергей Спиридонович?"
    aperturova "{cps=45}Прошу простить моего коллегу. Он совсем не понимает сути данной дисциплины."
    aperturova "{cps=45}Забудьте всё, что он вам сказал. Я начну сначала. Так, как правильно."
    aperturova "{cps=45}Добро пожаловать в компьютеризированный экспериментальный центр при лаборатории исследования природы."
    aperturova "{cps=45}Меня зовут Ирина Георгиевна Апертурова. Как наиболее квалифицированный специалист в этом помещении, я рекомендую не прибегать к помощи всяких зельеваров."
    snegov "{cps=45}Всякие, как вы выразились, зельевары, умеют преподавать дисциплину, в отличие от прочих инвалидов умственного труда."
    aperturova "{cps=45}Я пожалуй пропущу мимо ушей вашу грубость и продолжу выполнять свою работу."
    aperturova "{cps=45}В этом научном комплексе мы будем проводить различные эксперименты."
    aperturova "{cps=45}Экспериментальный центр гарантирует абсолютную безопасность условий каждого испытания."
    aperturova "{cps=45}А в опасных условиях экспериментальный центр предоставляет помощь в виде полезных советов"
    aperturova "{cps=45}В целях соблюдения безопасности проведения утвержденных программой опытов просим вас не уничтожать оборудование первостепенной важности."



    aperturova "{cps=45}Первое испытание: Тест на определение жёсткости воды."
    aperturova "{cps=45}Всё необходимое оборудование лежит перед вами."

    snegov "{cps=45}Ой, а вы, я вижу, совсем для умственно отсталых рассказываете."
    snegov "{cps=45}Студенты итак прекрасно видят приборы и, уверен, понимают что это за устройства."
    snegov "{cps=45}Лучше сразу переходить к рецепту успеха сегодняшнего предприятия."
    snegov "{cps=45}Рецепт следующий: в коническую колбу пипеткой поместить 50 кубических сантиметров воды, с помощью пипетки добавить 5 миллилитров буферного раствора. Далее следует добавить индикатор эриохрома черного Т."
    snegov "{cps=45}Жидкость должна окраситься в сиреневый цвет."
    snegov "{cps=45}Самая интересная часть - это титрование. Нужно взять вторую пипетку и начать постепенно добавлять раствор трилона Б, пока цвет жидкости не сменится на синий потеряв красные тона."
    snegov "{cps=45}Спешить не следует, раствор меняет цвет только через несколько секунд. У некоторых особо торопливых жидкость не синеет, а чернеет."
    snegov "{cps=45}Количество капель нужно подсчитать и выяснить объём затраченного раствора трилона Б. Двадцать капель - один миллилитр."
    snegov "{cps=45}В итоге взяв эту цифру можно выяснить жёсткость воды."
    aperturova "{cps=45}Перед началом тестирования хотим вам напомнить, что хотя основным принципом экспериментального центра является обучение в игровой форме, мы не гарантируем отсутствие увечий и травм."
    aperturova "{cps=45}Можете приступать."
>>>>>>> Stashed changes

   

    
    
    call colbagame
    

    stop music fadeout 1.0
    return

label colbagame:
    hide aperturova
    hide snegov
<<<<<<< Updated upstream

    "В колбу налить 50 миллилитров воды"
            
    
    show colba_voda with dissolve

    "Добавить 5 мл буферного раствора"

    "Добавить индикатор эриохрома черного Т"
=======
    menu:
        "В колбу налить 50 миллилитров воды":
            show colba_voda with dissolve
               


    menu:
        "Добавить 5 мл буферного раствора":
            $trilon = 0
    menu:
        "Добавить индикатор эриохрома черного Т":
            $trilon = 0
>>>>>>> Stashed changes

    show colba_purple with dissolve
    hide colba_voda

    $trilon = 0
    $posinelo = False

    call addtrilon

    return



label addtrilon:

    menu:
<<<<<<< Updated upstream
        "Добавить 10 капель раствора трилона Б":
            $trilon += 10
        "Добавить 5 капель раствора трилона Б":
            $trilon += 5
=======
        "Добавить 5 капель раствора трилона Б":
            $trilon += 5
        "Добавить 10 капель раствора трилона Б":
            $trilon += 10
>>>>>>> Stashed changes
        "Добавить 20 капель раствора трилона Б":
            $trilon += 20

    if trilon < 40:
<<<<<<< Updated upstream
        "Цвет явно не синий. Надо продолжать."
=======
        "{i}Цвет явно не синий. Надо продолжать."
>>>>>>> Stashed changes
        jump addtrilon
    elif trilon >= 40 and trilon <= 50:
        if posinelo == False:
            show colba_blue-purple with dissolve
            hide colba_purple
            $posinelo = True
<<<<<<< Updated upstream
        "В колбе вещество сиреневого цвета, но уже чуть-чуть синеет"
=======
        "{cps=45}{i}В колбе вещество сиреневого цвета, но уже чуть-чуть синеет"
>>>>>>> Stashed changes
        jump addtrilon
    elif trilon > 55:
        show colba_black with dissolve
        hide colba_blue-purple
<<<<<<< Updated upstream
        "Вещество в колбе стало чёрным, как душа сценаристов последнего сезона \"Икры Престолов\"."
=======
        "{cps=45}{i}Вещество в колбе стало чёрным, как душа сценаристов последнего сезона \"Икры Престолов\"."
>>>>>>> Stashed changes
        show snegov with dissolve
        snegov "Знаете, Мозг - сложный и многослойный орган - по крайней мере, у большинства людей, но, видимо, не у вас. Переделывайте."
        jump colbagame



    show colba_blue with dissolve
    hide colba_blue-purple
            
<<<<<<< Updated upstream
    "Жижа посинела"
    "Итого, затрачено было [trilon] капель трилона Б"
    $jest = trilon * 0.05
    "Это значит, что жёсткость воды составляет [jest] градусов жёсткости."
    show aperturova with dissolve
    aperturova "Работа принята. Погрешность не превышена"
=======
    "{cps=45}{i}Жижа посинела"
    "{cps=45}{i}Итого, затрачено было [trilon] капель трилона Б"
    $jest = trilon * 0.05
    "{cps=45}{i}Это значит, что жёсткость воды составляет [jest] градусов жёсткости."
    show aperturova with dissolve
    aperturova "{cps=45}Работа принята. Погрешность не превышена"
>>>>>>> Stashed changes



    
    return
       
    


