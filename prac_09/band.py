class Band:
    """Band class that aggregates multiple Musician objects."""

    def __init__(self, name=""):
        """Construct a Band with a name and an empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return a readable string showing the band and its musicians."""
        musicians_list = []
        for musician in self.musicians:
            musicians_list.append(str(musician))
        musicians_text = ", ".join(musicians_list)
        return f"{self.name} ({musicians_text})"

    def play(self):
        """Return text showing each musician playing."""
        results = []
        for musician in self.musicians:
            results.append(musician.play())
        return "\n".join(results)