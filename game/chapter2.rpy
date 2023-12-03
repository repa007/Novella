
define olga = Character('Ольга', color="#ba00b7")

define student = Character('Я', color="#00baaa")

label startChapter2:
    scene university
    with fade

    "Так. Какая у нас там следующая пара?"
    
    "Хмм теория принятия решений, звучит просто..."
    "Я человек неглупый, решения принимать умею, да и предмет скорее всего разговорный будет."
    "Хотя может стоит надеяться и на что-то поинтереснее."

    scene auditoriya_tpr
    with fade

    show olga
    with dissolve

    olga "Здравствуйте студенты, меня зовут Гостова Ольга Владимировна."

    olga "Вам наверное интересно, о чём будет предмет - теория принятия решений?"
    olga "Начнём с простого. В теории принятия решений есть специальный термин – лицо, принимающее решение, сокращенно ЛПР."
    olga "Это тот, на ком лежит ответственность за принятое решение, тот, кто подписывает приказ или иной документ, в котором выражено решение."
    olga "Есть ещё много понятий важных в этой сфере, например, цели, регламент, риски, ресурсы и критерии оценивания, но пока мы поговорим о математической составляющей."

    olga "Математические модели и методы – необходимый элемент экономической теории на микро- и макроуровне. Их использование позволяет:"
    olga "Во-первых, выделить и формально описать наиболее важные, существенные связи переменных и объектов."
    olga "Во-вторых, из четко сформулированных исходных данных и соотношений методами дедукции можно получать выводы, адекватные изучаемому объекту в той же мере, что и сделанные предпосылки."

    student "Да я в лучшем случае только половину слов понимаю, откуда терминов столько, я же не физике или дискретке сижу..."

    olga "Эй, на галёрке, не отвлекайтесь, это пока самые основы, не зная этого вы вообще у меня зачёт не получите."
    olga "Кстати, о зачёте, есть много правил, которые вам придётся соблюдать, если хотите, чтобы проблем не было."
    olga "Но одно из главных, это соблюдение всех ГОСТов. Они были придуманы не случайно, все вы должны их соблюдать при оформлении любых работ."
    olga "Так, сейчас не об этом. На чём я там остановилась? А точно.."

    olga "В-третьих, методы математики и статистики позволяют индуктивным путем получать новые знания об объекте: оценивать форму и параметры зависимостей его переменных, в наибольшей степени соответствующие имеющимся наблюдениям."
    olga "В-четвёртых, использование языка математики позволяет точно и компактно излагать положения теории, формулировать её понятия и выводы."

    olga "В общем, я думаю вы уже поняли, что пока мы сосредоточимся на математических методах, в такой науке, как принятие решений."
    
    olga "На этом закончим вводную часть лекции, теперь я хотела задать вам пару вопросов."
    olga "Как расшифровывается аббревиатура ЛПР?"

    $a = 0
    menu:
        "Лидер, принимающий решение":
            pass
        "Лабораторно-практическая работа":
            pass
        "Лицо, принимающее решение":
            $a += 1
        "Личные параметры регламента":
            pass


    olga "И ещё один вопрос, что можно получить из четко сформулированных исходных данных и соотношений методами дедукции?"

    menu:
        "Правильное решение":
            pass
        "Выводы, адекватные изучаемому объекту":
            $a += 1
        "Правильный ответ":
            pass
        "Объективный регламентированный способ решения задачи":
            pass
            
    if a == 0:
        olga "Это только первое занятие, а вы уже меня не слушаете, думаю нам трудно будет иметь с вами дело, поэтому сосредоточьтесь сейчас, чтобы не жалеть потом. Пока же я вынуждена поставить вам незачëт."
    elif a == 1:
        olga "Да, с памятью у вас, конечно, не очень, но суть вы улавливаете, поэтому приложите больше усилий и сдадите любой предмет без проблем."
        olga "Хоть и с долей скепсиса, но зачёт вам поставлю."
    else:
        olga "Вот, наконец умные ребята, которые умеют слушать преподавателя, у таких точно проблем не будет, ни с учёбой, ни с сессией, возможно далеко заглядываю, но понятно, что не просто так в ВУЗ поступали."
        olga "А я сама теперь могу с чистым сердцем поставить вам зачёт."
        

    olga "Ладно, на сегодня всё, надеюсь, вы внимательно меня слушали, уверена, это всё вам ещё ни раз пригодится. А пока отпускаю вас в свободное плавание, ещё увидимся."

    scene university
    with fade
    hide olga

    #поменял
    "На сегодня пары закончились."

    "Дома ждёт лучший друг студента - кровать."
   

    

    return