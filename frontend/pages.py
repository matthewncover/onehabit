from enum import Enum

from frontend.welcome import WelcomePage
from frontend.dashboard.dashboard import UserDashboardPage

from frontend.accounts.disclaimer import DisclaimerPage
from frontend.introduction import (
    PhilosophyPage, CoachIntroductionPage,
    HabitIntroductionPage, HabitIdentificationPage,
    HabitDefinitionPage, HabitWhyPage,
    HabitSummaryPage
)

class Pages(Enum):
    WelcomePage = WelcomePage
    UserDashboardPage = UserDashboardPage
    DisclaimerPage = DisclaimerPage

    PhilosophyPage = PhilosophyPage
    CoachIntroductionPage = CoachIntroductionPage
    HabitIntroductionPage = HabitIntroductionPage
    HabitIdentificationPage = HabitIdentificationPage
    HabitDefinitionPage = HabitDefinitionPage
    HabitWhyPage = HabitWhyPage
    HabitSummaryPage = HabitSummaryPage