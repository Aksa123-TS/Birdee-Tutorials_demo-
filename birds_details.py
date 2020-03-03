import birdee


class birds:

    def bird_type(self, *argv):
        print("Type of birds are:\n", "="*15)
        for btype in argv:
            print(btype)

    def bird_details(self, **kwrgs):
        print("examples of Birs:\n----------------------")
        for k, v in kwrgs.items():
            print(k, "=", v)


if __name__ == "__main__":
    birds_ob = birds()
    birds_ob.bird_type("wetland birds", "forest birds", "land birds",
                       "sea birds")
    birds_ob.bird_details(wetland_bird="pond heron", forest_bird="Leaf_"
                          "bird", Land_bird="Tailor bird",
                          Sea_bird="Gull")
