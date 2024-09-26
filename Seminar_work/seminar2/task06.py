balans = 0
nalog = 0
count = 0
sanctions = 5_000_000
while True:
    if count % 3 == 0:
        balans = balans / 100 * 103
        print(f'{balans = }')
    action = input('Enter a command from the list: replenish, take_off, exit: ')
    match action:
        case "replenish":
            print(f' {balans = }')
            if balans > sanctions:
                balans = balans / 100 * 90
                print(f' {balans = }')
            add_money = int(input('How much do you want to top up: '))
            if add_money % 50 == 0:
                balans += add_money
                print(f' {balans = }')
            count += 1

        case "take_off":
            print(f' {balans = }')
            if balans > sanctions:
                balans = balans / 100 * 90
                print(f' {balans = }')
            take_it_away_money = int(input('How much money do you want to withdraw: '))
            if take_it_away_money <= balans:
                if take_it_away_money % 50 == 0:
                    nalog = take_it_away_money / 100 * 1.5
                    if nalog < 30:
                        nalog = 30
                    elif nalog > 600:
                        nalog = 600

                    print(f' {nalog = }')
                    balans = balans - take_it_away_money - nalog
                    print(f' {balans = }')
                    count += 1

        case "exit":
            break
        case _:
            break