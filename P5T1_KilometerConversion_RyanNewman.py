# Pounds to Kilogram Converter
# 13MAR2019
# CTI-110 P5T1_KilometerConverter
# Ryan Newman
#
# Get the weight in kilograms from the user and convert it using the
#  modular code blocks

CONVERSION_FACTOR  = 0.6214

def main ():
    # Get the distance in kilometers
    kilometers = float(input('Enter a distance in kilometers: '))

    # Display the distance converted to miles
    show_miles(kilometers)

def show_miles(km) :
    # calculate miles
    miles = km * CONVERSION_FACTOR

    # Diplay the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function
main()
