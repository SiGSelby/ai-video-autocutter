# AI-Driven Audio Auto-Cutter ✂️

A high-performance Python script designed to eliminate hours of manual rough-cutting. It transcribes input audio using the **OpenAI Whisper** model, calculates precise millisecond timestamps of silence, and uses **MoviePy** to cleanly stitch together only the segments containing active speech.

### Key Capabilities
- Sub-second audio silence threshold filtering.
- Automated multi-clip seamless stitching.
- Hardware-accelerated transcription using PyTorch.
## 📊 Live Pipeline Example

### 📥 Input Data (`raw_footage.mp4`)
- **Total Duration:** 00:25 seconds
- **Audio Track:** "Hey guys... [5-second pause] ...today we are... [3-second cough] ...building an AI tool."

### ⚙️ Whisper AI Timestamp Alignment
- `[00:00 - 00:02]` -> "Hey guys" (Confidence: 98%)
- `[00:02 - 00:07]` -> [SILENCE DETECTED - DROPPED]
- `[00:07 - 00:09]` -> "today we are" (Confidence: 96%)
- `[00:09 - 00:12]` -> [AUDIO ANOMALY/COUGH - DROPPED]
- `[00:12 - 00:15]` -> "building an AI tool" (Confidence: 99%)

### 📤 Output Data (`ai_edited_output.mp4`)
- **Total Duration:** 00:07 seconds
- **Result:** A perfectly trimmed, rapid jump-cut sequence with all dead air automatically purged.
