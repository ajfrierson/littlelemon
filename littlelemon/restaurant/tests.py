from django.test import TestCase


from restaurant.models import Menu, Booking

class MenuModelTestCase(TestCase):
   def test_get_item(self):
      item =Menu.objects.create(
         ID = 1,
         Title = 'Ice Cream',
         Price = 5.99,
         Inventory = 100
      )
      itemstr = item.Title
      self.assertEqual(itemstr, 'Ice Cream')
      self.assertEqual(item.Price, 5.99)
      self.assertEqual(item.Inventory, 100)
      self.assertEqual(item.ID, 1)

class BookingModelTestCase(TestCase):
   def test_get_item(self):
      item = Booking.objects.create(
         ID = 1,
         Name = 'John Doe',
         BookingDate  = '2023-10-01',
         No_of_guests = 4
      )
      itemstr = item.Name
      self.assertEqual(itemstr, 'John Doe')
      self.assertEqual(item.BookingDate, '2023-10-01')
      self.assertEqual(item.No_of_guests, 4)
      self.assertEqual(item.ID, 1)