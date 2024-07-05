from abc import abstractmethod, ABC


"""
consider an app for digitalizing music sheets.
It receives a photo of the music sheet and outputs a
pdf, MusicXML or audio file with the music sheet digitalized.
"""


# Abstract class
class MusicSheet(ABC):
    def generate(self) -> None:
        self.start_process()
        self.load_image()
        self.detect_notes()
        self.generate_output()
        self.save_output()
        self.preview_output()
        self.finish()

    # Optional methods

    def load_image(self) -> None:
        print("MusicSheet: Loaded image")

    def detect_notes(self) -> None:
        print("MusicSheet: Detected notes")

    def save_output(self) -> None:
        print("MusicSheet: Saved output")

    # Abstract methods

    @abstractmethod
    def start_process(self) -> None:
        pass

    @abstractmethod
    def generate_output(self) -> None:
        pass

    @abstractmethod
    def preview_output(self) -> None:
        pass

    # Hook methods

    def finish(self) -> None:
        pass


# Concrete classes
class PDFMusicSheet(MusicSheet):
    def start_process(self) -> None:
        print("PDFMusicSheet: started generating PDF")

    def generate_output(self) -> None:
        print("PDFMusicSheet: Generated PDF")

    def preview_output(self) -> None:
        print("PDFMusicSheet: Opened PDF viwer")
        print("PDFMusicSheet: Previewed PDF")

    def finish(self) -> None:
        print("PDFMusicSheet: Close PDF viewer")


# Concrete classes
class MusicXMLMusicSheet(MusicSheet):
    def start_process(self) -> None:
        print("MusicXMLMusicSheet: started generating MusicXML file")

    def generate_output(self) -> None:
        print("MusicXMLMusicSheet: Generated MusicXML")

    def preview_output(self) -> None:
        print(
            "MusicXMLMusicSheet: Preview requires plugin musicxml-viewer."
            "Install plugin musicxml-viewer to preview MusicXML files."
        )


# Concrete classes
class AudioMusicSheet(MusicSheet):
    def start_process(self) -> None:
        print("AudioMusicSheet: started generating audio file")

    def generate_output(self) -> None:
        print("AudioMusicSheet: Generated audio")

    def preview_output(self) -> None:
        print("AudioMusicSheet: Requested permission to play audio on device")
        print("AudioMusicSheet: Opened device's default audio player")
        print("AudioMusicSheet: Played audio")

    def finish(self) -> None:
        print("AudioMusicSheet: Close device's default audio player")


if __name__ == "__main__":
    pdf_sheet = PDFMusicSheet()
    pdf_sheet.generate()

    print("\n")

    musicxml_sheet = MusicXMLMusicSheet()
    musicxml_sheet.generate()

    print("\n")

    audio_sheet = AudioMusicSheet()
    audio_sheet.generate()
