def calculate_parking():
    hours = float(input("กรุณาใส่จำนวนชั่วโมงที่จอดรถ (เช่น 2.35 หมายถึง 2 ชั่วโมง 35 นาที): "))
    rate_per_hour = float(input("กรุณาใส่อัตราค่าจอดรถต่อชั่วโมง (บาท): "))
    hours, minutes = divmod(hours, 1)
    minutes *= 100
    if minutes > 1:
        hours += 1
    price = hours * rate_per_hour
    return price

price = calculate_parking()
print("ค่าจอดรถเท่ากับ", price, "บาท")