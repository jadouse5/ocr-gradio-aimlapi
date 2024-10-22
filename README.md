# 📄 OCR Reader, 🔍 Analyzer, and 💬 Chat Assistant using 🔎 Zerox, 🧠 GPT-4o, powered by 🚀 AI/ML API

**What I Built**

I built an **OCR Document Reader** that allows users to upload and extract text from various document types such as PDFs, Word, and documents. The app utilizes the [**Zerox**](https://github.com/getomni-ai/zerox) library for Optical Character Recognition (OCR) and integrates the **AI/ML API's GPT-4o** model for advanced text analysis. With features like **support for multiple document formats**, **text analysis**, and an interactive interface built with **Gradio 5.0**, this app simplifies the process of extracting and analyzing text from complex documents.

## Limitations

- **Processing Time**: Enabling the `maintain_format` option can slow down processing due to sequential requests needed to preserve formatting.
- **API Constraints**: The app's capabilities depend on the limitations of the AI/ML API plan, such as request quotas and document size restrictions.
- **System Dependencies**: Requires installation of system packages like `poppler-utils`, which may not be straightforward on all platforms.

## Demo

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vtkgt94kkatc14x22uij.gif)

Here are some key features of the app:

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/qtp52gnbiwpmq96q2yo4.png)


- **Upload Documents**:  
  Users can upload PDFs, Word documents, or images for OCR processing.

- **Extracted Text Display**:  
  The extracted text is displayed within the app, with options to copy or download it.

- **Maintain Formatting**:  
  Optionally preserve the original document's formatting in the extracted text.

### Tech Stack

- **Python**: Core programming language.
- **Gradio 5.0**: For building the user-friendly interface.
- **Zerox**: Library used for OCR processing.
- **AI/ML API**: Provides the GPT-4o model for text analysis.
- **LiteLLM**: Used under the hood for model interactions.

## More Details

- **Zerox Library**: Transforms uploaded documents into images and performs OCR to extract text.
- **AI/ML API's GPT-4o**: Analyzes the extracted text, enabling advanced features like summarization or content analysis.
- **Gradio Interface**: Offers an intuitive web-based UI for users to interact with the app seamlessly.

## Future Improvements

1. **Batch Processing**: Enable users to upload and process multiple documents at once.
2. **Advanced Formatting Preservation**: Improve the ability to retain complex layouts, tables, and graphics.
3. **User Accounts**: Implement authentication to allow users to save and manage their processed documents.
4. **Cloud Integration**: Add options to upload documents from and save results to cloud storage services.

## Running the Repository

To run this project locally, follow these steps:

```bash
# 1. Clone the repository
git clone https://github.com/jadouse5/ocr-aimlapi-zerox.git
cd ocr-document-reader

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install system dependencies
# On Ubuntu/Linux
sudo apt-get update
sudo apt-get install -y poppler-utils

# On macOS (using Homebrew)
brew install poppler

# 4. Set up environment variables
# Create a .env file in the root directory and add:
OPENAI_API_KEY=your_api_key
OPENAI_API_BASE=https://api.aimlapi.com/v1  # Adjust if necessary

# 5. Run the application
python ocr_app.py

# 6. Open your browser and navigate to
http://localhost:7860
```

**Note**: Replace `your_api_key` with your actual API key for the AI/ML API.

## Hashtags

#OCR #AI #Gradio #Python #GPT4o #Zerox #TextAnalysis #MachineLearning

---

Feel free to customize this README with your own links, images, and additional details to better suit your project. This template follows the structure of the example you provided and highlights the key aspects of your OCR Document Reader application.
