class Pilha:
    def __init__ (self):
        self.items = []

    def isVazio (self):
        return self.items == 0

    def push (self, item):
        if len(self.items) < 30: #A questão da o tamanho
          self.items.append(item)
        else:
          print (" naõ se pode adicionar mais elementos nesta pilha")

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def lenght(self):
        return len(self.items)
        
pilha = Pilha()
