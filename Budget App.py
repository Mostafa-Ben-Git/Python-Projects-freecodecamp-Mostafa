class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount: float, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description=""):
        if self.check_funds(amount) == True:
            self.ledger.append({"amount": -1 * amount, "description": description})
            return True
        else:
            return False
        

    def get_balance(self):
        balance = 0
        for dict in self.ledger:
            balance += dict['amount']
        return balance

    def transfer(self, amount: float, budget_category):
        if self.check_funds(amount) == True:
            self.ledger.append(
                {"amount": -1 * amount, "description": f"Transfer to {budget_category.name}"}
            )
            budget_category.ledger.append(
                {"amount":  amount, "description": f"Transfer from {self.name}"}
            )
            return True
        else:
            return False
    def check_funds(self,fund:float):
        if fund > Category.get_balance(self):
            return False
        else:
            return True
    def __str__(self):
        title = str(self.name).center(30,'*')
        body = ""
        total= f"Total: {self.get_balance()}"
        for dic in self.ledger:
            left = str(dic['description'])
            right = format(dic['amount'],'.2f')
            body += f'{left[:23].ljust(23)}{right.rjust(7)}\n'
        return f'{title}\n{body}{total}'
def create_spend_chart(categorys:list): #categorys
    # making list with same lenght names base on longest name in categorys
    longest_len_name = len(max([j.name for j in categorys],key=len))
    name_lis = [str(i.name).ljust(longest_len_name) for i in categorys]
    # Extracting total spend of all categorys
    total_spend = 0
    perc_lis = []
    for category in categorys:
        total_withdraw = 0
        for amount in category.ledger:
            if amount['amount'] < 0 :
                total_withdraw += -amount['amount']
                total_spend += -amount['amount']
        perc_lis.append(total_withdraw)
        total_withdraw = 0
    # making list with percentage spend per category
    perc_lis = list(map(lambda x: round(round(x / total_spend * 100),-1),perc_lis))  
    # Parts of the spend Chart
    title= "Percentage spent by category"
    bars = ""
    names=""
    # Printing Bars
    for i in range(11)[::-1]:
        bars += f'{str(i*10).rjust(3)}|'
        for j in perc_lis:
            if j >= i*10:
                bars+=' o '
        bars += '\n'
    bars+= " "*4+str('-'*10)
    # Printing Names in terminal Vertically 
    for i in range(longest_len_name):
        names += ' '*4
        for x in name_lis:
            names += f' {x[i]} '
        names+='\n'
    # Full spand chart
    return f'{title}\n{bars}\n{names}'
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
school = Category('School')
food.deposit(900, "deposit")
food.transfer(400,school)
school.withdraw(150,'PC Gamer')
entertainment.deposit(900, "deposit")
business.deposit(900, "deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)
print(food)
print(business)
print(entertainment)
print(school)

print(create_spend_chart([business, food, entertainment,school]))
