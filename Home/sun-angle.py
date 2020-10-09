# https://py.checkio.org/en/mission/sun-angle/

'''
Every true traveler must know how to do 3 things: fix the fire, find the water and extract useful information from the nature around him.
Programming won't help you with the fire and water, but when it comes to the information extraction - it might be just the thing you need.

Your task is to find the angle of the sun above the horizon knowing the time of the day.
Input data: the sun rises in the East at 6:00 AM, which corresponds to the angle of 0 degrees.
At 12:00 PM the sun reaches its zenith, which means that the angle equals 90 degrees.
6:00 PM is the time of the sunset so the angle is 180 degrees. If the input will be the time of the night (before 6:00 AM or after 6:00 PM),
your function should return - "I don't see the sun!".
'''

def sun_angle(time):
    hour, min = map(int, time.split(":"))
    # 12h = 180 degree, 1h = 15 degree, 1min = 0.25 degree
    # 90 = 6 * 15 drgee (from 00:00 to 06:00) 
    angle = hour * 15 + min * 0.25 - 90
    return angle if 0 <= angle <= 180 else "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
