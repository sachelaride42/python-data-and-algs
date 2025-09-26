class Category:
    def __init__(self, category):
        self.category = category
        self.ledger = []
        self.funds = 0
        self.spent = 0

    def __str__(self):
        return_string = ''
        length = len(self.category)
        n_stars = 30 - length
        stars_left = n_stars // 2
        stars_right = 30 - length - stars_left
        title = ('*' * stars_left) + self.category + ('*' * stars_right)
        return_string += title + '\n'

        for item in self.ledger:
            if len(item['description']) > 23:
                item_desc = item['description'][0:23]
            else:
                item_desc = item['description']

            txt_amount = f"{item['amount']:.2f}"
            if len(txt_amount) > 7:
                item_amount = txt_amount[0:7]
            else:
                item_amount = txt_amount
            n_spaces = 30 - len(item_desc) - len(item_amount)
            return_string += item_desc + ' ' * n_spaces + item_amount + '\n'

        cat_total = f'Total: {self.funds:.2f}'
        return_string += cat_total
        return return_string

    def deposit(self, amount, description=''):
        self.funds += amount
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description=''):
        if not self.check_funds(amount):
            return False
        else:
            self.spent += amount
            self.funds -= amount
            self.ledger.append({'amount': amount * -1, 'description': description})
            return True

    def get_balance(self):
        return self.funds

    def transfer(self, amount, obj_category):
        if not self.check_funds(amount):
            return False
        else:
            self.withdraw(amount, f'Transfer to {obj_category.category}')
            obj_category.deposit(amount, f'Transfer from {self.category}')
            return True

    def check_funds(self, amount):
        if amount > self.funds:
            return False
        else:
            return True


def create_spend_chart(list_categories):
    text = 'Percentage spent by category'
    text += '\n'
    total_spent = 0
    list_percentages = []
    list_names = []
    for category in list_categories:
        total_spent += category.spent
        print(category.spent)
        list_names.append(category.category)
    print(total_spent)
    for category in list_categories:
        percentage = category.spent / total_spent * 100 - ((category.spent / total_spent) * 100 % 10)
        list_percentages.append(percentage)
    # print(list_percentages)
    # print(list_names)
    for n in range(100, -10, -10):
        if n == 100:
            text += f'{n}| '
        elif n != 0:
            text += f' {n}| '
        else:
            text += f'  0| '
        for percentage in list_percentages:
            if percentage >= n:
                text += 'o  '
            else:
                text += '   '
        text += '\n'
    n_stars = 1 + 3 * len(list_categories)
    text += 4 * ' ' + '-' * n_stars + '\n'

    bigger_name_size = len(max(list_names, key=len))
    for i in range(0, bigger_name_size):
        text += 5 * ' '
        for name in list_names:
            if i >= len(name):
                text += ' ' * 3
            else:
                text += name[i] + ' ' * 2
        if i != bigger_name_size - 1:
            text += '\n'

    print(text)
    return text


food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(25, 'groceries')
food.withdraw(25, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.withdraw(50)
create_spend_chart([food, clothing])

