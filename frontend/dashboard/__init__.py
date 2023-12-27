from enum import Enum

from .why import WhyTab
from .editor import EditorTab
from .tracker import TrackerTab
from .analysis import AnalysisTab
from .profile import ProfileTab
from .feedback import FeedbackTab

class DashboardTabs(Enum):
    why = WhyTab
    editor = EditorTab
    tracker = TrackerTab
    analysis = AnalysisTab
    profile = ProfileTab
    feedback = FeedbackTab