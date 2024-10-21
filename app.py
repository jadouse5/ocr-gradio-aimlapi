import os
import gradio as gr
from pyzerox import zerox
import asyncio
import openai
import markdown2
from gradio_pdf import PDF

# Header
header = """
# 📄 OCR Reader, 🔍 Analyzer, and 💬 Chat Assistant using 🔎 Zerox, 🧠 GPT-4o, powered by 🚀 AI/ML API

Author: Jad Tounsi El Azzoiani
GitHub: [https://github.com/jadouse5](https://github.com/jadouse5)
LinkedIn: [Jad Tounsi El Azzoiani](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)

This project uses:
- [AI/ML API](https://api.aimlapi.com)
- [Gradio](https://www.gradio.app)
- [pyzerox](https://github.com/getomni-ai/zerox?tab=readme-ov-file#python-zerox)
"""

# Set up the model and provider
model = "gpt-4o"  # GPT-4o model from AI/ML API

# Set the environment variables for the AI/ML API
os.environ["OPENAI_API_KEY"] = "your_api_key_here"
os.environ["OPENAI_API_BASE"] = "https://api.aimlapi.com/v1"

# Initialize the OpenAI client
client = openai.OpenAI(
    api_key=os.environ["OPENAI_API_KEY"],
    base_url=os.environ["OPENAI_API_BASE"]
)

# Async function to process the file using Zerox OCR and GPT-4o
async def process_file(file):
    file_path = file.name
    result = await zerox(
        file_path=file_path,
        model=model,
        cleanup=True,
        concurrency=5,
        maintain_format=True,
    )
    content = "\n\n".join([page.content for page in result.pages])
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI assistant that analyzes OCR output. Provide your analysis in markdown format, using bold text, tables, and other formatting as appropriate to make the information clear and easy to read."},
            {"role": "user", "content": f"Analyze the following OCR output and provide a summary:\n\n{content}"}
        ],
        temperature=0.7,
        max_tokens=500
    )
    
    ai_analysis = response.choices[0].message.content
    ai_analysis_html = markdown2.markdown(ai_analysis)
    
    return content, ai_analysis_html, file_path

# Function to handle chat with AI
def chat_with_ai(message, chat_history, document_content):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an AI assistant that can answer questions about a document. Use the document content to provide accurate answers."},
            {"role": "user", "content": f"Document content: {document_content}"},
            {"role": "user", "content": message}
        ],
        temperature=0.7,
        max_tokens=150
    )
    ai_response = response.choices[0].message.content
    chat_history.append((message, ai_response))
    return "", chat_history

# Build the Gradio interface
with gr.Blocks() as demo:
    gr.Markdown(header)
    
    api_key_input = gr.Textbox(
        label="Enter your AI/ML API Key",
        type="password",
        placeholder="Enter your API key here"
    )
    
    file_input = gr.File(label="Upload Document", file_types=[".pdf", ".docx", ".jpg", ".png", ".jpeg"])
    
    with gr.Row():
        ocr_output = gr.Textbox(label="Extracted Text", lines=10, scale=3)
        run_button = gr.Button("Run OCR and Analysis", scale=1)
    
    with gr.Row():
        with gr.Column(scale=1):
            pdf_viewer = PDF(label="Original Document", interactive=False)
        with gr.Column(scale=1):
            ai_analysis_output = gr.HTML(label="AI Analysis")
    
    gr.Markdown("## Chat with AI about the document")
    chatbot = gr.Chatbot()
    msg = gr.Textbox(label="Ask a question about the document")
    clear = gr.Button("Clear")
    
    document_content = gr.State()

    def process_and_display(file, api_key):
        os.environ["OPENAI_API_KEY"] = api_key
        client.api_key = api_key
        content, analysis, file_path = asyncio.run(process_file(file))
        return file_path, content, analysis, content

    run_button.click(
        process_and_display,
        inputs=[file_input, api_key_input],
        outputs=[pdf_viewer, ocr_output, ai_analysis_output, document_content]
    )

    msg.submit(chat_with_ai, [msg, chatbot, document_content], [msg, chatbot])
    clear.click(lambda: None, None, chatbot, queue=False)

    footer = gr.Markdown("""
    ---
    Created by Jad Tounsi El Azzoiani | [GitHub](https://github.com/jadouse5) | [LinkedIn](https://www.linkedin.com/in/jad-tounsi-el-azzoiani-87499a21a/)
    
    Powered by [AI/ML API](https://api.aimlapi.com), [Gradio](https://www.gradio.app), and [pyzerox](https://github.com/getomni-ai/zerox?tab=readme-ov-file#python-zerox)
    """)

demo.launch()
