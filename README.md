# AI-Driven Audio Auto-Cutter ✂️

A high-performance Python script designed to eliminate hours of manual rough-cutting. It transcribes input audio using the **OpenAI Whisper** model, calculates precise millisecond timestamps of silence, and uses **MoviePy** to cleanly stitch together only the segments containing active speech.

### Key Capabilities
- Sub-second audio silence threshold filtering.
- Automated multi-clip seamless stitching.
- Hardware-accelerated transcription using PyTorch.
