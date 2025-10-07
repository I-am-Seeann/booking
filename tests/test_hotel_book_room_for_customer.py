import pytest

from customer import Customer
from hotel import Hotel
from room import Room

class TestHotelBookRoomForCustomer:

    @pytest.fixture
    def sample_rooms(self):
        return [
            Room(1, "Single", 100, 1, is_available=True),
            Room(2, "Double", 200, 2, is_available=True),
            Room(3, "Single", 300, 3, is_available=False)
        ]

    @pytest.fixture
    def sample_hotel(self, sample_rooms):
        return Hotel("California", sample_rooms)

    @pytest.fixture
    def customer_with_sufficient_balance(self):
        return Customer("Rich", 1000.0)

    @pytest.fixture
    def poor_customer(self):
        return Customer("Ana", 50.0)

    def test_successful_booking_available_room(self, sample_hotel, customer_with_sufficient_balance):
        room_number = 1
        nights = 3
        room = sample_hotel.find_room_by_number(room_number)

        result = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        assert result is True
        assert not room.is_available
        assert room in customer_with_sufficient_balance.booked_rooms
        assert len(customer_with_sufficient_balance.booked_rooms) == 1

    def test_booking_unavailable_room(self, sample_hotel, customer_with_sufficient_balance):
        room_number = 3
        nights = 2

        result = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        assert result is False
        assert len(customer_with_sufficient_balance.booked_rooms) == 0

    def test_booking_nonexistent_room(self, sample_hotel, customer_with_sufficient_balance):
        room_number = 999
        nights = 2

        result = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        assert result is False
        assert len(customer_with_sufficient_balance.booked_rooms) == 0

    def test_booking_with_insufficient_budget(self, sample_hotel, poor_customer):
        room_number = 2
        nights = 3
        room = sample_hotel.find_room_by_number(room_number)

        result = sample_hotel.book_room_for_customer(poor_customer, room_number, nights)

        assert result is False
        assert room.is_available
        assert len(poor_customer.booked_rooms) == 0

    def test_booking_multiple_rooms_successfully(self, sample_hotel, customer_with_sufficient_balance):
        room1_number = 1
        room2_number = 2
        nights = 2

        result1 = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room1_number, nights)

        result2 = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room2_number, nights)

        assert result1 is True
        assert result2 is True
        assert len(customer_with_sufficient_balance.booked_rooms) == 2

    def test_booking_same_room_twice(self, sample_hotel, customer_with_sufficient_balance):
        room_number = 1
        nights = 2

        result1 = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        result2 = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        assert result1 is True
        assert result2 is False
        assert len(customer_with_sufficient_balance.booked_rooms) == 1

    def test_booking_with_zero_nights(self, sample_hotel, customer_with_sufficient_balance):
        room_number = 1
        nights = 0
        room = sample_hotel.find_room_by_number(room_number)

        result = sample_hotel.book_room_for_customer(customer_with_sufficient_balance, room_number, nights)

        assert result is False
        assert room.is_available
        assert room not in customer_with_sufficient_balance.booked_rooms