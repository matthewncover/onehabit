from enum import Enum

from .why import WhyTab
from .tracker import TrackerTab
from .editor import EditorTab
from .analysis import AnalysisTab
from .coach import CoachTab
from .settings import SettingsTab

# from .profile import ProfileTab
# from .feedback import FeedbackTab

class DashboardTabs(Enum):
    why = WhyTab
    tracker = TrackerTab
    editor = EditorTab
    analysis = AnalysisTab
    coach = CoachTab
    settings = SettingsTab
    # profile = ProfileTab
    # feedback = FeedbackTab