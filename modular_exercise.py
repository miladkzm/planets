class ConvertTemperature(object):
    celsius: int
    kelvin: int
    fahrenheit: int
    temperature: int
    unit: str

    def __init__(
            self,
    ):
        self.abs_zero = {
            "C": -273.15,
            "F": -459.67,
            "K": 0
        }

    def convert_fahrenheit(
            self,
    ):
        # Convert Fahrenheit to Celsius
        celsius = (self.temperature - 32) * (5 / 9)
        if celsius < self.abs_zero['C']:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = celsius + abs(self.abs_zero['C'])
            if kelvin < self.abs_zero["K"]:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                fahrenheit = (celsius * (9 / 5)) + 32
                if fahrenheit < self.abs_zero["F"]:
                    # Invalid temperature, below absolute zero
                    return "Invalid temperature"
                else:
                    return {"Celsius": celsius, "Kelvin": kelvin}

    def convert_celsius(
            self,
    ):
        # Convert Celsius to Fahrenheit
        fahrenheit = (self.temperature * (9 / 5)) + 32
        if fahrenheit < self.abs_zero["F"]:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Kelvin
            kelvin = self.temperature + abs(self.abs_zero['C'])
            if kelvin < self.abs_zero["K"]:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return {"Fahrenheit": fahrenheit, "Kelvin": kelvin}

    def convert_kelvin(
            self
    ):
        # Convert Kelvin to Celsius
        celsius = self.temperature - self.abs_zero["C"]
        if celsius < self.abs_zero["C"]:
            # Invalid temperature, below absolute zero
            return "Invalid temperature"
        else:
            # Convert Celsius to Fahrenheit
            fahrenheit = (celsius * (9 / 5)) + 32
            if fahrenheit < self.abs_zero["F"]:
                # Invalid temperature, below absolute zero
                return "Invalid temperature"
            else:
                return {"Celsius": celsius, "Fahrenheit": fahrenheit}

    def convert_temperature(
            self,
            input_temperature: int,
            unit: str
    ):
        self.temperature = input_temperature
        self.unit = unit
        if unit not in self.abs_zero.keys():
            return "Invalid unit"
        else:
            if self.unit == "F":
                return self.convert_fahrenheit()
            elif self.unit == "C":
                return self.convert_celsius()
            elif self.unit == "K":
                return self.convert_kelvin()


# to run
if __name__ == "__main__":
    temperature = ConvertTemperature()

    print(temperature.convert_temperature(0, "C"))
