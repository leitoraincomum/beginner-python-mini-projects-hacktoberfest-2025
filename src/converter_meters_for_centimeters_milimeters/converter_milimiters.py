def converter():
    print('Converter from meters to centimeters and millimeters')
    meter = float(input('Enter the value in meters for conversion: '))
    decimeter = meter * 10
    centimeter = meter * 100
    millimeter = meter * 1000
    decameter = meter / 10
    hectometer = meter / 100
    kilometer = meter / 1000
    print('The value of {} meters is equivalent to {} decimeters, {} centimeters, and {} millimeters.'
      '\nIt is also equivalent to {} decameters, {} hectometers, {} kilometers.'
      .format(meter, decimeter, centimeter, millimeter, decameter, hectometer, kilometer))
    print('>>> In another way \n{} meters is equivalent to {} centimeters or {} millimeters.'
      '\nIt is also equivalent to {} decameters, {} hectometers, {} kilometers.'
      .format(meter, (meter * 100), (meter * 1000), (meter / 10), (meter / 100), (meter / 1000)))