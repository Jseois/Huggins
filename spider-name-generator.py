import random

class SpiderNameGenerator:
    def __init__(self):
        self.spider_terms = [
            "Web", "Silk", "Widow", "Spinner", "Weaver", "Arachne", "Orb", "Tarantula", 
            "Hunter", "Prowler", "Stalker", "Crawler", "Jumper", "Shadow"
        ]
        
        self.atmospheric_terms = [
            "Dusk", "Twilight", "Midnight", "Shade", "Mist", "Gloom", "Dark", "Dawn",
            "Night", "Shadow", "Moon", "Fog", "Ethereal", "Mystic"
        ]
        
        self.descriptors = [
            "Venomous", "Silent", "Deadly", "Ancient", "Cunning", "Swift", "Patient",
            "Lurking", "Waiting", "Hidden", "Secret", "Wise", "Eternal", "Phantom"
        ]
    
    def generate_name(self, format_type="basic"):
        if format_type == "basic":
            return f"{random.choice(self.spider_terms)}{random.choice(self.atmospheric_terms)}"
        elif format_type == "descriptive":
            return f"{random.choice(self.descriptors)} {random.choice(self.spider_terms)}"
        elif format_type == "complex":
            return f"The {random.choice(self.descriptors)} {random.choice(self.spider_terms)} of {random.choice(self.atmospheric_terms)}"
        elif format_type == "title":
            return f"{random.choice(self.spider_terms)}, {random.choice(self.descriptors)} {random.choice(self.atmospheric_terms)}"
    
    def generate_multiple(self, count=5, format_type="basic"):
        return [self.generate_name(format_type) for _ in range(count)]

# Example usage
generator = SpiderNameGenerator()
print("Basic Names:", generator.generate_multiple(3, "basic"))
print("Descriptive Names:", generator.generate_multiple(3, "descriptive"))
print("Complex Names:", generator.generate_multiple(3, "complex"))
print("Title Names:", generator.generate_multiple(3, "title"))
