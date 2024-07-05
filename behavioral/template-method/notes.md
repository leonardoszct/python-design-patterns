# Template Method

> [!IMPORTANT]
> This is my personal notes of [Refactoring Guru's article on Template Method](https://refactoring.guru/design-patterns/template-method). Visit their site for a complete version 🤓

### Notes

- **Intent**: defines the structure of an algorithm in the superclass and gives the subclasses the freedom to override specific steps of the algorithm without changing the said structure.

- **Problem:** consider an app for digitalizing music sheets. It receives a photo of the music sheet and outputs a pdf document with the music sheet digitalized. At the beginning, the app only generated PDF's, but users asked for other output formats, as editable MusicXML and audio files with the sheet being played. To generate the different outputs it takes different approachs, but they all have similar code structure. 
 
- **Solution:** break the algorithm inot a sequence of steps (methods) and define a *template method* to execute this steps in a specific  order. Then, the client provides a subclass which implements/overrides all steps required.  


- **Structure:**
  - **Abstract Class**: declares methods that act as steps of an algorithm and the template method that calls those steps in a specific order.
  - **Concrete classes**: can override/implment steps (but not the template method).

- **Applicability**
  - When clients should extend only particular behaviours of an algorithm and not the whole piece
  - When there's multiple classes with amost identical algorithms with small differences between them.  

### Output

The `template-method/index.py` execution output is:

```cmd
PDFMusicSheet: started generating PDF
MusicSheet: Loaded image
MusicSheet: Detected notes
PDFMusicSheet: Generated PDF
MusicSheet: Saved output
PDFMusicSheet: Opened PDF viwer
PDFMusicSheet: Previewed PDF
PDFMusicSheet: Close PDF viewer


MusicXMLMusicSheet: started generating MusicXML file
MusicSheet: Loaded image
MusicSheet: Detected notes
MusicXMLMusicSheet: Generated MusicXML
MusicSheet: Saved output
MusicXMLMusicSheet: Preview requires plugin musicxml-viewer.Install plugin musicxml-viewer to preview MusicXML files.


AudioMusicSheet: started generating audio file
MusicSheet: Loaded image
MusicSheet: Detected notes
AudioMusicSheet: Generated audio
MusicSheet: Saved output
AudioMusicSheet: Requested permission to play audio on device
AudioMusicSheet: Opened device's default audio player
AudioMusicSheet: Played audio
AudioMusicSheet: Close device's default audio player
```
****