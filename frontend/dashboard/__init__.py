from enum import Enum

from .why import WhyTab
from .tracker import TrackerTab
from .editor import EditorTab
from .analysis import AnalysisTab
from .profile import ProfileTab
from .feedback import FeedbackTab

class DashboardTabs(Enum):
    why = WhyTab
    tracker = TrackerTab
    editor = EditorTab
    analysis = AnalysisTab
    profile = ProfileTab
    feedback = FeedbackTab