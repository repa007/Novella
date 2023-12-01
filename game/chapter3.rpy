
define yasherov = Character('Ящеров', color="#00780e")

define student = Character('Я', color="#00baaa")

label startChapter3:

    scene black
    with fade

    "*звон будильника"

    scene room
    with fade

    menu:
        "Отложить на 5 минут?"
        "Да":
            student "Пожалуй вздремну еще чуток"
            call prospal from _call_prospal
        "Нет":
            student "Все-таки не буду опаздывать."
            student "Пойду на пару"
            scene auditoria_yascherov
            with fade
            show yasherov


    yasherov "Я раньше работал в другом институте, ещë во времена аспирантуры."
    yasherov "И был у нас один студент, который хорошо общался с преподавателями и многие вопросы решал 'на хороших отношениях'"
    yasherov "В те времена, интернет был только по трафику и его количество на объект было ограничено."
    yasherov "И вот этот студент, получив доступ к управлению сетью вуза, стал перепродавать часть вузовского трафика сторонним лицам." 
    yasherov "По итогу он украл у вуза таким способом много денег и самого трафика."
    yasherov "Дело замяли и завершили тем, что убедили его по собственному забрать документы из института, чтобы не создавать шума."
    yasherov "Потому что в ином случае пострадали и преподаватели, которые предоставили ему доступ к ресурсам вуза и никак не могли бы доказать свою непричастность."
    yasherov "Этот кейс хорошо иллюстрирует то, насколько внимательно нужно относиться к тому, кому предоставляете доступ к ресурсам предприятия."
    yasherov "Именно об этом и будет курс, в первую очередь не о программной защите, а о средствах корпоративной защиты доступа к ресурсам, финансам и данным компании или предприятия."
    yasherov "Вы должны понять ограничения при найме сотрудников, расположении помещений и выборе оборудования и подрядчиков, а также следить за своими сотрудниками во избежание корпоративного шпионажа."
    yasherov "У меня много статей на тему информационной безопасности, и книга, которую вы можете купить в специальных интернет магазинах с научной литературой в бумажном или электронном варианте."
    yasherov "А пока глянь те ка историю, которая идеально вписывается в нашу тему."


    "Комикс"

    yasherov "На сегодня закончим на этом, уверен вы и так всë поняли по моим примерам, проблем у ответственного студента возникнуть не должно."

    return

label prospal:
    scene black
    with fade
    "..."
    scene room
    with fade

    "Нет! Я проспал"
    "Надеюсь преподователь не будет сильно ругаться"

    scene auditoria_yascherov
    with fade

    show yasherov

    yasherov "Добрый день, молодой человек, можете ответить почему я вас не видел на первом занятии?"
    menu:
        "Искренне прошу прощения, я не смог разобраться в сложной архитектуре этого здания и слишком долго искал нужную аудиторию.":
            pass
        "Извините, я болел, поэтому не смог прийти, обещаю, что этого больше не повториться.":
            pass
        "Да тут не здание а лабиринт, фиг найдëшь, куда идти.":
            pass
        "Я задержался, потому что переводил бабушку через дорогу.":
            pass
    yasherov "Ладно, проходи"

    return
