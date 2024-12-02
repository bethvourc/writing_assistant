# Text Correction Automation Tool

This Python script provides a utility for correcting typos, casing, and punctuation in text while preserving the original formatting (like line breaks). It leverages a text-generation model for accurate text corrections and is designed for seamless usage through keyboard shortcuts.

---

## Features

1. **Text Correction**: 
   - Fix typos, punctuation, and casing while retaining line breaks.
   - Does not add preambles or additional text; only the corrected content is returned.

2. **Hotkey Integration**:
   - **F1 (`<122>`)**: Fixes the current line of text.
   - **F2 (`<120>`)**: Fixes the selected text.

3. **Clipboard Handling**:
   - Automates copying and pasting corrected text using `pyperclip` and keyboard simulation.

4. **Local API Integration**:
   - Communicates with a locally hosted endpoint (`OLLAMA_ENDPOINT`) to perform text corrections using the specified model.

---

## Prerequisites

- Python 3.9 or higher
- Dependencies:
  - `pynput`: For capturing and simulating keyboard inputs.
  - `pyperclip`: For handling clipboard operations.
  - `httpx`: For making HTTP requests to the local API.

- A running instance of the text model server:
  - Endpoint: `http://localhost:11434/api/generate`
  - Configuration: 
    - Model: `mistral:7b-instruct-q4_K_S`
    - Keep Alive: `5m`
    - Stream: `False`

---

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-repo/writing_assistant.git
   cd writing_assistant
   ```

2. Install dependencies:
   ```bash
   pip install pynput pyperclip httpx
   ```

3. Ensure the text model server is running locally.

---

## Usage

1. **Run the script**:
   ```bash
   python main.py
   ```

2. **Hotkeys**:
   - Press **F1** to correct the current line:
     - Automatically selects the current line, sends it for correction, and replaces it with the corrected version.
   - Press **F2** to correct the selected text:
     - Corrects the highlighted portion and pastes the fixed version back.

3. **Stop the script**:
   - Exit the script using standard termination (e.g., `Ctrl+C` in the terminal).

---

## Code Structure

- **`fix_text(text)`**: Sends the input text to the API endpoint and returns the corrected text.
- **`fix_current_line()`**: Automates text selection, correction, and replacement for the current line.
- **`fix_selection()`**: Automates text correction for the currently selected text.
- **Keyboard Listeners**:
  - `on_f1`: Maps to the F1 key for fixing the current line.
  - `on_f2`: Maps to the F2 key for fixing the selected text.

---

## Configuration

Update the following variables as needed:
- **`OLLAMA_ENDPOINT`**: The API endpoint URL.
- **`OLLAMA_CONFIG`**: Configuration for the text model (e.g., model name, keep-alive duration).

---

## Limitations

- Requires a locally running model server.
- Currently supports only macOS-specific keyboard shortcuts (e.g., `Cmd + Shift + Left`).

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Feel free to submit issues or pull requests to enhance the functionality of this tool. Contributions are welcome!