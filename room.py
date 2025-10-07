class Room:
    def __init__(self, room_number: int, room_type: str, price_per_night: int,
                 max_guests: int, is_available: bool = True) -> None:
        if price_per_night <= 0:
            raise ValueError("Price per night must be positive")
        if max_guests <= 0:
            raise ValueError("Max guests must be positive")
        if room_number <= 0:
            raise ValueError("Room number must be positive")


        self.room_number = room_number
        self.room_type = room_type
        self.price_per_night = price_per_night
        self.max_guests = max_guests
        self.is_available = is_available

    def book_room(self) -> None:
        self.is_available = False

    def release_room(self) -> None:
        self.is_available = True

    def calculate_price(self, nights: int) -> float:
        return self.price_per_night * nights

    def __str__(self) -> str:
        return  f"Room N: {self.room_number}\n" + \
                f"Room Type: {self.room_type}\n" + \
                f"Price per night: ${self.price_per_night}\n" + \
                f"Max guests: {self.max_guests}\n" + \
                f"Available: {self.is_available}"


