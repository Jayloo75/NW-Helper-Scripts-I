class FishingWindow:

    region_middle_third = False
    fish_caught_level_bubble_region = False

    # Methods
    def __init__(self, win_class):
        self.windows_obj = win_class
        self.set_region_middle_third(win_class)
        self.set_fish_caught_level_bubble_region()

    def get_region_full_window(self):
        return self.windows_obj.region_full_window

    # define the middle 1/3 slice of the screen to keep under watch
    def set_region_middle_third(self, win_class):
        print("win_class.width", win_class.width)
        x1_third = int(win_class.width * 0.33 + win_class.left)
        x2_third = int(win_class.left + win_class.width * 0.66)
        y1_third = int(win_class.height * 0.15 + win_class.top)
        y2_third = int(win_class.top + win_class.height * 0.85)
        self.region_middle_third = (x1_third, y1_third, x2_third, y2_third)
        print("Debug: region_middle_third ", self.region_middle_third)

    def get_region_middle_third(self):
        return self.region_middle_third

    # Define region to look for fish caught bubble
    def set_fish_caught_level_bubble_region(self):
        xxx1 = 1064 + self.windows_obj.left
        yyy1 = 698 + self.windows_obj.top
        self.fish_caught_level_bubble_region = (xxx1, yyy1, 50, 50)

    def get_fish_caught_level_bubble_region(self):
        return self.fish_caught_level_bubble_region
