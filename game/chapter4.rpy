
define student = Character('Я', color="#00baaa")

define ohrannik = Character('Охранник', color="#003bba")


define prepod = Character('Фирук', color="#00ff1a")

label startChapter4:
    scene university
    with fade
    "На сегодня всё. Можно и домой."
    "Хотя есть нюанс…"
    "Физкультура сама на себя ходить не будет."
    "Затягивать с посещением данной дисциплины больше нельзя."
    "Говорилось, что спортзал где-то неподалёку."

    scene street
    with fade

    "Спортзал в километре отсюда… А до начала пары 5 минут."
    "Проблема…"
    "А кто это накачанный и в фирменной футболке политеха несётся в обозначенном картами направлении?"

    show vitalik
    with dissolve

    "Это же местная знаменитость! Виталик “скандинавская ходьба”."
    "Вероятно он тоже торопится на занятие."

    menu:
        "Побежать за Виталиком":
            call runWithVitalik
        "Осмотреться":
            show back_fizra_scuters
            with fade
            "Возле крыльца стоит великое множество электросамокатов. Решение найдено!"
            "Данное средство индивидуальной мобильности разрушает представление о скорости."
            "Впрочем главное не разрушиться об столб или автомобиль."
            "Резкие манёвры с запредельными перегрузками, достойными опытного лётчика-истребителя, позволили избежать коллизии."
            "Электросамокат настолько быстр, что почти удалось догнать Виталика, хотя тот к концу дистанции всё ещё сохранял отрыв."

    "Благодаря нечеловеческим усилиям порог преодолён вовремя. Но впереди возникает следующее препятствие."

    scene blue with dissolve
    show guard with dissolve

    "Грозный лик охранника преграждает дорогу"
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

    scene blue with dissolve
    show guard with dissolve


    menu:
        "Извините, а где преподавателя найти?":
            pass
    
    ohrannik "Обитель наставничья, что методическим кабинетом зовётся, сразу за углом располагается."


    scene yellow with dissolve
    show prepod_fizra with dissolve

    #change
    prepod "Ну здравствуй!"
    prepod "Я тебя тут раньше не видел."
    prepod "У первого курса сегодня занятия в тренажерке на минус первом этаже."
    prepod "Давай, иди, не мешай работать."


    scene back_fizra_gym with fade
    "Найти тренажёрку было несложно. Бодрую музыку из неё слышно за километр."

    #change
    show prepod_fizra with dissolve
    prepod "Welcome!"
    prepod "Этот сотрудник политеха известен как Dungeon Master."
    prepod "У нас тут, как ты видишь, обстановка способствует наращиванию мышц и духа."
    "Действительно, душок тут уже нарастили."
    prepod "Для начала нужно рассказать тебе технику безопасности."
    prepod "Во-первых обязательно нужно быть в спортивной форме."
    prepod "Имеются в виду предметы одежды. Физической формой мы вас обеспечим на занятии."
    prepod "Далее… Если у плохое самочувствие или травма, то заниматься нельзя. Если почувствовали себя плохо во время занятия, немедленно останавливаетесь и сообщаете мне."
    prepod "Скажу очевидное: меня надо слушать. Делай как я говорю. Железо не терпит неправильно обращения."
    prepod "Без разминки ничё нельзя."
    prepod "К движущимся частям блочных устройств прикасаться запрещено."
    prepod "Людей которые выполняют упражнения не трогать и речами не донимать."
    prepod "Жим лёжа в одиночку проводить нельзя, надо чтоб кто-нибудь страховал."
    prepod "И блины со штанги нужно снимать так, чтобы не возникало разницы между сторонами в более чем один блин."
    prepod "Со спортивным инвентарём обращаемся бережно."
    prepod "И ещё надо брать с собой водичку."
    prepod "Ладно, вы тут сплошняком айтишники, так что с железом знакомы."
    "Шутканул так шутканул."
    prepod "Кстати, справка о группе здоровья у тебя есть?"
    "Справка была при себе."
    prepod "Отдашь мне копию потом."
    prepod "Вот тут распишись за технику безопасности и можем приступать."
    "Занятие шло своим чередом."
    "А пока оно шло, в голову пришла умная мысля"
    "Как вообще получить зачёт?"
    "С этим вопросом пришлось обратиться к преподавателю."
    prepod "Для зачёта главное собрать достаточно баллов."
    prepod "Баллы даются за различные спортивные достижения и участие в спортивных мероприятиях университета, за посещения занятий, за сдачу нормативов и за то, что вы ходите в другие спортивные учреждения."
    prepod "В исключительных случаях баллы могут поставить за работу на электронной платформе и научно-исследовательскую работу."
    prepod "В первом семестре вы все занимаетесь со своими группами. Потом вы сможете выбирать время и специализацию, куда будете ходить."
    prepod "У нас есть на выбор:"
    "Преподаватель достаёт бумажку и начинает читать с неё"
    prepod "Для основной и подготовительной группы здоровья:"
    prepod "баскетбол, качалка и аэробика - в нашем корпусе, и ещё ОФП, мини-футбол пауэрлифтинг,  кроссфит, стритлифтинг, армлифтинг и волейбол в других."
    prepod "Для специальной медицинской группы:"
    prepod "Скандинавская ходьба и настольный теннис у нас и специальная ОФП в других корпусах."
    prepod "Выбирайте что хотите и записывайтесь на любое свободное время."
    prepod "Но это всё потом. Маленькие ещё."
    "Препод был явно доволен своей колкостью"
    prepod "Ну ладно, я как босс этой качалки объявляю занятие оконченным."
    
    return










        


label runWithVitalik:
    scene fizra
    with fade

    
    
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
    call RunChoice
    return



label RunChoice:
    define a = False
    define b = False
    menu:
        "Бежать как лес.":
            if a == False:
                "При повороте головы налево виден пруд, за которым зеленеет густой лес."
                "В голове от таких видов и единения с природой всплывает образ мудрого дуба."
                "Впрочем не нужно быть мудрым дубом, чтобы понять, что лес никуда не убежит и поразглядывать его можно будет как нибудь потом."
                "Надо прибегнуть к другим способам оказаться на паре вовремя."
                $a = True
            else:
                "Я уже бежал как лес. Может попробовать что-то еще?"
            jump RunChoice
        
        "Отвести руки назад и согнуть корпус вперёд.":
            if b == False:
                "Истинным фанатам японской анимации достоверно известно, что такая конфигурация туловища и присоединённых к нему конечностей значительно улучшает аэродинамическое качество персонажа и даёт ему +100 к скорости."
                "Ранее практическое применение данного умения было сопряжено с некоторыми рисками."
                "Однако, местные органы правопорядка уже давно относятся с пониманием к лицам, перемещающимся подобным образом в этом районе."
                "Всё же у этого умения есть и минусы. При его применении накладывается дебафф, значительно увеличивающий расход стамины."
                "Шиноби должен искать альтернативу."
                $b = True
            else:
                "Я не хочу еще раз этого делать."
            jump RunChoice

        "раз, два, раз, два, раз, два…":
            "Спустя некоторое время начинает казаться, что классический подход к бегу действительно эффективен. Ещё бы! Он же основан на бинарной системе счисления “раз-два”. Конечно для программиста ничего лучше не придумать!"
    return