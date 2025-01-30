import openai
import sys

def transcribe_and_summarize(audio_path):
    print("Transcribing...")
    with open(audio_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    
    text = transcript['text']
    print(f"\nTranscript: {text}\n")
    
    print("Summarizing action items...")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Extract action items from this transcript as a bulleted list."},
            {"role": "user", "content": text}
        ]
    )
    print(f"\nAction Items:\n{response.choices[0].message.content}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python transcribe.py <audio.mp3>")
    else:
        transcribe_and_summarize(sys.argv[1])
