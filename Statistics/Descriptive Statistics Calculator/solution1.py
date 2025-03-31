# https://www.deep-ml.com/problems/78

# pros:
# - easy to understand

# cons:
# - it's a fucking mess without numpy

import numpy as np 

def descriptive_statistics(data):
	# Your code here
	
    # mean
    mean = sum(data) / len(data)
    
    # median
    mid = len(data) // 2
    if len(data) % 2 == 0:
        median = (data[mid] + data[mid - 1]) / 2
    else:
        median = data[mid]

    # mode
    count = {}
    for num in data:
        count[num] = count.get(num, 0) + 1

    max_freq = max(count.values())

    mode = [key for key, val in count.items() if val == max_freq][0]    
    
    # variance
    variance = sum((x - mean) ** 2 for x in data) / len(data)

    # standard deviation
    std_dev = variance ** 0.5

    # percentile
    percentiles = []
    for p in [25, 50, 75]:
        index = (p / 100) * (len(data) - 1)
        lower = int(index)
        upper = lower + 1
        
        weight = index - lower

        if upper < len(data):
            percentile_value = data[lower] + weight * (data[upper] - data[lower])
        else:
            percentile_value = data[lower] 

        percentiles.append(percentile_value)

    # iqr
    iqr = percentiles[2] - percentiles[0]
    

    stats_dict = {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": np.round(variance,4),
        "standard_deviation": np.round(std_dev,4),
        "25th_percentile": percentiles[0],
        "50th_percentile": percentiles[1],
        "75th_percentile": percentiles[2],
        "interquartile_range": iqr
    }

	return stats_dict