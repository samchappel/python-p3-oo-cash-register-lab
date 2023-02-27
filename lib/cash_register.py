#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
    self.discount = discount
    self.total = 0
    self.items = []
    self.transaction = []

  def add_item(self, title, price, quantity=1):
    self.total += price * quantity
    self.transaction.append( price * quantity)
    for i in range(quantity):
      self.items.append(title)

  def apply_discount(self):
    if (self.discount > 0):
      discount_amount = self.total * self.discount / 100
    # self.total = self.total - discount_amount
      self.total -= discount_amount # shorthand for the line of code above where we are subtracting and reassigning the new total at the same time

      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print('There is no discount to apply.')

  
  def void_last_transaction(self):
    self.total -= self.transaction.pop()
  
