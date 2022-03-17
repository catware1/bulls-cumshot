# Вы можете расположить сценарий своей игры в этом файле.

# Ресурсы игры - шрифт
define gui.interface_text_font = "stuff/Inter-Medium.ttf"

# Сцены
image bg default = Tile("bluewaves.png")  # Синие волны из главного меню игры
image bg vyatka = Tile("vyatka.jpg")
image bg pomoyka = Tile("pomoyka.jpg")

# Скины персонажей
image gman default = "Gman.png"
image gman fucked = "Gman_fucked.png"
image biden default = "biden.png"
image down default = "grafik.png"


# Определение персонажей игры.
define gman = Character('Хуесос из полжизни2')
define game = Character('ИДЁТ ЗАПУСК РАКЕТ НА США... 10%')


# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    stop music fadeout 1.0

    scene bg default

    show gman default

    gman "Приветствую. Вероятнее всего, мои выводы покажутся Вам слишком поспешными."
    gman "Да, я тот самый мужик в костюме из второй халфы, но в итоге меня спиздили и продали в рабство Юрия Киселёва."
    gman "Пожалуйста, спасите меня."
    gman "Нахуя ты скачал это говно?"
    show gman fucked
    gman "А хотя... отличая игра (только не бейте)"
    hide gman
    scene bg vyatka
    game 'Все действия происходили в самой жопе России, а именно городе Кирове.'
    scene bg pomoyka
    game 'Казалось бы, какое неожиданное фото провинциальных помоек, но вот что я вам скажу...'
    show biden default
    game 'Именно здесь лежал сам Джо Байден.'
    game '«Неудивительно» - наверняка подумали Вы, но у меня ещё есть кое-что для Вас.'
    hide biden
    show down default
    game 'Это - экономика США и других стран Европы, потому что они обосрались. Ну да ладно, я тоже.'
    
    

    return
