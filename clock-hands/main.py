def calc_angle(h, m):
    hour_step_angle = 30

    # reference for measuring tha angles is the "12" hour
    minute_angle = m * 6
    hour_angle = (h % 12) * hour_step_angle + (m / 60) * hour_step_angle

    angle = abs(minute_angle - hour_angle)
    return angle if angle <= 180 else 360 - angle


print(calc_angle(3, 30))
# 75
print(calc_angle(12, 30))
# 165
print(calc_angle(2, 20))
# 50
print(calc_angle(6, 30))
# 15
print(calc_angle(10, 16))
# 148
