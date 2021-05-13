class Category:
    def __init__(self, ledger):
        self.name_cat = ledger
        self.ledger = ledger
        self.ledger = list()
        self.withdraw_list = list()

    def deposit(self, amount, description=''):
        self.ledger.append({"amount": amount, "description": description})
        return self.ledger

    def withdraw(self, amount, description=''):
        if Category.check_funds(self, amount):
            if amount:
                self.ledger.append({"amount": -amount, "description": description})
                self.withdraw_list.append(amount)
                return True
            else:
                return False
        else:
            return False

    def get_balance(self):
        amount_subtracted = 0
        if self.ledger:
            for i in range(len(self.ledger)):
                if i == 0:
                    continue
                amount_subtracted += self.ledger[i]['amount']
            balance = self.ledger[0]['amount'] + amount_subtracted
            f_balance = '{:.2f}'.format(balance)
            return float(f_balance)
        else:
            return 0

    def transfer(self, amount, other_bud_cat):
        if Category.check_funds(self, amount):
            if amount:
                Category.withdraw(self, amount=amount, description=f"Transfer to {other_bud_cat.name_cat}")
                other_bud_cat.deposit(amount=amount, description=f"Transfer from {self.name_cat}")
                return True
            else:
                return False
        else:
            return False

    def check_funds(self, amount):
        amount_subtracted = 0
        if self.ledger:
            for i in range(len(self.ledger)):
                if i == 0:
                    continue
                amount_subtracted += self.ledger[i]['amount']
            balance = self.ledger[0]['amount'] + amount_subtracted
            if amount > balance:
                return False
            else:
                return True
        else:
            return False

    def __str__(self):

        # Printing name of category
        length = len(self.name_cat)
        if length != 2 and length != 4 and length != 6 and length != 8 and length != 10 and length != 12 and length != 14 and length != 16 and length != 18 and length != 20 and length != 22 and length != 24 and length != 26 and length != 28 and length != 30:
            length -= 1
        stars_needed = float(30 - length)
        f_cat_name = ''
        for i in range(int(stars_needed)):
            f_cat_name += '*'
            if i == (stars_needed / 2) - 1:
                f_cat_name += self.name_cat
            if len(f_cat_name) == 30:
                break

        # Printing and formatting data from ledger------------------------------
        result_line = ''
        for i in range(len(self.ledger)):
            txt = self.ledger[i]['description']
            amnt = '{:.2f}'.format(self.ledger[i]['amount'])

            f_txt = ''
            t_spcs = ''
            if len(txt) < 23:
                t_sp_req = 23 - len(txt)
                for i in range(t_sp_req):
                    t_spcs += ' '
            for i in txt:
                f_txt += i
                if len(f_txt) >= 23:
                    break
            f_txt += t_spcs

            f_amnt = ''
            a_spcs = ''
            if len(amnt) <= 7:
                a_sp_req = 7 - len(amnt)
                for i in range(a_sp_req):
                    a_spcs += ' '
            for i in amnt:
                f_amnt += i
                if len(f_amnt) >= 7:
                    break
            f_amnt = a_spcs + f_amnt

            f_line = f_txt + f_amnt
            result_line += str(f_line) + '\n'

        # getting total
        T_balance = 'Total: ' + str(self.get_balance())

        # Getting final fully formatted result
        final_result = f_cat_name + '\n' + result_line + T_balance

        return final_result

    def get_withdraw(self):
        return self.withdraw_list


def create_spend_chart(cat_list):
    total_withdrawn = 0
    for i in cat_list:
        x = 0
        for j in i.get_withdraw():
            x += j
        total_withdrawn += x

    instances = dict()
    for instance in cat_list:
        instance_name = instance.name_cat
        total_per_inst = 0
        for i in instance.get_withdraw():
            total_per_inst += i
        if round(((total_per_inst / total_withdrawn) * 10)) > 1:
            percent_per_i = round(((total_per_inst / total_withdrawn) * 10)) + 1
        else:
            percent_per_i = round(((total_per_inst / total_withdrawn) * 10))
        instances[instance_name] = percent_per_i

    # ---------------------------------------------------------------------
    lines_list = []
    below_line = 0  # to count number of categories
    key_list = list()
    for key, value in instances.items():
        bar_line = ''
        below_line += 1
        key_list.append(key)
        for i in range(value):
            bar_line += 'o'
        lines_list.append(bar_line)
    f_list = list()
    longest = max(len(word) for word in lines_list)
    for i in lines_list:
        if len(i) == longest:
            f_list.append(i)
        else:
            spaces = ''
            spaces_req = longest - len(i)
            for j in range(spaces_req):
                spaces += ' '

            new_item = spaces + i
            f_list.append(new_item)

    per_list = ['  0| ', ' 10| ', ' 20| ', ' 30| ', ' 40| ', ' 50| ', ' 60| ', ' 70| ', ' 80| ', ' 90| ', '100| ']
    c_list = list()

    f_longest = max(len(word) for word in f_list)
    for i in range(f_longest):
        x = '  '.join(word.ljust(f_longest)[i] for word in f_list) + '  '
        c_list.append(x)

    c_longest = max(len(word) for word in key_list)
    c = ''
    catetory_list = list()
    for i in range(c_longest):
        x = '     '
        c = '  '.join(word.ljust(c_longest)[i] for word in key_list) + '  '
        c = x + c
        catetory_list.append(c)
    catetory_list.reverse()

    y_list = list()
    hyphens = '    '
    for i in range(below_line):
        hyphens += '---'
    hyphens += '-'
    y_list.append(hyphens)

    per_list_len = len(per_list)
    n = -1
    len_clist = -(len(c_list) + 1)
    for i in per_list:
        y = i + c_list[n]
        n -= 1
        y_list.append(y)
        if n == len_clist:
            break
    sp = ''
    for i in per_list[len(c_list):]:
        for j in range(len(hyphens) - 5):
            sp += ' '

        y_list.append(i + sp)
        sp = ''
    # ---------------------------------------------------
    output = ''
    for i in y_list:
        output += i + '\n'

    output_list = catetory_list + y_list
    output_list.reverse()
    final_output = 'Percentage spent by category'
    for i in output_list:
        final_output += '\n' + i
    return final_output


food = Category("Food")
food.deposit(900, "deposit")

entertainment = Category("Entertainment")
entertainment.deposit(900, "deposit")

business = Category("Business")
business.deposit(900, "deposit")

education = Category("Education")
education.deposit(4000, "deposit")

food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
education.withdraw(500)
print(create_spend_chart([business, food, entertainment, education]))
