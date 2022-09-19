import unittest
from my_program import ParkingLot
class TestParkingLot(unittest.TestCase):

	def test_create_parking_lot_positive(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot(6)
		self.assertEqual(6,res)

	def test_create_parking_lot_negative(self):
		parkingLot = ParkingLot()
		res = parkingLot.createParkingLot()
		self.assertEqual('Please enter capacity',res)

if __name__ == '__main__':
	unittest.main()