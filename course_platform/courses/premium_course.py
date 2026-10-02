from courses.course import Course
from utils.logger_config import logger


class PremiumCourse(Course):

    def __init__(
        self,
        course_name,
        instructor,
        duration,
        price,
        mentor_support,
        live_sessions
    ):

        # Call parent constructor
        super().__init__(
            course_name,
            instructor,
            duration,
            price
        )

        self.mentor_support = mentor_support
        self.live_sessions = live_sessions

        logger.info(
            f"Premium course created: {self.course_name}"
        )

    def show_course_details(self):

        # Call parent method
        super().show_course_details()

        print("Course Type: Premium")
        print("Mentor Support:", self.mentor_support)
        print("Live Sessions:", self.live_sessions)