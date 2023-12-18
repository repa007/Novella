
define student = Character('Неизвестный студент', color="#00baaa")
<<<<<<< Updated upstream

define ohrannik = Character('Охранник', color="#003bba")


define prepod = Character('Физрук', color="#00ff1a")
define DM = Character('Dungeon Master', color="#00ff1a")

label startChapter5:
    scene university
    with fade
    "На сегодня всё. Можно и домой."
    "Хотя есть нюанс…"
    "Физкультура сама на себя ходить не будет."
    "Затягивать с посещением данной дисциплины больше нельзя."
    "Говорилось, что спортзал где-то неподалёку."

    scene street
    with fade
    show fizra_map
    "Спортзал в километре отсюда… А до начала пары 5 минут."
    "Проблема…"
    "А кто это накачанный и в фирменной футболке политеха несётся в обозначенном картами направлении?"

    show vitalik
    with dissolve

    "Это же местная знаменитость! Виталик “скандинавская ходьба”."
    "Вероятно он тоже торопится на занятие."
=======
define ohrannik = Character('Охранник', color="#003bba")
define prepod = Character('Физрук', color="#00ff1a")
define DM = Character('Dungeon Master', color="#00ff1a")

define audio.street = "music/part.wav"
define audio.run = "music/run.wav"
define audio.metal = "music/metal.wav"

label startChapter5:
    scene black
    with fade
    "{font=Gilroy-ExtraBold.otf}ГЛАВА V ”ФИЗИЧЕСКАЯ КУЛЬТУРА”"

    scene university
    with fade
    play music street
    "{cps=45}{i}На сегодня всё. Можно и домой."
    "{cps=45}{i}Хотя есть нюанс…"
    "{cps=45}{i}Физкультура сама на себя ходить не будет."
    "{cps=45}{i}Затягивать с посещением данной дисциплины больше нельзя."
    "{cps=45}{i}Говорилось, что спортзал где-то неподалёку."

    scene street
    with fade
    show fizra_map
    "{cps=45}{i}Спортзал в километре отсюда… А до начала пары 5 минут."
    "{cps=45}{i}Проблема…"
    stop music fadeout 1.0
    play music run
    "{cps=45}{i}А кто это накачанный и в фирменной футболке политеха несётся в обозначенном картами направлении?"

    show vitalik
    with dissolve

    "{cps=45}{i}Это же местная знаменитость! Виталик “скандинавская ходьба”."
    "{cps=45}{i}Вероятно он тоже торопится на занятие."
>>>>>>> Stashed changes

    menu:
        "Побежать за Виталиком":
            call runWithVitalik from _call_runWithVitalik
        "Осмотреться":
            show back_fizra_scuters
            with fade
<<<<<<< Updated upstream
            "Возле крыльца стоит великое множество электросамокатов. Решение найдено!"
            scene fizra
            with fade
            "Данное средство индивидуальной мобильности разрушает представление о скорости."
            "Впрочем главное не разрушиться об столб или автомобиль."
            "Резкие манёвры с запредельными перегрузками, достойными опытного лётчика-истребителя, позволили избежать коллизии."
            "Электросамокат настолько быстр, что почти удалось догнать Виталика, хотя тот к концу дистанции всё ещё сохранял отрыв."

    "Благодаря нечеловеческим усилиям порог преодолён вовремя. Но впереди возникает следующее препятствие."

    scene back_fizra_guard with fade
    show guard with dissolve

    "Грозный лик охранника преграждает дорогу."
    ohrannik "Документик покажите."
    menu:
        "Да, сейчас студенческий достану.":
            ohrannik "Ну проходи"
        "Усы и хвост - вот мои документы":
            ohrannik "Помнится и я любил бросать остроты, да потом из-за них мне прострелили колено."
            ohrannik "Ладно, скоморох, иди с миром."

    scene black with fade

    "Переодеться в раздевалке не заняло много времени."

    "Но куда дальше идти?"
    "Надо спросить у охранника."
=======
            "{cps=45}{i}Возле крыльца стоит великое множество электросамокатов. Решение найдено!"
            scene fizra
            with fade
            "{cps=45}{i}Данное средство индивидуальной мобильности разрушает представление о скорости."
            "{cps=45}{i}Впрочем главное не разрушиться об столб или автомобиль."
            "{cps=45}{i}Резкие манёвры с запредельными перегрузками, достойными опытного лётчика-истребителя, позволили избежать коллизии."
            "{cps=45}{i}Электросамокат настолько быстр, что почти удалось догнать Виталика, хотя тот к концу дистанции всё ещё сохранял отрыв."

    "{cps=45}{i}Благодаря нечеловеческим усилиям порог преодолён вовремя. Но впереди возникает следующее препятствие."

    scene back_fizra_guard with fade
    show guard with dissolve
    stop music fadeout 1.0
    play music street

    "{cps=45}{i}Грозный лик охранника преграждает дорогу."
    ohrannik "{cps=45}Документик покажите."
    menu:
        "Да, сейчас студенческий достану.":
            ohrannik "{cps=45}Ну проходи."
        "Усы и хвост - вот мои документы":
            ohrannik "{cps=45}Помнится и я любил бросать остроты, да потом из-за них мне прострелили колено."
            ohrannik "{cps=45}Ладно, скоморох, иди с миром."

    scene black with fade

    "{cps=45}{i}Переодеться в раздевалке не заняло много времени."

    "{cps=45}{i}Но куда дальше идти?"
    "{cps=45}{i}Надо спросить у охранника."
>>>>>>> Stashed changes

    scene back_fizra_guard with dissolve
    show guard with dissolve


    menu:
        "Извините, а где преподавателя найти?":
            pass
    
<<<<<<< Updated upstream
    ohrannik "Обитель наставничья, что методическим кабинетом зовётся, сразу за углом располагается."


    scene fizra_room with dissolve
    show prepod_fizra with dissolve

    #change
    prepod "Ну здравствуй!"
    prepod "Я тебя тут раньше не видел."
    prepod "У первого курса сегодня занятия в тренажерке на минус первом этаже."
    prepod "Давай, иди, не мешай работать."


    scene back_fizra_gym with fade
    "Найти тренажёрку было несложно. Бодрую музыку из неё слышно за километр."

    #change
    show dungeonmaster with dissolve
    DM "Welcome!"
    DM "Этот сотрудник политеха известен как Dungeon Master."
    DM "У нас тут, как ты видишь, обстановка способствует наращиванию мышц и духа."
    "Действительно, душок тут уже нарастили."
    DM "Для начала нужно рассказать тебе технику безопасности."
    DM "Во-первых обязательно нужно быть в спортивной форме."
    DM "Имеются в виду предметы одежды. Физической формой мы вас обеспечим на занятии."
    DM "Далее… Если у плохое самочувствие или травма, то заниматься нельзя. Если почувствовали себя плохо во время занятия, немедленно останавливаетесь и сообщаете мне."
    DM "Скажу очевидное: меня надо слушать. Делай как я говорю. Железо не терпит неправильно обращения."
    DM "Без разминки ничё нельзя."
    DM "К движущимся частям блочных устройств прикасаться запрещено."
    DM "Людей которые выполняют упражнения не трогать и речами не донимать."
    DM "Жим лёжа в одиночку проводить нельзя, надо чтоб кто-нибудь страховал."
    DM "И блины со штанги нужно снимать так, чтобы не возникало разницы между сторонами в более чем один блин."
    DM "Со спортивным инвентарём обращаемся бережно."
    DM "И ещё надо брать с собой водичку."
    DM "Ладно, вы тут сплошняком айтишники, так что с железом знакомы."
    "Шутканул так шутканул."
    DM "Кстати, справка о группе здоровья у тебя есть?"
    "Справка была при себе."
    DM "Отдашь мне копию потом."
    DM "Вот тут распишись за технику безопасности и можем приступать."
    "Занятие шло своим чередом."
    "А пока оно шло, в голову пришла умная мысля"
    "Как вообще получить зачёт?"
    "С этим вопросом пришлось обратиться к преподавателю."
    DM "Для зачёта главное собрать достаточно баллов."
    DM "Баллы даются за различные спортивные достижения и участие в спортивных мероприятиях университета, за посещения занятий, за сдачу нормативов и за то, что вы ходите в другие спортивные учреждения."
    DM "В исключительных случаях баллы могут поставить за работу на электронной платформе и научно-исследовательскую работу."
    DM "В первом семестре вы все занимаетесь со своими группами. Потом вы сможете выбирать время и специализацию, куда будете ходить."
    DM "У нас есть на выбор:"
    "Преподаватель достаёт бумажку и начинает читать с неё"
    DM "Для основной и подготовительной группы здоровья:"
    DM "баскетбол, качалка и аэробика - в нашем корпусе, и ещё ОФП, мини-футбол пауэрлифтинг,  кроссфит, стритлифтинг, армлифтинг и волейбол в других."
    DM "Для специальной медицинской группы:"
    DM "Скандинавская ходьба и настольный теннис у нас и специальная ОФП в других корпусах."
    DM "Выбирайте что хотите и записывайтесь на любое свободное время."
    DM "Но это всё потом. Маленькие ещё."
    "Препод был явно доволен своей колкостью"
    DM "Ну ладно, я как босс этой качалки объявляю занятие оконченным."
    
=======
    ohrannik "{cps=45}Обитель наставничья, что методическим кабинетом зовётся, сразу за углом располагается."

    scene fizra_room with dissolve
    show prepod_fizra with dissolve

    #change
    prepod "{cps=45}Ну здравствуй!"
    prepod "{cps=45}Я тебя тут раньше не видел."
    prepod "{cps=45}У первого курса сегодня занятия в тренажерке на минус первом этаже."
    prepod "{cps=45}Давай, иди, не мешай работать."


    scene back_fizra_gym with fade
    stop music fadeout 1.0
    play music metal

    "{cps=45}{i}Найти тренажёрку было несложно. Бодрую музыку из неё слышно за километр."

    #change
    show dungeonmaster with dissolve
    DM "{cps=45}Welcome!"
    DM "{cps=45}Этот сотрудник политеха известен как Dungeon Master."
    DM "{cps=45}У нас тут, как ты видишь, обстановка способствует наращиванию мышц и духа."
    "{cps=45}{i}Действительно, душок тут уже нарастили."
    DM "{cps=45}Для начала нужно рассказать тебе технику безопасности."
    DM "{cps=45}Во-первых обязательно нужно быть в спортивной форме."
    DM "{cps=45}Имеются в виду предметы одежды. Физической формой мы вас обеспечим на занятии."
    DM "{cps=45}Далее… Если у плохое самочувствие или травма, то заниматься нельзя. Если почувствовали себя плохо во время занятия, немедленно останавливаетесь и сообщаете мне."
    DM "{cps=45}Скажу очевидное: меня надо слушать. Делай как я говорю. Железо не терпит неправильно обращения."
    DM "{cps=45}Без разминки ничё нельзя."
    DM "{cps=45}К движущимся частям блочных устройств прикасаться запрещено."
    DM "{cps=45}Людей которые выполняют упражнения не трогать и речами не донимать."
    DM "{cps=45}Жим лёжа в одиночку проводить нельзя, надо чтоб кто-нибудь страховал."
    DM "{cps=45}И блины со штанги нужно снимать так, чтобы не возникало разницы между сторонами в более чем один блин."
    DM "{cps=45}Со спортивным инвентарём обращаемся бережно."
    DM "{cps=45}И ещё надо брать с собой водичку."
    DM "{cps=45}Ладно, вы тут сплошняком айтишники, так что с железом знакомы."
    "{cps=45}{i}Шутканул так шутканул."
    DM "{cps=45}Кстати, справка о группе здоровья у тебя есть?"
    "{cps=45}{i}Справка была при себе."
    DM "{cps=45}Отдашь мне копию потом."
    DM "{cps=45}Вот тут распишись за технику безопасности, и можем приступать."
    "{cps=45}{i}Занятие шло своим чередом."
    "{cps=45}{i}А пока оно шло, в голову пришла умная мысля"
    "{cps=45}{i}Как вообще получить зачёт?"
    "{cps=45}{i}С этим вопросом пришлось обратиться к преподавателю."
    DM "{cps=45}Для зачёта главное собрать достаточно баллов."
    DM "{cps=45}Баллы даются за различные спортивные достижения и участие в спортивных мероприятиях университета, за посещения занятий, за сдачу нормативов и за то, что вы ходите в другие спортивные учреждения."
    DM "{cps=45}В исключительных случаях баллы могут поставить за работу на электронной платформе и научно-исследовательскую работу."
    DM "{cps=45}В первом семестре вы все занимаетесь со своими группами. Потом вы сможете выбирать время и специализацию, куда будете ходить."
    DM "{cps=45}У нас есть на выбор:"
    "{cps=45}{i}Преподаватель достаёт бумажку и начинает читать с неё"
    DM "{cps=45}Для основной и подготовительной группы здоровья:"
    DM "{cps=45}баскетбол, качалка и аэробика - в нашем корпусе, и ещё ОФП, мини-футбол пауэрлифтинг,  кроссфит, стритлифтинг, армлифтинг и волейбол в других."
    DM "{cps=45}Для специальной медицинской группы:"
    DM "{cps=45}Скандинавская ходьба и настольный теннис у нас и специальная ОФП в других корпусах."
    DM "{cps=45}Выбирайте что хотите и записывайтесь на любое свободное время."
    DM "{cps=45}Но это всё потом. Маленькие ещё."
    "{cps=45}{i}Препод был явно доволен своей колкостью."
    DM "{cps=45}Ну ладно, я как босс этой качалки объявляю занятие оконченным."
    stop music fadeout 1.0

>>>>>>> Stashed changes
    return










        


label runWithVitalik:
    scene fizra
    with fade

    
    
<<<<<<< Updated upstream
    "С первых секунд очевидно, что за Виталиком не угнаться."
    "Можно списать всё на ноутбук болтающийся в рюкзаке за спиной, но это лишь самоутешение."
    "Скандинавская ходьба сделала Виталика невероятно быстрым и выносливым."
    "Для неподготовленного человека этот забег будет настоящим испытанием."
    "Впрочем долой раздумья, нужно сосредоточится."
    "Я скорость…"
    "Я скорость…"
    "С электрическим гулом мимо проносится самокат."
    "А ведь возле входа в универ этих самокатов целая куча валялась."
    "Обидно, но обратного пути уже нет, надо бежать."
    "Не время об этом думать, нужно бежать."
    "раз, два, раз, два, раз, два…"
    "А силы уже потихоньку покидают тело"
    "Виталик уже скрылся за горизонтом."
=======
    "{i}С первых секунд очевидно, что за Виталиком не угнаться."
    "{i}Можно списать всё на ноутбук болтающийся в рюкзаке за спиной, но это лишь самоутешение."
    "{i}Скандинавская ходьба сделала Виталика невероятно быстрым и выносливым."
    "{i}Для неподготовленного человека этот забег будет настоящим испытанием."
    "{i}Впрочем долой раздумья, нужно сосредоточится."
    "{i}Я скорость…"
    "{i}Я скорость…"
    "{i}С электрическим гулом мимо проносится самокат."
    "{i}А ведь возле входа в универ этих самокатов целая куча валялась."
    "{i}Обидно, но обратного пути уже нет, надо бежать."
    "{i}Не время об этом думать, нужно бежать."
    "{i}раз, два, раз, два, раз, два…"
    "{i}А силы уже потихоньку покидают тело."
    "{i}Виталик уже скрылся за горизонтом."
>>>>>>> Stashed changes
    call RunChoice from _call_RunChoice
    return



label RunChoice:
    define les = False
    define vpered = False
    menu:
        "Бежать как лес.":
            if les == False:
<<<<<<< Updated upstream
                "При повороте головы налево виден пруд, за которым зеленеет густой лес."
                "В голове от таких видов и единения с природой всплывает образ мудрого дуба."
                "Впрочем не нужно быть мудрым дубом, чтобы понять, что лес никуда не убежит и поразглядывать его можно будет как нибудь потом."
                "Надо прибегнуть к другим способам оказаться на паре вовремя."
                $les = True
            else:
                "Я уже бежал как лес. Может попробовать что-то еще?"
=======
                "{i}При повороте головы налево виден пруд, за которым зеленеет густой лес."
                "{i}В голове от таких видов и единения с природой всплывает образ мудрого дуба."
                "{i}Впрочем не нужно быть мудрым дубом, чтобы понять, что лес никуда не убежит и поразглядывать его можно будет как нибудь потом."
                "{i}Надо прибегнуть к другим способам оказаться на паре вовремя."
                $les = True
            else:
                "Может попробовать что-то еще?"
>>>>>>> Stashed changes
            jump RunChoice
        
        "Отвести руки назад и согнуть корпус вперёд.":
            if vpered == False:
<<<<<<< Updated upstream
                "Истинным фанатам японской анимации достоверно известно, что такая конфигурация туловища и присоединённых к нему конечностей значительно улучшает аэродинамическое качество персонажа и даёт ему +100 к скорости."
                "Ранее практическое применение данного умения было сопряжено с некоторыми рисками."
                "Однако, местные органы правопорядка уже давно относятся с пониманием к лицам, перемещающимся подобным образом в этом районе."
                "Всё же у этого умения есть и минусы. При его применении накладывается дебафф, значительно увеличивающий расход стамины."
                "Шиноби должен искать альтернативу."
                $vpered = True
            else:
                "Я не хочу еще раз этого делать."
            jump RunChoice

        "раз, два, раз, два, раз, два…":
            "Спустя некоторое время начинает казаться, что классический подход к бегу действительно эффективен. Ещё бы! Он же основан на бинарной системе счисления “раз-два”. Конечно для программиста ничего лучше не придумать!"
=======
                "{i}Истинным фанатам японской анимации достоверно известно, что такая конфигурация туловища и присоединённых к нему конечностей значительно улучшает аэродинамическое качество персонажа и даёт ему +100 к скорости."
                "{i}Ранее практическое применение данного умения было сопряжено с некоторыми рисками."
                "{i}Однако, местные органы правопорядка уже давно относятся с пониманием к лицам, перемещающимся подобным образом в этом районе."
                "{i}Всё же у этого умения есть и минусы. При его применении накладывается дебафф, значительно увеличивающий расход стамины."
                "{i}Шиноби должен искать альтернативу."
                $vpered = True
            else:
                "{i}Это мы уже проходили."
            jump RunChoice

        "раз, два, раз, два, раз, два…":
            "{i}Спустя некоторое время начинает казаться, что классический подход к бегу действительно эффективен. Ещё бы! Он же основан на бинарной системе счисления “раз-два”. Конечно для программиста ничего лучше не придумать!"
>>>>>>> Stashed changes
    return