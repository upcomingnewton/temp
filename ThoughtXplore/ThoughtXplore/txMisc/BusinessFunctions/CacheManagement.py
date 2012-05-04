from django.core.cache import cache
import ThoughtXplore.CONFIG as CONFIG
from ThoughtXplore.txMenu.BusinessFunctions.GroupMenuFunctions import GroupMenuFunctions
from ThoughtXplore.CONFIG import LOGGER_USER, CACHE_TIME_FOR_GROUP_MENU
import logging

LoggerUser = logging.getLogger(LOGGER_USER)