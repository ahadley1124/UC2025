def heading_time(start_heading, end_heading, duration):
	if start_heading - end_heading < 0:
		heading_range = end_heading - start_heading
		range_per_sec = heading_range / duration
		return range_per_sec
	else:
		heading_range = start_heading - end_heading
		range_per_sec = heading_range / duration
		return range_per_sec

def EL_time(maz_el, duration):
	return max_el / duration
