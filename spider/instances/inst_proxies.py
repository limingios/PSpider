# _*_ coding: utf-8 _*_

"""
inst_proxies.py by xianhu
"""

import time
import logging
from ..utilities import extract_error_info


class Proxieser(object):
    """
    class of Proxieser, must include function working()
    """

    def __init__(self, sleep_time=10):
        """
        constructor
        :param sleep_time: default 10, sleeping time after a fetching for proxies
        """
        self._sleep_time = sleep_time
        return

    def working(self) -> (int, list):
        """
        working function, must "try, except" and don't change the parameters and return
        :return (proxies_result, proxies_list): proxies_result can be -1(get failed), 1(get success)
        :return (proxies_result, proxies_list): proxies_list is a proxies list which getting from web or database
        """
        logging.debug("%s start", self.__class__.__name__)

        time.sleep(self._sleep_time)
        try:
            proxies_result, proxies_list = self.proxies_get()
        except Exception:
            proxies_result, proxies_list = -1, []
            logging.error("%s error: %s", self.__class__.__name__, extract_error_info())

        logging.debug("%s end: proxies_result=%s, len(proxies_list)=%s", self.__class__.__name__, proxies_result, len(proxies_list))
        return proxies_result, proxies_list

    def proxies_get(self) -> (int, list):
        """
        get proxies from web or database, you can rewrite this function, parameters and return refer to self.working()
        """
        raise NotImplementedError
