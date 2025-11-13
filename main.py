import dice, monster

tracker_list = monster.tracker_list

monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))
monster.Monster("Goblin", 2, dice.set_dices("3w4"))

while True:
    monster.show_list()
    main_input = input("> ")
    command = main_input.split(" ")
    if command[0] == "change":
        target = int(command[1])
        command_input = input("How much damage does he take? > ")
        print(command_input)
        command_input = int(command_input)
        print(type(command_input))
        tracker_list[target].cur_hp -= max(0,command_input)
        tracker_list[target].check_if_dead()
