import os
import re

dir = os.getcwd()
last_elements = []
last_artist_index = None
last_track_index = None

def all_items_same_except_num(dict_x, dict_y, num):
    unfits = 0
    #print(f"\nComparing \n{dict_x} \nwith \n{dict_y}\n")

    if dict_x.__len__() != dict_y.__len__() or dict_x.__len__() <= num or dict_y.__len__() <= num:
        #print("False")
        return False
    for item in dict_x.items():
        if item not in dict_y.items():
            unfits += 1
    #print(f"Unfits: {unfits}")
    #print(unfits <= num)
    return unfits <= num

for file in os.listdir(dir):
    if file.endswith(".wav") or file.endswith(".mp3"):
        print("\n-----------------------\n")
        print(f"Current: {file}")

        # Save file ending for later
        file_ending = re.search(r"(\.[a-z|0-9]+)\Z", file).group(0)

        # Get elements (artist, title, album, etc.) from file name
        # and remove file ending
        # and save them with their index in a dictionary
        #elements = re.split(r"(\s*-\s*)", file)
        elements = re.split(r" - ", file)
        elements[-1] = elements[-1].replace(file_ending, "")
        elements = dict(zip(range(len(elements)), elements))
        print(f"\nElements: \n{elements}")

        artist_index = last_artist_index
        track_index = last_track_index

        if not all_items_same_except_num(elements, last_elements, 2):
            # Assign element indices to Artist and Track
            print(f"Elements: {elements.__len__()}")
            if elements.__len__() == 1:     # In case there is only one element
                artist = input("Artist: ")  # we assume it to be the track
                elements[1] = artist
                artist_index = 1
                track_index = 0  
            elif elements.__len__() == 2: # In case there are two elements
                artist_index = 0          # we assume the first to be the artist
                track_index = 1           # and the second to be the track
            else:
                artist_index = int(input("Artist index: "))
                track_index = int(input("Track index: "))
        
        new_name = f"{elements[artist_index]} - {elements[track_index]}{file_ending}"
        print(f"Changed: \n{file} \nto: \n{new_name}")
        os.rename(file, new_name)

        # Save last elements for next iteration
        last_elements = elements
        last_artist_index = artist_index
        last_track_index = track_index