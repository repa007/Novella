
define arsentiev = Character('Арсентьев', color="#ba0000")

label startChapter1:

    scene street
    with fade

    "{font=Gilroy-ExtraBold.otf}ГЛАВА I “ВВЕДЕНИЕ В СПЕЦИАЛЬНОСТЬ”"
    "{cps=25}Сентябрь. Знойное дыхание лета ещё не покинуло столицу"
    "{cps=25}Утреннее солнце предвещает новые приключения"
    "{cps=25}Что ждёт студента в его первый учебный день?"
    "{cps=25}Корпус на улице Прянишникова (с некоторых пор здесь поселился факультет ИТ)"
    "{cps=25}В народе это место известно как “Пряники”"
    "{cps=25}Место спокойное и тихое. Находится около большого пруда, парка и садов Тимирязевской академии"
    
    scene university
    with fade
    
    "{font=Gilroy-ExtraBold.otf}КАФЕДРА ИНФОРМАТИКИ"
    
    show arsentiev
    with dissolve
    
    arsentiev "{cps=25}Я смотрю к нам прибыло пополнение"
    arsentiev "{cps=25}Зовут меня Дмитрий Андреевич Арсентьев"
    arsentiev "{cps=25}Я тут на кафедре информатики и ИТ вроде как главный"
    
    hide arsentiev
    with dissolve
    
    "*перешёптывания в аудитории"
    "{cps=25}Тот самый Арсентьев!" 
    "{cps=25}Говорят, что он общается только сложными метафорами, шутками и оборванными фразами"
    "{cps=25}Старшекурсники рассказывают, что у него есть уникальная способность появляться в нужный момент и предлагать сделать проект, за который можно получить зачёт"
    "{cps=25}Ходят даже слухи что Арсентьев одолел кровожадность не менее легендарного Норникеля, что по половине группы валил"
    
    show arsentiev
    with dissolve
    
    arsentiev "{cps=25}Сегодня у нас будет первая пара по предмету “Введение в специальность”"
    arsentiev "{cps=25}Вообще предмет будет проводится в дистанционном формате, так что напрягать вас с точки зрения передвижения не буду"
    arsentiev "{cps=25}Итак… приступим! А то я уже устал так напрягать речевой аппарат"
    
    "{cps=25}Морально-волевые волевые возможности по поддержанию напряжённого монолога явно покинули Арсентьева, и он продолжил занятие в свойственном ему стиле"
    
    arsentiev "{cps=25}Гениальный"
    arsentiev "{cps=25}Алан"
    arsentiev "{cps=25}Человек"
    arsentiev "{cps=25}Прометей принёс нам огонь, а он эти ваши компухтеры запилил"
    arsentiev "{cps=25}Немцам расшифровал"
    arsentiev "{cps=25}Энигму"
    arsentiev "{cps=25}Хорошая сегодня погодка"
    arsentiev "{cps=25}Так о чём это я?"
    arsentiev "{cps=25}Ах да..."
    arsentiev "{cps=25}Не посрамите имя великого учёного своими нелепыми каракулями в коде!"
    arsentiev "{cps=25}Поговорим о профилях"
    arsentiev "{cps=25}Что у нас есть?"
    arsentiev "{cps=25}Первый профиль"
    arsentiev "{cps=25}Автоматизированные системы…"
    arsentiev "{cps=25}…обработки информации и управления"
    arsentiev "{cps=25}Ух ты!"
    arsentiev "{cps=25}Запомнил"
    arsentiev "{cps=25}Короче..."
    arsentiev "{cps=25}Профиль для тех кто хочет программировать"
    arsentiev "{cps=25}Что там дальше?"
    arsentiev "{cps=25}Информационные технологии в медиаиндустрии и дизайне"
    arsentiev "{cps=25}Ага... "
    arsentiev "{cps=25}Туда у нас обычно все девочки сбегают"
    arsentiev "{cps=25}И те, кто рисовать умеет"
    arsentiev "{cps=25}Технологии дополненной и виртуальной реальности"
    arsentiev "{cps=25}Вот это лютая тема!"
    arsentiev "{cps=25}Современно"
    arsentiev "{cps=25}Модно"
    arsentiev "{cps=25}Молодёжно"
    arsentiev "{cps=25}Дальше по списку наш флагман"
    arsentiev "{cps=25}Программное обеспечение игровой компьютерной индустрии"
    arsentiev "{cps=25}Готовим оккупантов стимов да плеймаркетов"
    arsentiev "{cps=25}Ну и последний профиль…"
    arsentiev "{cps=25}Информационные системы умных пространств"
    arsentiev "{cps=25}Там мы настоящих волшебников учим"
    arsentiev "{cps=25}Кричишь “да будет свет” и лампочка загорается"
    arsentiev "{cps=25}Ладно"
    arsentiev "{cps=25}Об этом вам ешё более подробно расскажут"
    arsentiev "{cps=25}Тест на внимательность!"
    
    menu:
        "{cps=25}Кто я?"
        "Дмитрий Алексеевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE
        "Дмитрий Андреевич":
            call ARSENTIEV_TRUE from _call_ARSENTIEV_TRUE
        "Андрей Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_1
        "Арсентий Дмитриевич":
            call ARSENTIEV_FALSE from _call_ARSENTIEV_FALSE_2

    menu:
        arsentiev "{cps=25}Тьюринга хоть помните?"
        "Это гениальный человек": 
            call CONTINUE_STORY from _call_CONTINUE_STORY
        "Да, это из-за него у нас есть компьютеры": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_1
        "Шифр немецкий расшифровал": 
            call CONTINUE_STORY from _call_CONTINUE_STORY_2

    
    return

label ARSENTIEV_TRUE:
    arsentiev "{cps=25}Соколы!"
    return
    
label ARSENTIEV_FALSE:
    arsentiev "{cps=25}Беда..."
    arsentiev "{cps=25}Вы меня явно невнимательно слушали!"
    arsentiev "{cps=25}Дмитрий Андреевич я"
    return
    
label CONTINUE_STORY:
    arsentiev "{cps=25}Вы чертовски правы!"
    arsentiev "{cps=25}Ну ладно, гуляйте"
    return

