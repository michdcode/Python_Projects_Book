import plistlib
import numpy as np
import matplotlib.pyplot as plt

song_data = "itunes_playlst.xml"


def find_duplicates(song_data):
    """Reads in song file and searches for duplicates."""

    #obtain song name & length from ITunes dump & save song & count to dictionary
    playlst = plistlib.readPlist(song_data)
    tracks = playlst['Tracks']
    track_names = {}
    for track_id, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']
            if name in track_names:
                if duration//1000 == track_names[name][0]//1000:
                    count = track_names[name][1]
                    track_names[name] = (duration, count+1)
            else:
                track_names[name] = (duration, 1)
        except:
            pass
    return track_names


def extract_duplicates(track_names):
    """Extracts duplicate songs."""

    #use song dictionary to find duplicates and save any duplicates to text file
    duplicates = []
    for track, num in track_names.items():
        if num[1] > 1:
            duplicates.append((num[1], track))
        if len(duplicates) > 0:
            print "Found %d duplicates; saved to duplicates.txt" % len(duplicates)
        else:
            print "No duplicates found."
    f = open('duplicates.txt', 'w')
    for entry in duplicates:
        f.write("[%d] %s\n" % (entry[0], entry[1]))
    f.close()


def plot_ratings_durations(song_data):
    """Reads in song file and plots ratings & duration."""

    #obtain song ratings and duration from iTunes library dump
    playlst = plistlib.readPlist(song_data)
    tracks = playlst['Tracks']
    ratings = []
    durations = []
    for track_id, track in tracks.items():
        try:
            ratings.append(track['Album Rating'])
            durations.append(track['Total Time'])
        except:
            pass
    if ratings == [] or durations == []:
        print("No valid Album Rating/Total Time data in %s." % song_data)
        return

    # create numpy array for duration (32 bit integer) & convert MS to seconds
    x = np.array(durations, np.int32)
    x = x/60000.0
    # create numpy arrary for ratings (32 bit integer)
    y = np.array(ratings, np.int32)
    #draw two plots in same figure, with 2 rows & 1 column
    plt.subplot(2, 1, 1)
    # create plot using circles
    plt.plot(x, y, 'o')
    # inflate range for visual appeal
    plt.axis([0, 1.05*np.max(x), -1, 110])
    # label axis
    plt.xlabel('Track duration')
    plt.ylabel('Track rating')
    # plot histogram
    plt.subplot(2, 1, 2)
    plt.hist(x, bins=20)
    plt.xlabel('Track duration')
    plt.ylabel('Count')
# show plot
    plt.show()
