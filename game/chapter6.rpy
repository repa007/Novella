
define norin = Character('Норинкель', color="#d9ff01")

define student = Character('Я', color="#00baaa")


label startChapter6:
    scene auditoria_chislaki with fade

    "Настал тот час, которого боятся все студенты ИСиТа.."
    "Их нога ступила на порог зловещей башни грозного Норникеля Виктора Петровича"
    "Вокруг гнетущая атмосфера и покрытые печалью лица людей, пришедших сдавать лабораторные"
    "Не видя среди них ни одного радостного, вы понимаете, что пока ни у кого лабы так и не приняли"


    show norin with dissolve
    norin "Так, прошу всех ранее пришедших освободить аудиторию."
    norin "Отсутствие у вас качественно выполненного задания не означает, что я буду тратить на вас время занятия других студентов."
    "Толпа измученных и едва живых студентов выползает из аудитории. Во взгляде каждого из них читается:'Бегите, вы не знаете, куда пришли!!!'"
    norin "Добрый день, товарищи студенты, если вы посещали дистанционные лекционные занятия, то уже должны знать, что меня зовут Норникель Виктор Петрович."
    norin "Если же вы видите и слышите меня впервые, то прошу запомнить, как меня зовут."
    norin "Студент, который в середине семестра защищая лабораторные назовëт меня например, Василий Павлович, на зачëт может не рассчитывать, потому что явно не слушает преподавателя."
    norin "Что ж, начнëм сегодняшнее занятие."
    norin "Процесс решения задачи физики, техники, экономики и, в частности, проектирования конструкций с помощью методов математического моделирования состоит из нескольких основных этапов."
    norin "Первый, исследование объекта и содержательная постановка задачи."
    norin "Второй, построение математической модели."
    norin "Третий, выбор численного метода и разработка вычислительного алгоритма."
    norin "Четвертый, разработка программы или выбор пакета прикладных программ."
    norin "Пятый, проведение вычислений и анализ результатов."
    norin "А теперь, непосредственно о численных методах."
    norin "Чтобы найти корни уравнения F(x) = 0, используется численное решение нелинейных уравнений."
    norin "Итерационный процесс последовательно уточняет значения x, приближаясь к корню."
    norin "Итерации прекращаются, когда разница между последовательными приближениями становится меньше заданной точности ε или когда выполнено условие F(x) ≈ 0. "
    norin "Вот смотрю на вас, а в глазах пустота, понимания в них пока вообще не вижу."
    norin "Это самые основы, так что понять будет не сложно, в первую очередь прошу вас это хотя бы запомнить."
    norin "Ладно, перестану пока вас теорией грузить, но сейчас мне нужно подумать: сразу спросить, запомнили вы хоть что-то или же привести более понятный пример."
    norin "О, точно, придумал как объяснить так, чтобы дошло и до ëжика."
    norin "Допустим, вы с друзьями одной компанией раз в месяц едете в лес, жарить шашлыки."
    norin "Мясо покупают разные люди, и часто его берут либо слишком много, либо слишком мало."
    norin "Тут каждый ваш выезд - это одна итерация, и вы должны понимать, что в любом случае постепенно компания определит точное количество мяса, которое надо купить, чтобы все остались сыты и продукты не пропадали."
    norin "Так уже лучше, теперь у многих в глазах проблески понимания проглядывают."
    norin "Хотя смотрю на других, а они меня еще после слова 'шашлыки' слушать перестали, аж слюнки потекли."
    norin "Понимаю тягости жизни студента, поэтому долго вас мурыжить не стану."
    norin "Просто ответьте на пару моих вопросов и вперëд, можете бежать в столовую."


   

    menu:
        norin "Первый вопрос, что является вторым этапом процесса решения математических задач, методом математического моделирования?"
        "Разработка программы или выбор пакета прикладных программ.":
            call falseAnswer1 from _call_falseAnswer1
        "Выбор численного метода и разработка вычислительного алгоритма.":
            call falseAnswer1 from _call_falseAnswer1_1
        "Построение математической модели.":
            call trueAnswer1 from _call_trueAnswer1
        "Проведение вычислений и анализ результатов.":
            call falseAnswer1 from _call_falseAnswer1_2

    
    

    menu:
        norin "Вопрос второй: Когда прекращаются итерации при при численном решении нелинейных уравнений?"
        "Когда разница между последовательными приближениями становится меньше заданной точности ε .":
            call trueAnswer2 from _call_trueAnswer2
        "Когда необходимое значение x, подходящее под условия задачи.":
            call falseAnswer2 from _call_falseAnswer2
        "Когда выполнено условие F(x) != 0.":
            call falseAnswer2 from _call_falseAnswer2_1
        "Когда выполнено условие F(x) ≈ 0.":
            call trueAnswer2 from _call_trueAnswer2_1
    return



label trueAnswer3:
    norin "Что ж, раз я обещал, то слова свои забирать не стану, вы получаете зачëт, но учтите, я ещë буду вести у вас другой предмет, так что даже не надейтесь на снисходительность в следующий раз."
    return

label falseAnswer3:
    norin "Вы даже имя преподавателя запомнить не удосужились, о чëм тогда вообще говорить."
    norin "Ставлю вам незачëт, но не переживайте, мы с вами встретимся ещë не раз."
    norin "А именно на другом моëм предмете, уже на следующем курсе, и разумеется на вашей пересдаче."
    return

label falseAnswer2:
    menu:
        norin "Как я вижу понимания предмета у вас всë-таки нет, остаëтся надеяться на память, если сможете правильно назвать моë имя и отчество, с огромной натяжкой, но зачëт поставлю."
        "Василий Павлович":
            call falseAnswer3 from _call_falseAnswer3
        "Виктор Петрович":
            call trueAnswer3 from _call_trueAnswer3
        "Владимир Платонович":
            call falseAnswer3 from _call_falseAnswer3_1
        "Виталий Пахомович":
            call falseAnswer3 from _call_falseAnswer3_2
    return


label trueAnswer2:
    norin "Что ж, поздравляю вас с зачëтом, когда он есть уже не важно, были до этого ошибки или нет."
    return


label falseAnswer1:
    norin "А я смотрю кое-кто решил меня не слушать ещë когда вошëл в аудиторию..."
    norin "Ладно дам ещë попытку, понимаю, что мог отвлечься."
    return

label trueAnswer1:
    norin "Молодец, видно, что не стал игнорировать преподавателя с самого начала занятия, ответишь ещë на один и считай зачëт у тебя в кармане."
    return