from util.constant import PLAYERS_COUNT

greeting = 'Hello. Here you can see the probability of winning your team in a kicker. To start, enter a message like ' \
           '"1, 2, 3, 4", where the first 2 digits correspond to the players of the red team and the second of yellow.'

user_list = '1-Alexey Kadach\n2-Andrey Rykhalski\n3-Alexey Skadorva\n4-Denis Ryaboshtanov\n5-Denis Yankovec\n' \
            '6-Evgeny Krylov\n7-George Ognevoy\n8-Igor Pahomov\n9-Julia Adamchik\n10-Kirill Kovalenko\n' \
            '11-Pavel Yukhnevich\n12-Ruslan Molchanov\n13-Sergey Ilyashenko\n14-Snezhana Lukashik\n' \
            '15-Sergey Makarov\n16-Vadim Siamro\n17-Alina Kovalevskaya\n18-Ilya Tkachev\n19-Maxim Klivenko\n' \
            '20-Ivan Kitsa\n21-Anastasiya Novosyol\n22-Siarhei Hubin\n23-Pavel Gomza\n24-Karina Rene\n' \
            '25-Evgeni Efimenko\n26-Pavel Anosov\n27-George Bisiarin\n28-Vadzim Marchanka'

incorrect_input = 'Sorry but input format is incorrect. Example of input: "1, 2, 3, 4."'

user_not_unique = 'Sorry but players in one request should be unique.'

user_incorrect = 'Sorry but players id is incorrect. It should be: More or equal to 1 and less or equal to ' + \
                 str(PLAYERS_COUNT) + '.'
