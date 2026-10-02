from courses.course import Course
from courses.premium_course import PremiumCourse

from exceptions.custom_exceptions import (
    InvalidPriceError,
    InvalidDurationError,
    InvalidDiscountError
)

from utils.logger_config import logger


def main():

    try:

        print("===== ONLINE LEARNING PLATFORM =====")

        # Regular courses
        python_course = Course(
            "Python Fundamentals",
            "Amrutha Varshini Alva",
            20,
            3000
        )

        sql_course = Course(
            "SQL for Beginners",
            "Rahul",
            15,
            2500
        )

        # Premium courses
        ai_course = PremiumCourse(
            "Generative AI Masterclass",
            "Ananya",
            30,
            10000,
            "Yes",
            10
        )

        cloud_course = PremiumCourse(
            "AWS Cloud Architecture",
            "Vikram",
            40,
            12000,
            "Yes",
            15
        )

        # Display course details
        python_course.show_course_details()

        sql_course.show_course_details()

        ai_course.show_course_details()

        cloud_course.show_course_details()

        # Discount calculation
        print("\n--- Discount Example ---")

        discounted_price = ai_course.calculate_discount(20)

        print(
            "Price after 20% discount: ₹",
            discounted_price
        )

        # Course count
        print(
            "\nTotal courses created:",
            Course.get_course_count()
        )

    except InvalidPriceError as error:

        print("Price Error:", error)
        logger.error(error)

    except InvalidDurationError as error:

        print("Duration Error:", error)
        logger.error(error)

    except InvalidDiscountError as error:

        print("Discount Error:", error)
        logger.error(error)

    except Exception as error:

        print("Unexpected error:", error)

        logger.exception(
            "Unexpected application error"
        )


if __name__ == "__main__":
    main()