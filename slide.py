
class Slide():
    def __init__(self, v_tags_1=None, v_tags_2=None, h_tags=None, v_image_1=None, v_image_2=None, h_image=None, prev_score=None, next_score=None):
        self.v_image_1 = v_image_1
        self.v_image_2 = v_image_2
        self.h_image = h_image
        self.v_tags_1 = v_tags_1
        self.v_tags_2 = v_tags_2
        self.h_tags = h_tags
        self.all_tags = []
        if v_tags_1 is not None:
            self.all_tags.extend(v_tags_1)
        if v_tags_2 is not None:
            self.all_tags.extend(v_tags_2)
        if h_tags is not None:
            self.all_tags.extend(h_tags)
        self.all_tags = list(set(self.all_tags))
        self.prev_score = prev_score
        self.next_score = next_score

    def __str__(self):
        if self.h_image:
            return 'Horizontal image, id = {0}, tags = {1}'.format(self.h_image, self.h_tags)
        else:
            return 'Vertical image, id = {0}, tags = {1}'.format(self.v_image_1, self.v_tags_1)

    def __repr__(self):
        if self.h_image:
            return 'Horizontal image, id = {0}, tags = {1}'.format(self.h_image, self.h_tags)
        else:
            return 'Vertical image, id = {0}, tags = {1}'.format(self.v_image_1, self.v_tags_1)
