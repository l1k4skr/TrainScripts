import math 

def sub_list_int(list__):
    """Converts a list of list strings to a list of integers

    Args:
        list__ (list): 2D list of strings
        
    return: 2D list of integers
    """
    for  index, i in enumerate(list__):
        for index_, g in enumerate(i):
            list__[index][index_] = int(g)
    return list__

def _total_time(_2d_list):
    """Returns a list of the total time of each runner

    Args:
        _2d_list (2d List): 2d list of integers

    Returns:
        list: list of integers
    """
    times = []
    
    for i in _2d_list:
        total = 0
        for index__, e in enumerate(i):
            if index__ == 0:
                total += e*60*60
            elif index__ == 1:
                total += e*60
            else:
                total += e
        times.append(total)
    return times

def time2str(time):
    """Converts time in seconds to string

    Args:
        time (int): time in seconds
        
    return: time in string format
    """
    hours =  int(math.floor((time//3600)))
    
    if hours < 10:
        hours = "0" + str(hours)
    minutes = int(math.floor((time%3600)//60 ))#?
    
    if minutes < 10:
        minutes = "0" + str(minutes)
        
    seconds = int(math.floor((time%3600)%60))
    if seconds < 10:
        seconds = "0" + str(seconds)
    return f"{hours}|{minutes}|{seconds}"

def get_range(_2d_list):
    """Returns the range of a 2D list

    Args:
        _2d_list (list): 2D list of integers
    return: range of the list
    """
    total_times = _total_time(_2d_list)
    range_ = max(total_times) - min(total_times)
    
    range_ = time2str(range_)
    
    return range_

def get_mean(_2d_list):
    """Returns the mean of a 2D list

    Args:
        _2d_list (list): 2D list of integers
    return: mean of the list
    """
    total_times = _total_time(_2d_list)
    mean = sum(total_times)/len(total_times)
    mean = time2str(mean)
    return mean

def get_median(_2d_list):
    """gets the median of a 2D list

    Args:
        _2d_list (Matrix): data

    Returns:
        str: hh|mm|ss format
    """
    if len(_2d_list)%2 == 0:
        total = _total_time(_2d_list)
        total.sort()
        median = (total[len(total)//2] + total[len(total)//2 - 1])/2
    else:
        total = _total_time(_2d_list)
        total.sort()
        median = total[len(_2d_list)//2]
        
    median = time2str(median)
    return median

def list_separation(_2d_list):
    """Separates a 2D list of strings into a 2D list of integers

    Args:
        _2d_list (Mratrix): 2d list

    Returns:
        _list_: integer 2d list
    """
    list_ =_2d_list.split(', ')
    list_ = [i.split("|") for i in list_]
    list_ = sub_list_int(list_)
    return list_ 

def stat(strg):
    if strg == "":
        return ""
    lst = list_separation(strg)
    
    range2 = get_range(lst)
    
    mean = get_mean(lst)
    
    median = get_median(lst)
    return f"Range: {range2} Average: {mean} Median: {median}"

print(stat("11|15|59, 10|16|16, 12|17|20, 9|22|34, 13|19|34, 11|15|17, 11|22|00, 10|26|37, 12|17|48, 9|16|30, 12|20|14, 11|25|11"))
print(stat("1|15|59, 1|16|16, 1|17|20, 1|22|34, 1|19|34, 1|15|17, 1|22|00, 1|26|37, 1|17|48, 1|16|30, 1|20|14, 1|25|11"))

