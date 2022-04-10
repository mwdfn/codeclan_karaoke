class Room:
    def __init__(self, input_room_number):
        self.room_number = input_room_number
        self.guest_list = []
        self.song_list = []

    def check_guest_list_len(self):
        return len(self.guest_list)

    def check_song_list_len(self):
        return len(self.song_list)

    def add_guest_to_list(self, guest_name):
        self.guest_list.append(guest_name)

    def add_song_to_list(self, song_title):
        self.song_list.append(song_title)
        print(self.song_list)



