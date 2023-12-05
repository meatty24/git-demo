def xxx(message):
    """Выводит тебя из себя напрочь"""
    resp=None
    while resp not in ("yep", "nope"):
        resp=input(message).lower()
    return resp

answer =xxx("Дать Вам по ебалу, месье? [yep/nope]")
print("Твой выбор:", answer)

if answer==("yep"):
    print("По ебалу на")
if answer==("nope"):
    print("Получи по jope")
