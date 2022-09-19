import argparse

class Car:
	def __init__(self,register_number,color):
		self.color =  color
		self.register_number = register_number

class ParkingLot:
    def __init__(self):
        self.capacity = 0
        self.slotid = 0
        self.alloted_seats_slots = 0

    def createParkingLot(self, capacity):
        if capacity:
            self.slots = [-1] * capacity
            self.capacity = capacity
            return self.capacity
        else:
            return "Please enter capacity"

    def getEmptySlot(self):
        for i in range(len(self.slots)):
            if self.slots[i] == -1:
                return i

    def park(self, register_number, color):
        if self.alloted_seats_slots < self.capacity:
            slotid = self.getEmptySlot()
            self.slots[slotid] = Car(register_number, color)
            self.slotid = self.slotid + 1
            self.alloted_seats_slots = self.alloted_seats_slots + 1
            return slotid + 1
        else:
            return -1

    def leave(self, slotid):

        if self.alloted_seats_slots > 0 and self.slots[slotid - 1] != -1:
            self.slots[slotid - 1] = -1
            self.alloted_seats_slots = self.alloted_seats_slots - 1
            return True
        else:
            return False

    def status(self,file_output=''):
        if file_output:
            ptr="Slot No.\tRegistration No.\tColour\n"
        else:
            print("Slot No.\tRegistration No.\tColour")
        for i in range(len(self.slots)):
            if self.slots[i] != -1:
                if file_output:
                    ptr+=(str(i + 1) + "\t\t" + str(self.slots[i].register_number) + "\t\t" + str(self.slots[i].color))
                else:
                    print(str(i + 1) + "\t\t" + str(self.slots[i].register_number) + "\t\t" + str(self.slots[i].color))
            else:
                continue
        if file_output and  self.slots[i] != -1:
            return ptr

    def getregister_numberFromColor(self, color):
        register_numbers = []
        if self.capacity != 0:
            for i in self.slots:
                if i == -1:
                    continue
                if i.color == color:
                    register_numbers.append(i.register_number)
            return register_numbers
        else:
            return "slot not created"

    def getSlotNoFromregister_number(self, register_number):
        for i in range(len(self.slots)):
            # print(self.slots[i].register_number)
            if self.slots[i].register_number == register_number:
                return i + 1
            else:
                continue
        return -1

    def getSlotNoFromColor(self, color):

        slotnos = []

        for i in range(len(self.slots)):

            if self.slots[i] == -1:
                continue
            if self.slots[i].color == color:
                slotnos.append(str(i + 1))
        return slotnos

    def show(self, line, file_output=''):
        if line.startswith('create_parking_lot'):
            n = int(line.split(' ')[1])
            res = self.createParkingLot(n)
            if file_output:
                return 'Created a parking lot with ' + str(res) + ' slots'
            else:
                print('Created a parking lot with ' + str(res) + ' slots')

        elif line.startswith('park'):
            register_number = line.split(' ')[1]
            color = line.split(' ')[2]
            res = self.park(register_number, color)
            if res == -1:
                if file_output:
                    return("Sorry, parking lot is full")
                else:
                    print("Sorry, parking lot is full")
            else:
                if file_output:
                    return('Allocated slot number: ' + str(res))
                else:
                    print('Allocated slot number: ' + str(res))

        elif line.startswith('leave'):
            leave_slotid = int(line.split(' ')[1])
            status = self.leave(leave_slotid)
            if status:
                if file_output:
                    return('Slot number ' + str(leave_slotid) + ' is free')
                else:
                    print('Slot number ' + str(leave_slotid) + ' is free')

        elif line.startswith('status'):
            if file_output:
                return self.status("file_output")
            else:
                self.status()

        elif line.startswith('registration_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            register_numbers = self.getregister_numberFromColor(color)
            if 'slot not created' in register_numbers:
                if file_output:
                    return('Please create parking slot first')
                else:
                    print('Please create parking slot first')
            else:
                if file_output:
                    return(', '.join(register_numbers))
                else:
                    print(', '.join(register_numbers))

        elif line.startswith('slot_numbers_for_cars_with_colour'):
            color = line.split(' ')[1]
            slotnos = self.getSlotNoFromColor(color)
            if file_output:
                return(', '.join(slotnos))
            else:
                print(', '.join(slotnos))

        elif line.startswith('slot_number_for_registration_number'):
            register_number = line.split(' ')[1]
            slotno = self.getSlotNoFromregister_number(register_number)
            if slotno == -1:
                if file_output:
                    return"Not found"
                else:
                    print("Not found")
            else:
                if file_output:
                    return slotno
                else:
                    print(slotno)

        elif line.startswith('exit'):
            exit(0)


def main():
    parkinglot = ParkingLot()
    parser = argparse.ArgumentParser()
    parser.add_argument('--gt', dest='src_file')
    args = parser.parse_args()

    if args.src_file:
        dest_file = open('file_output.txt', 'w')
        with open(args.src_file) as f:
            for line in f:
                l1=parkinglot.show(line, "file_output")
                dest_file.writelines(l1)
                dest_file.write('\n')
    else:
        while True:
            line = input("$ ")
            parkinglot.show(line)


if __name__ == '__main__':
    main()