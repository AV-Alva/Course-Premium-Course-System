from exceptions.custom_exceptions import (
    InvalidPriceError,
    InvalidDurationError,
    InvalidDiscountError
)

from utils.logger_config import logger


class Course:

    # Class variable
    course_count = 0

    def __init__(self, course_name, instructor, duration, price):

        if price <= 0:
            logger.error(
                f"Invalid price for course {course_name}: {price}"
            )
            raise InvalidPriceError(
                "Course price must be greater than zero."
            )

        if duration <= 0:
            logger.error(
                f"Invalid duration for course {course_name}: {duration}"
            )
            raise InvalidDurationError(
                "Course duration must be greater than zero."
            )

        self.course_name = course_name
        self.instructor = instructor
        self.duration = duration
        self.price = price

        Course.course_count += 1

        logger.info(
            f"Course created: {self.course_name}"
        )

    def show_course_details(self):

        print("\n--- Course Details ---")
        print("Course Name:", self.course_name)
        print("Instructor:", self.instructor)
        print("Duration:", self.duration, "hours")
        print("Price: ₹", self.price)

    def calculate_discount(self, discount_percentage):

        if discount_percentage < 0 or discount_percentage > 100:

            logger.warning(
                f"Invalid discount {discount_percentage}% "
                f"for {self.course_name}"
            )

            raise InvalidDiscountError(
                "Discount must be between 0 and 100."
            )

        discount_amount = (
            self.price * discount_percentage / 100
        )

        final_price = self.price - discount_amount

        logger.info(
            f"{discount_percentage}% discount applied "
            f"to {self.course_name}. "
            f"Final price: {final_price}"
        )

        return final_price

    @classmethod
    def get_course_count(cls):
        return cls.course_count