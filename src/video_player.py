"""A video player class."""

from .video_library import VideoLibrary
from .video_playlist import Playlist
import random


class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self._current_video = None
        self._video_paused = True
        self._playlists = []

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        output = ""
        all_videos = sorted(self._video_library.get_all_videos(), key=lambda video: video.title)
        for video in all_videos:
            video_tags = ""
            for tag in video.tags:
                video_tags += tag + " "
            output += "\n  " + video.title + " (" + video.video_id + ") [" + video_tags.rstrip() + "]"

        print(f"Here's a list of all available videos: {output}")

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        output = ""
        get_video = self._video_library.get_video(video_id)
        if get_video == None:
            output = "Cannot play video: Video does not exist"
        else:
            # If there is no video playing currently, play.
            self._video_paused = False
            if self._current_video == None:
                self._current_video = get_video
                output = (f"Playing video: {self._current_video.title}")
            else:
                output = (f"Stopping video: {self._current_video.title}")
                self._current_video = get_video
                output += "\n" + (f"Playing video: {self._current_video.title}")

        print(output)

    def stop_video(self):
        """Stops the current video."""
        output = ""
        if self._current_video == None:
            output = "Cannot stop video: No video is currently playing"
        else:
            output = (f"Stopping video: {self._current_video.title}")
            self._current_video = None

        print(output)

    def play_random_video(self):
        """Plays a random video from the video library."""
        videos = self._video_library.get_all_videos()
        self.play_video(videos[random.randint(0, len(videos)-1)].video_id)

    def pause_video(self):
        """Pauses the current video."""
        output = ""
        if self._current_video == None:
            output = "Cannot pause video: No video is currently playing"
        else:
            if self._video_paused == False:
                self._video_paused = True
                output = (f"Pausing video: {self._current_video.title}")
            else:
                output = (f"Video already paused: {self._current_video.title}")

        print(output)

    def continue_video(self):
        """Resumes playing the current video."""
        output = ""
        if self._current_video == None:
            output = "Cannot continue video: No video is currently playing"
        else:
            if self._video_paused == False:
                output = (f"Cannot continue video: Video is not paused")
            else:
                self._video_paused = False
                output = (f"Continuing video: {self._current_video.title}")

        print(output)

    def show_playing(self):
        """Displays video currently playing."""
        if self._current_video == None:
            output = "No video is currently playing"
        else:
            tags = ""
            for tag in self._current_video.tags:
                tags += tag + " "
            if self._video_paused == False:
                output = (f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{tags.rstrip()}]")
            else:
                output = (f"Currently playing: {self._current_video.title} ({self._current_video.video_id}) [{tags.rstrip()}] - PAUSED")

        print(output)

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        output = ""
        if playlist_name in self._playlists:
            output = "Cannot create playlist: A playlist with the same name already exists"
        else:
            self._playlists.append(Playlist(playlist_name, {}))
            output = (f"Successfully created new playlist: {playlist_name}")     

        print(output)

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        

        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
