from datetime import datetime
import math


class PointsCalculator:

    # Rule 1: One point for every alphanumeric character in the retailer name.
    @staticmethod
    def points_for_retailer_name(receipt):
        return sum(c.isalnum() for c in receipt["retailer"])

    # Rule 2: 50 points if the total is a round dollar amount with no cents.
    @staticmethod
    def points_for_round_dollar_amount(receipt):
        total = float(receipt["total"])
        return 50 if total.is_integer() else 0

    # Rule 3: 25 points if the total is a multiple of 0.25.
    @staticmethod
    def points_for_multiple_of_0_25(receipt):
        total = float(receipt["total"])
        return 25 if total % 0.25 == 0 else 0

    # Rule 4: 5 points for every two items on the receipt.
    @staticmethod
    def points_for_item_pairs(receipt):
        return (len(receipt["items"]) // 2) * 5
    
    # Rule 5: If the trimmed length of the item description is a multiple of 3, multiply the price by 0.2 and round up to the nearest integer. The result is the number of points earned.
    @staticmethod
    def points_for_item_description(receipt):
        points = 0
        for item in receipt["items"]:
            trimmed_length = len(item["shortDescription"].strip())
            if trimmed_length % 3 == 0:
                points += math.ceil(float(item["price"]) * 0.2)
        return points

    # Rule 6: 6 points if the day in the purchase date is odd.
    @staticmethod
    def points_for_odd_purchase_day(receipt):
        purchase_date = datetime.strptime(receipt["purchaseDate"], "%Y-%m-%d")
        return 6 if purchase_date.day % 2 != 0 else 0

    # Rule 7: 10 points if the time of purchase is after 2:00pm and before 4:00pm.
    @staticmethod
    def points_for_purchase_time(receipt):
        purchase_time = datetime.strptime(receipt["purchaseTime"], "%H:%M")
        return 10 if 14 <= purchase_time.hour < 16 else 0
    
    # Return the sum of all calculated points from each rule.
    @classmethod
    def calculate_points(cls, receipt):
        points = 0
        points += cls.points_for_retailer_name(receipt)
        points += cls.points_for_round_dollar_amount(receipt)
        points += cls.points_for_multiple_of_0_25(receipt)
        points += cls.points_for_item_pairs(receipt)
        points += cls.points_for_item_description(receipt)
        points += cls.points_for_odd_purchase_day(receipt)
        points += cls.points_for_purchase_time(receipt)
        return points