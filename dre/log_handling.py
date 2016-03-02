from __future__ import division

import json
import math


def reduce_logs(logs):
    """
    Takes a list of log dictionaries and converts
    them into a minial form

    """

    # get a list of unique dictionaries (not including the forecast value)
    conditions = [log["condition"] for log in logs]
    unique_conditions = {json.dumps(log): log for log in logs}.values()
    
    possibilities = []
    for condition in unique_conditions:
        these_forecasts = []
        for log in logs:
            if log["condition"] == condition:
                these_forecasts.append(log["forecast"])
        reduced_log = {"condition": condition, "forecasts": these_forecasts}

        possibilities.append(reduced_log)
    # import pdb; pdb.set_trace()

    return possibilities