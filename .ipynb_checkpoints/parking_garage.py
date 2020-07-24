class Garage():
    def __init__(self,tickets,parkingSpaces,currentTicket):
        self.tickets = tickets
        self.parkingSpaces = parkingSpaces
        self.currentTicket = currentTicket
    
    def takeTicket(self):
        self.currentTicket[self.ticket[-1]] = ''
        del self.tickets[-1]
        del self.parkingSpaces[-1]
        print('Please take your ticket...')
        



    def payForParking():
        response = input('Please enter your ticket number:')
        if self.currentTicket[response] == '':
            print('Please pay for your ticket...')
            payment = input('Press any key to pay..')
            self.currentTicket[response] = 'paid'
            print('Thanks for parking! You have 15 minutes to exit.')
        else:
            print('Your ticket is already paid! You have 15 minutes to exit the lot.')
        
        
        
        #self.tickets.append(int([-1]+1))
        #self.parkingSpaces.append(int[-1]+1)






    def leaveGarage(self):

        