from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMiles(App):
    """A simple Kivy app to convert miles to kilometres."""
    output_km = StringProperty("0.0")

    def build(self):
        """ Build and return the app's root widget."""
        self.title = "Convert Miles"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_convert(self):
        """Convert the miles value from the input box into kilometres."""
        miles = self.get_valid_miles()
        km = miles * MILES_TO_KM
        self.output_km = f"{km:.5f}"

    def handle_increment(self, change):
        """Increase or decrease the miles value by the given amount."""
        miles = self.get_valid_miles()
        miles += change
        self.root.ids.user_input.text = str(miles)

    def get_valid_miles(self):
        """Safely get a valid float value from the TextInput."""
        text = self.root.ids.user_input.text
        try:
            return float(text)
        except (ValueError, TypeError):
            return 0.0


ConvertMiles().run()
