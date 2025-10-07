import pytest

from customer import Customer

class TestCustomerPayForBooking:

    def test_successful_payment_with_sufficient_budget(self):
        customer = Customer("Ana", 500.0)
        initial_budget = customer.budget
        payment_amount = 300.0
        expected_budget = initial_budget - payment_amount
        expected_score = payment_amount * 100

        result = customer.pay_for_booking(payment_amount)

        assert result is True
        assert customer.budget == expected_budget
        assert customer.score == expected_score

    def test_failed_payment_with_insufficient_budget(self):
        customer = Customer("Ana", 100.0)
        initial_budget = customer.budget
        initial_score = customer.score
        payment_amount = 300.0

        result = customer.pay_for_booking(payment_amount)

        assert result is False
        assert customer.budget == initial_budget
        assert customer.score == initial_score

    def test_payment_with_exact_budget(self):
        customer = Customer("Ana", 250.0)
        payment_amount = 250.0
        expected_budget = 0.0
        expected_score = payment_amount * 100

        result = customer.pay_for_booking(payment_amount)

        assert result is True
        assert customer.budget == expected_budget
        assert customer.score == expected_score

    def test_payment_with_zero_amount(self):
        customer = Customer("Ana", 100.0)
        payment_amount = 0

        with pytest.raises(ValueError):
            customer.pay_for_booking(payment_amount)

    def test_payment_negative_amount_raises_concern(self):
        customer = Customer("Ana", 100.0)
        payment_amount = -50.0

        with pytest.raises(ValueError):
            customer.pay_for_booking(payment_amount)
